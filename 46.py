accounts = {101: 1000, 102: 2000, 103: 3000}
def menu(acc_no):
    while True:
        print("\n-------- Banking Menu ----------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Exit to Main Menu")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Your balance: {}".format(accounts[acc_no]))

        elif ch == 2:
            amount = int(input("Enter deposit amount: "))
            accounts[acc_no] += amount
            print("{} deposited. New balance: {}".format(amount, accounts[acc_no]))

        elif ch == 3:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= accounts[acc_no]:
                accounts[acc_no] -= amount
                print("{} withdrawn. Remaining balance: {}".format(amount, accounts[acc_no]))
            else:
                print("Insufficient balance or invalid amount.")

        elif ch == 4:
            to_acc = int(input("Enter receiver account number: "))
            amount = int(input("Enter amount to transfer: "))
            if to_acc in accounts and to_acc != acc_no:
                if amount <= accounts[acc_no]:
                    accounts[acc_no] -= amount
                    accounts[to_acc] += amount
                    print("{} transferred to account {}".format(amount, to_acc))
                    print("Your new balance: {}".format(accounts[acc_no]))
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid recipient account number.")

        elif ch == 5:
            print("Returning to main menu\n")
            break

        else:
            print("Invalid choice. Please try again.")

while True:
    print("\n-------- Welcome to Banking System ----------")
    ch = int(input("Enter your Account Number (or 0 to exit): "))
    if ch in accounts:
        menu(ch)
    elif ch == 0:
        print("Exiting the system")
        break
    else:
        print("Invalid account number. Try again")
