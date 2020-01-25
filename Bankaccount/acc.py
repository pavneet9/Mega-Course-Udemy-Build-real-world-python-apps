#

class Account:

    def __init__(self, filename):
        self.filepath = filename
        with open(filename,"r") as file:
            self.balance = int(file.read())

    def withraw(self,funds):
        self.balance = self.balance - funds

    def deposit(self,funds):
        self.balance = self.balance + funds

    def commit():
        with open(self.filepath,"w") as file:
            file.write(str(self.balance))

class Checking(Account):
    def __init__(self)
          Account.__init__(self, filename)
    def transfer(self,funds):
        self.balance = self.balance - funds

account = Account("balance.txt.txt")
print (account.balance)
