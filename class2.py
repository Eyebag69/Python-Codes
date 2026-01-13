class Account:
  def __init__(self, account_no, holder_name, balance):
    self.account_no = account_no
    self.holder_name = holder_name
    self.balance = balance
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    self.balance -= amount
  def show_balance(self):
    print(self.balance)
class SavingsAccount(Account):
  def __init__(self, account_no, holder_name, balance, interest_rate):
    super().__init__(account_no, holder_name, balance)
    self.interest_rate = interest_rate
  def add_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
s = SavingsAccount("SB101", "Aashish", 5000, 0.04)
s.deposit(400)
s.show_balance()


