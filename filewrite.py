from database import *
import json 
import csv

def save_files(expenses):
    file_path = "C:/Users/victus/OneDrive/Desktop/expenses.txt"

    with open(file_path, "w") as file:
     for lists in expenses:
      file.write(lists)
     print(f"Json file Created with path {file_path}")