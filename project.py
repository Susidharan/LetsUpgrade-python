#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhara
#
# Created:     15-06-2023
# Copyright:   (c) dhara 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class user():
 def __init__(self, name, age, gender):
  self.name = name
  self.age = age
  self.gender = gender

 def show_details(self):
        print("Personal Details :-")
        print(" ")
        print("name : ", self.name)
        print("age : ", self.age)
        print("gender : ", self.gender)

class Bank(user):
    def __init__(self, name, age, gender):
      super().__init__(name, age, gender)
      self.balance = 0

    def deposit(self, amount):
      self.amount = amount
      self.balance = self.balance+self.amount
      print("The account balance has been updated : INR ", self.balance)

    def withdraw(self, amount):
      self.amount = amount
      if self.amount > self.balance:
        print("Insufficient Funds | Balance Available : INR ")
      else:
        self.balance = self.balance - self.amount
        print("The account balance has been updated : INR ", self.balance)
    def view_balance(self):
        self.show_details()
        print("The account balance has been updated : INR ", self.balance)