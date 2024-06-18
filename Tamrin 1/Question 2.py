class BankAccount:
    def __init__ (self, balance=0):
        self.balance = balance

    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print (f"{amount} deposited. New balance is {self.balance}.")
        else:
            print ("Invalid amount. Please enter a positive amount.")

    def withdraw (self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print (f"{amount} withdrawn. New balance is {self.balance}.")
            else:
                print ("Insufficient balance.")
        else:
            print ("Invalid amount. Please enter a positive amount.")

    def check_balance (self):
        print (f"Your balance is {self.balance}.")


def main ():
    account = BankAccount ()

    while True:
        print ("\nWelcome to the Bank Account Management System")
        print ("1. Deposit money")
        print ("2. Withdraw money")
        print ("3. Check balance")
        print ("4. Exit")

        choice = input ("Please choose an option (1-4): ")

        if choice == '1':
            amount = float (input ("Enter the amount to deposit: "))
            account.deposit (amount)
        elif choice == '2':
            amount = float (input ("Enter the amount to withdraw: "))
            account.withdraw (amount)
        elif choice == '3':
            account.check_balance ()
        elif choice == '4':
            print ("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print ("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main ()
