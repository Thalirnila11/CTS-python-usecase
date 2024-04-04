class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited ${amount}."
        else:
            return "Invalid deposit amount."

# Example usage
if __name__ == "__main__":
    account = BankAccount()
    amount = float(input("Enter the amount to deposit: "))
    print(account.deposit(amount))
