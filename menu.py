from models.expense import *
from database import *
from datetime import datetime
import json 
from filewrite import *   

def main_menu():
    print("*" * 30)
    print("Expense Trakcer💰")
    print("*" * 30)
    print()
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Update Expenses")
    print("5. Delete Expenses")
    print("6. Expense Statstics")
    print("7. Category Summary")
    print("8. Monthly Summary")
    print("9. Expert Report")
    print("10. Clear All Expenes")
    print("11. Save Changes")
    print("12. Exit")

    try:
        choice = int(input("Please Enter your Choice: "))
        return choice 

    except ValueError:
        print("Error❌")
        print("Please Enter only the required input!!")

    except Exception:
        print("Error❌")
        print("Something Went Wrong!")

def add_expenses():

  
     description = input("Enter your description... ")
    

     while True:
      try:
         amount = int(input("Enter an amount: "))
         break
      except ValueError:
         print("Please Enter only the required inputs on amount")
      except Exception:
               print("Something is Wrong")

      
     catagory = input("Enter Catagory: ")
     

     while True:
      try:
         date_input = input("Enter Date(year-month-date): ")
         date = datetime.strptime(date_input, "%Y-%m-%d") 
         break
      except ValueError:
            print("Please Enter only the required inputs")
      except Exception:
               print("Something is Wrong")
 
     add = Add_expense(description, amount, catagory, date, )
     expenses.append(add)
     save_files(expenses)
     print("-" * 30)
     print(f"Your Expense ID is: {Add_expense.description_ID}")
     print("Expense Added Successfully!✅")
     print("-" * 30)
   
def view_expenses():
    
    print("-" * 30)
    for expense in expenses:
       print(f"Description_ID:{expense.description_ID}")
       print(f"Description: {expense.description}")
       print(f"Catagory: {expense.catagory}")
       print(f"Amount: {expense.amount}")
       print(f"Date: {expense.date}")
    print("-" * 30)

def search_expenses():
   try:
    enter_ID = int(input("Please Enter your expense ID: "))

    
    for expense in expenses:
       if enter_ID == expense.description_ID:
            print("-" * 30)
       
            print(f"Description_ID:{expense.description_ID}")
            print(f"Description: {expense.description}")
            print(f"Catagory: {expense.catagory}")
            print(f"Amount: {expense.amount}")
            print(f"Date: {expense.date}")
            print("-" * 30)
 
   except ValueError:
      print("Enter only the required inputs")

def update_expenses():
   
   try:
    enter_ID = int(input("Please Enter your Expense ID: "))
    if enter_ID == Add_expense.description_ID:
       try:
        description1 = input("Enter your description... ")
       except UnboundLocalError:
          print("Not Associated with Value")
       except Exception:
         print("Something went Wrong")

       while True:
         try:
            amount1 = int(input("Enter an amount: "))
            break
         except UnboundLocalError:
            print("Not Associated with Value")
         except Exception:
               print("Something went Wrong")
       
       try:        
         catagory1 = input("Enter Catagory: ")
       except UnboundLocalError:
          print("Not Associated with Value")
       except Exception:
          print("Something went Wrong")
       while True:
         try:
            date_input = input("Enter Date(year-month-date): ")
            date1 = datetime.strptime(date_input, "%Y-%M-%D")  
            break
         except ValueError:
            print("Please Enter only the required inputs!")
         except UnboundLocalError:
            print("Not Associated with Value")
         except Exception:
            print("Something went Wrong")
   except ValueError:
      print("Please Enter only the required inputs!")
   except Exception:
      print("Something Went Wrong!")   

   for view in expenses:
      view.desciption = description1
      view.amount = amount1
      view.catagory = catagory1
      view.date = date1

   print("Expense Updated Successfully!✅")

def delete_expenses():

   try:
      enter_ID = int(input("Enter your Expense ID: "))
      for removal in expenses:
       if enter_ID == Add_expense.description_ID:
         expenses.remove(removal)
         print("Expense data removed Successfully!✅")
   except ValueError:
      print("Please Enter only the required inputs")
   except Exception:
      print("Something went wrong")

def expense_statistics(highest, lowest):

   print(f"Total Expense: {Add_expense.total_expense}$")
   average = Add_expense.get_average()
   print(f"Average Expense: {average:.2f}$")

   for expense in expenses:
    if expense.amount >= highest:
       highest = expense.amount
       print(f"Highest: {highest}")

   for expense in expenses:
      if expense.amount <= lowest:
         lowest = expense.amount
         print(f"Lowest: {lowest}")

def catagory_summary():
   print("-" * 30)
   print("==Catagory Summary==")
   print("-" * 30)
   print("-" * 30)
   for expense in expenses:
    print(f"  {expense.catagory}.............{expense.amount}$")


   print("-" * 30)

def monthly_summary():
   print("-" * 30)
   print("Monthly Summary") 
   print("-" * 30)
   monthly_expenses = {}
   for expense in expenses:
      month_key = (expense.date.year, expense.date.month)

      if month_key in monthly_expenses:
           monthly_expenses[month_key] += expense.amount

      else:
         monthly_expenses[month_key] = expense.amount

   for key,values in monthly_expenses.items():
      print(f"Month, year: {key}..................Amount: {values}$")
   for spend in expenses:
      total = 0
      total += spend.amount
      print(f"Total Spending: {total}")
   print("These are your monthly expenses")
   print("-" * 30)

def expert_report():
 pass


def clear_expenses():
  expenses.pop()
  print("Expenses Removed Successfully!")
   