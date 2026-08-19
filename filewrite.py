from database import *
import json 
import csv

def save_files(expenses):
    file_path = "C:/Users/victus/OneDrive/Desktop/expenses.json"

    data = []
    for expense in expenses:
     data.append({
    
      "description": expense.description,
      "catagory": expense.catagory,
      "amount": expense.amount,
      "date": expense.date.strftime("%Y-%m-%d"),
                                                                                                                            
    })

    with open(file_path, "w") as file:
     json.dump(data, file, indent=4)
     print(f"Json file Created with path {file_path}")