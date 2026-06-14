inventory = []
print("Woke up in a cabin")
print("Looked out window, saw a bear")

while True:
    choice_1 = input("\nDo you want to (scream/hide)? ").strip().lower()
    if choice_1 == "scream":
        print("Bear hears you, GAME OVER!!")
        break
    else:
        print("Bear walks away")
        print("Walked out front door, found a bicycle", end='')
        choice_2 = input("\n Do you want to (ride/stay)? ").strip().lower()
        if choice_2 == "stay":
            print("You got lost in the yard, GAME OVER!!")
            break
        else:
            print("""You cycled to safety
            Now you found a chset""")
            choice_3 = input("\n Do you want to open it(yes/no)? ").strip().lower()

            if choice_3 == "no":
                print("Journey continues...")

            else:
                print("You found a key!!")
                inventory.append("KEY")
                print("Journey continues...")

            if "KEY" in inventory:
                print("""You found a HUGE BOX
                You found a DIAMOND!!!""")

            else:
                print("""You found a HUGE BOX
                But You can't open it, GAME OVER""")

            break



















