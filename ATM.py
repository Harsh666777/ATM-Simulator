def atm_simulator():
    pin = '1007'
    attempts = 0
    
    while attempts < 3:
        entered_pin = input("Please enter your PIN: ")
        
        if entered_pin == pin:
            print("PIN accepted. Welcome to the ATM!")
            while True:
                print("\nOptions:")
                print("1. Check balance")
                print("2. Withdraw funds")
                print("3. Deposit funds")
                print("4. Exit")
                choice = input("Please select an option (1-4): ")

                if choice == '1':
                    print("Your balance is $99999999")  
                elif choice == '2':
                    amount = float(input("Enter the amount to withdraw: "))
                    print("Withdrawn $", amount)
                elif choice == '3':
                    amount = float(input("Enter the amount to deposit: "))
                    print("Deposited $", amount)
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please select a valid option.")
        else:
            attempts += 1
            print("Incorrect PIN. Please try again.")
    
    print("Too many incorrect attempts. Exiting...")
    

atm_simulator()