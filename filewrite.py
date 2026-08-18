from database import *
import json 
import csv

def save_files(expenses):
    file_path = "C:/Users/victus/OneDrive/Desktop/expenses.json"

    data = []

    data.append({
  
      "description": expenses.description,
      "catagory": expenses.catagory,
      "amount": expenses.amount,
      "date": expenses.date.strftime("%Y-%m-%d"),

    })

    with open(file_path, "x") as file:
     json.dump(data, file, indent=4)
     print(f"Json file Created with path {file_path}")