# Venue Config.
event_registry = {
    "total capacity": 10,
    "ticket price": 250
}

# Booking ledger
customer_name = []
tickets_booked = []

# The Inquiry Phase
while event_registry["total capacity"] > 0:
    # Fixed the nested double quotes inside the f-string here:
    print(f"\nWelcome! {event_registry['total capacity']} seats are currently remaining for tonight's flight.")

    name = input("Enter Your Name: ")
    tickets = int(input("No. of tickets: "))

    # GATE 1: Input Sanity Check
    if tickets > 0:
        print("Processing your booking...")

        # GATE 2: Capacity Check (Nested INSIDE Gate 1)
        if tickets <= event_registry["total capacity"]:
            print("Approved")
            event_registry["total capacity"] -= tickets

            customer_name.append(name)
            tickets_booked.append(tickets)

            # Financial Calculation & State Mutation
            ticket_price = event_registry["ticket price"]
            total_cost = tickets * ticket_price
            
            print(f"Your Final Bill ₹{total_cost}")
            print("Booking Successful! Thank you!")
        else:
            print(f"Booking Failed! Only {event_registry['total capacity']} seats left.")
            
    else:
        print("Invalid number of tickets! Please enter a number greater than 0.")

print("\nSOLD OUT")

