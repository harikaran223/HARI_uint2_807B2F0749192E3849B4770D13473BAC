class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposit of ${amount} successful. New balance: ${self.__account_balance}")
      else:
          print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrawal of ${amount} successful. New balance: ${self.__account_balance}")
      else:
          print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
      print(f"Account Balance for {self.__account_holder_name} (Account Number: {self.__account_number}): ${self.__account_balance}")
account_holder_name = input("Enter the account holder's name: ")
account_number = input("Enter the account number: ")
account1 = BankAccount(account_number=account_number, account_holder_name=account_holder_name, initial_balance=1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()