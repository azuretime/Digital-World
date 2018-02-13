class Account:    
    def __init__(self, owner, account_number, amount): 
        self.owner = owner
        self.account_number = account_number
        self.balance = amount

    def __str__(self):
        return '%s, %s, balance: %r' %(self.owner, self.account_number, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#my anw
class Account:
    def __init__(self, owner, account_number, amount):
        self.owner=owner
        self.account_number=account_number
        self.amount=amount
        
    def deposit(self, amount):
        self.amount+=amount
        return self.amount
        
    def withdraw(self, amount):
        self.amount-=amount
        return self.amount
        
    def __str__(self):
        str=self.owner+' , '+self.account_number+' , balance: %d'%(self.amount)
        return str
        
a1 = Account ('John Olsson', '19371554951', 20000)
a2 = Account ('Liz Olsson', '19371564761', 20000)
a1. deposit (1000)
a1. withdraw (4000)
a2. withdraw (10500)
a1. withdraw (3500)
print a1
print a2