class BankAccount:
    def __init__(self, account_no, holder_name, account_balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print("The deposited amount is :", amount)
        else:
            print("The deposited amount ",amount,"is invalid")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawl amount is:", amount)
        elif amount<= self.account_balance:
            self.account_balance -= amount
            print("The withdrawl mount is :", amount)
        else:
            print("Insufficient balance")

    def checkBalance(self):
        print("Account No :", self.account_no)
        print("Account Holder Name :", self.holder_name)
        print("Account Balance :", self.account_balance)

# create boject of BnkAccount
b1 = BankAccount("sb101", "kedar", 67000)
b2 = BankAccount("sb103", "varun", 23000)

print("Account 1")
b1.checkBalance()
b1.deposit(3000)
b1.withdraw(7000)
print()
b1.checkBalance()
print()

print("Account 2")
b2.checkBalance()
b2.deposit(1000)
b2.withdraw(10000)
print()
b2.checkBalance()
print()

