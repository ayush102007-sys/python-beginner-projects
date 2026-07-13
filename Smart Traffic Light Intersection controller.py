import random
import time

# Junction Configuration
current_light_colour = "Red"
# Start with initial traffic
lane_database = {
    "[North]": [current_light_colour, random.randrange(1, 20)],
    "[South]": [current_light_colour, random.randrange(1, 20)],
    "[East]": [current_light_colour, random.randrange(1, 20)],
    "[West]": [current_light_colour, random.randrange(1, 20)]
}

active_lane = None  # Persistent tracker across loops

# Creating program loop and Counting no of cars/Summation
while sum(lane_info[1] for lane_info in lane_database.values()) > 0:

    # Timing rules
    minimum_time = 10
    extra_per_count = 2
    maximum_time = 45

    # Sensor pulse display
    print(f"""
==================================================
📊 LIVE SENSOR SCAN:
North: {lane_database["[North]"][1]} cars
South: {lane_database["[South]"][1]} cars
East:  {lane_database["[East]"][1]} cars
West:  {lane_database["[West]"][1]} cars
==================================================
    """)

    # 🔧 FIX 1: Robustly find the lane name with the highest car count
    # This avoids comparing lists and prevents the StopIteration crash completely!
    priority_lane = max(lane_database, key=lambda k: lane_database[k][1])
    max_cars = lane_database[priority_lane][1]

    # Dynamic Timer Calculation
    calculated_time = minimum_time + (max_cars * extra_per_count)
    print(f"Initial calculated time -> {calculated_time} seconds")

    if calculated_time > maximum_time:
        calculated_time = maximum_time
        print(f"⚠️ Guardrail Activated! Time capped at maximum limit.")

    print(f"Final Applied 🟢 Green Light Time: {calculated_time} seconds\n")
    time.sleep(1)

    # State Shift execution: Handle the Old Lane first if it exists!
    if active_lane is not None:
        old_lane = active_lane
        print(f"🔄 Phase A: Changing {old_lane} from 🟢 GREEN to 🟡 YELLOW.")
        lane_database[old_lane][0] = "Yellow"
        time.sleep(1)

        print(f"{old_lane} lane is 🟡 YELLOW... Slowing down traffic...")
        t = 3
        while t > 0:
            minutes, seconds = divmod(t, 60)
            time_string = f"{minutes:02d}:{seconds:02d}"
            print(time_string, end="", flush=True)
            time.sleep(1)
            t -= 1
            print("\b" * len(time_string), end="", flush=True)
        
        print("\n🟡 Yellow timer expires!")
        
        # Phase B: All Red Lock-down
        lane_database[old_lane][0] = "Red"
        print("🚨 [ ALL GATES RED: 🔴 North | 🔴 South | 🔴 East | 🔴 West ]")
        print("Clearing intersection buffer safely...")
        time.sleep(2)

    # Phase C: Switch target to green
    active_lane = priority_lane
    lane_database[active_lane][0] = "Green"
    print(f"🚦 TRAFFIC LOG: {active_lane} Lane switched to 🟢 Green for {calculated_time} seconds. Clearing backlog...")

    # Green light timer for active_lane
    while calculated_time > 0:
        minutes, seconds = divmod(calculated_time, 60)
        time_string = f"{minutes:02d}:{seconds:02d}"
        print(time_string, end="", flush=True)
        time.sleep(1)
        calculated_time -= 1
        print("\b" * len(time_string), end="", flush=True)

    print("\n🟢 Green light expires!")
    lane_database[active_lane][1] = 0  # Clear cars out of the active green lane

    # 🔧 FIX 2: Simulate traffic progression by adding new cars randomly to waiting lanes
    for lane, details in lane_database.items():
        if lane != active_lane:  # Only add cars to lanes that had a red light
            details[1] += random.choice([0, 1, 2, 3])  # New cars piling up

print("\n🎉 All lanes clear! Intersection simulation completed successfully.")
