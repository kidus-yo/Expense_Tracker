from database import *
import json 
import csv
from models.expense import *
import datetime

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

   try:
     with open(file_path, 'r') as file:
      content = json.load(file)
   except FileNotFoundError:
      print("File Not Found!")

      load_expenses = []

      for data in content:
       expense = Add_expense(
         data["description"],
         data["catagory"],
         data["amount"],
         datetime.strptime(data["date"], "%Y-%m-%d")

      )
       expense.description_ID = data["description_ID"]
       load_expenses.append(expense)

   if content:
      highest_id = max( description["description_ID"] for description in content)
      Add_expense.description_ID = highest_id + 1

   return load_expenses