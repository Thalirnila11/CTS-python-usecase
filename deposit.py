class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited ${amount}."
        else:
            return "Invalid deposit amount."
    def withdraw(self, amount):
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    return f"Withdrew ${amount} successfully."
                else:
                    return "Insufficient funds."
            else:
                return "Invalid withdrawal amount."

    def check_balance(self):
        return f"Your current balance is ${self.balance}."
    def view_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transaction history.")

# Example usage
if __name__ == "__main__":
    account = BankAccount()
    amount = float(input("Enter the amount to deposit: "))
    print(account.deposit(amount))
    withdrawal_amount = float(input("Enter the amount to withdraw: "))
    print(account.withdraw(withdrawal_amount))
    print(account.check_balance())
    account.view_transaction_history()
