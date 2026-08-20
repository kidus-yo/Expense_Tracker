from menu import *

class Add_expense:

     description_ID = 1101
     total_expense = 0
     total_count = 0

     def __init__(self, description, amount, catagory, date):
          self.description = description
          self.amount = amount
          self.catagory = catagory
          self.date = date

          Add_expense.description_ID += 1
          Add_expense.total_count += 1
          Add_expense.total_expense += amount

     @classmethod
     def get_count(cls):
          return f"{cls.total_count}"

     @classmethod
     def get_average(cls):
          return f"Average Expense: {cls.total_expense / cls.total_count}"
