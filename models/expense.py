from menu import *

class Add_expense:

     description_ID = 1101
     def __init__(self, description, amount, catagory, date):
          self.description = description
          self.amount = amount
          self.catagory = catagory
          self.date = date
          Add_expense.description_ID += 1