class BankAccount: 
    def __init__(self): 
        self.balance=0
        self.trans=0
  
    def deposit(self): 
        amount=float(input("Amount to be Deposit:")) 
        self.balance += amount 
        self.trans+=1

    def withdraw(self): 
        amount = float(input("Amount to be Withdraw:")) 
        self.trans+=1
        if self.balance>=amount: 
            self.balance-=amount 
        else: 
            print("Balance Not Sufficient") 
  
    def deductFees(self):
        if self.trans>3:
            self.balance-=100
            print("100Rs deducted")
            
    def getBalance(self): 
        print("Current Balance=",self.balance) 
  
    
class CheckingAccount(BankAccount):
    pass

class SavingAccount(BankAccount):
    def addInterest(self):
        self.balance+=self.balance*0.005
a=SavingAccount()
a.deposit()
a.addInterest()
a.withdraw()
a.getBalance()
b=CheckingAccount()
b.deposit()
b.withdraw()
b.getBalance()
