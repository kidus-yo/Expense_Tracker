from database import *
import json 
import csv
from models.expense import *

def save_files(expenses):
  file_path = "C:/Users/victus/OneDrive/Desktop/expenses.json"

  data = []

  for expense in expenses:
      data.append({

      "description_ID": expense.description_ID,
      "description": expense.description,
      "catagory": expense.catagory,
      "amount": expense.amount,
      "date": expense.date.strftime("%Y-%m-%d"),
     
  })
 

  with open(file_path, "w") as file:
      json.dump(data, file, indent=4)
      print(f"Json file Created with path {file_path}")


def load_files():
   file_path = "C:/Users/victus/OneDrive/Desktop/expenses.json"

   with open(file_path, 'r') as file:
      content = json.load(file)

   if content:
      highest_id = max( description["description_ID"] for description in content)
      Add_expense.description_ID = highest_id + 1

   return content