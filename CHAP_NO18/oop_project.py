from bank_accounts import *

Dave = BankAccount("1000","Dave")
Sara = BankAccount("2000","Sara")


# Dave.deposit(100)
# Dave.viableTransation(10100)
# Dave.withDraw(1400)
# Dave.transfer(400,Sara)

# Jim = InterestRewardsAccount("1000","Jim")
# Jim.deposit(300)
# Jim.transfer(1200,Dave)

Muneeb = SavingsAccount("2000","Muneeb")

Muneeb.transfer(200,Sara)