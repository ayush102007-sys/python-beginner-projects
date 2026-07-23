# ATM Bank System Setup
bank_database = {
    12345 : {
    'a/c holder': 'Binni',
    'PIN': 2007,
    'a/c balance': 5000
},
    67890 : {
    'a/c holder': 'Kali',
    'PIN': 6789,
    'a/c balance': 20000
},
    55555 : {
    'a/c holder': 'Ankush',
    'PIN': 1020,
    'a/c balance': 12000
},
    10200 : {
    'a/c holder': 'Ayush',
    'PIN': 2026,
    'a/c balance': 15000
},
    61295 : {
    'a/c holder': 'Rajib',
    'PIN': 1995,
    'a/c balance': 25000
}
}

account_no = int(input("Enter your Account Number: "))

if account_no in bank_database:

    active_user = bank_database[account_no]

    print(f"Welcome back, {active_user['a/c holder']}!")

    failed_attempts = 0
    transaction_limit = 2000

    choice_1 = input("Do you want to check bank a/c status? (YES/NO)-> ").strip().lower()

    if choice_1 == 'yes':
        # LOOP 1: Security Access Control Gate
        while failed_attempts < 3:
            pin = int(input("Enter your PIN no: "))

            if bank_database[account_no]['PIN'] == pin:
                print("\nAuthenticated successfully...")

                # LOOP 2: Active Transaction Session Loop
                while True:
                    print(f"\nYour balance: ₹{bank_database[account_no]['a/c balance']}")
                    choice = input("Deposit / Withdraw / Exit -> ").strip().lower()

                    if choice == 'deposit':
                        deposit_money = int(input("Amount : "))
                        if deposit_money > 0:
                            bank_database[account_no]['a/c balance'] += deposit_money

                            print(f"Your account balance: ₹{bank_database[account_no]['a/c balance']}")
                        else:
                            print("Invalid deposit amount.")

                    elif choice == 'withdraw':
                        withdraw_money = int(input("Amount : "))

                        if (withdraw_money <= bank_database[account_no]['a/c balance']) and (withdraw_money <= transaction_limit):
                            bank_database[account_no]['a/c balance'] -= withdraw_money
                            print(f"Your account balance: ₹{bank_database[account_no]['a/c balance']}")
                        elif withdraw_money > transaction_limit:
                            print("Exceeds ATM single transaction limits.")
                        else:
                            print("Insufficient Funds.")

                    elif choice == 'exit':
                        print("Logged Out... Thank you!")
                        break  # Breaks Loop 2 (Ends the active banking session)
                    else:
                        print("Invalid option selected.")

                break # Breaks Loop 1 (Prevents asking for PIN again after logout)

            else:
                failed_attempts += 1
                print(f"PIN Not Matched. Attempts remaining: {3 - failed_attempts}")

        if failed_attempts == 3:
            print("\nCard Confiscated due to 3 failed entry attempts.")

    print("Goodbye!")

else:
    print("Account not found.")
