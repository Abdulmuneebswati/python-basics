

class BankException(Exception):
    pass

class BankAccount():
    def __init__(self,initial_amount,acc_name):
        self.balance = float(initial_amount)
        self.name = acc_name

    def getBalance(self):
        print(f"\n Account:'{self.name}' created \n Balance: ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited...")
        self.getBalance()
    def viableTransation(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BankException("Insufficient Balance")
    def withDraw(self,amount):
        try:
            self.viableTransation(amount)
            self.balance -= amount
            self.getBalance()
        except BankException as error:
            print(f"With draw interrupted:{error}")
    def transfer(self,amount,account):
        try:
            print("\n******Transaction started********")
            self.viableTransation(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print("\n transaction completed")

        except BankException as error:
            print(f"Transaction interrupted:{error}")




class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("Deposit complete")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5
    
    def withDraw(self, amount):
        try:
            self.viableTransation(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\n withdraw completed")
            self.getBalance()
        except BankException as error:
            print(f"withdraw interrupted:{error}")