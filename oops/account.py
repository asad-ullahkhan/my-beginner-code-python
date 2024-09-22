class account:
    def __init__(self,name,bal,acc_no):
        self.name=name
        self.balance=bal
        self.account_no=acc_no
    def debit(self,amount):
        self.balance-=amount
        print(f"{amount} is debited from your account")
        print("current balance=",self.get_balance()) 
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} is credited to your account")
        print("current balance=",self.get_balance()) 
    def get_balance(self):
        return self.balance           

acc1=account("asad",45000,"aaa1111")
print(acc1.debit(25000))
print(acc1.credit(45000))


