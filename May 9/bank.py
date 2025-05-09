class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    # Account details
    def __repr__(self):
        return "Account Holder: %s \nBalance: %.2f\n" % (self.name, self.balance)
    
    # To check balance
    def show_balance(self):
        print("Balance amount in the account: %.2f\n" % self.balance)

    # For making a deposit
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")
        self.show_balance()

    # For making a withdrawal
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
        self.show_balance()



def main():
    print("..............WELCOME TO THE BANKING SYSTEM................\n")
    name = input("Enter account holder's name: ")
    account = BankAccount(name)
    print("\nAccount created successfully!\n")

    while True:
        print("\n===== BANK ACCOUNT MENU =====")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Account Details")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account.show_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Enter a valid amount!")
                else:
                    account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Enter a valid amount!")
                else:
                    account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print(account)
        elif choice == '5':
            print("Thank you for using the bank account system.")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()
