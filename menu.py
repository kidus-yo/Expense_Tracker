from models.expense import *
from database import *   

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
    print("11. Exit")

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

     try:
        description = input("Enter your description... ")
     except ValueError:
        print("Please Enter only the required inputs")
     except Exception:
        print("Something is Wrong")

     try:
        amount = int(input("Enter an amount: "))
     except ValueError:
        print("Please Enter only the required inputs")
     except Exception:
            print("Something is Wrong")

     try:        
      catagory = input("Enter Catagory: ")
     except ValueError:
      print("Please Enter only the required inputs")
     except Exception:
            print("Something is Wrong")

     try:
      date = input("Enter Date: ")
     except ValueError:
          print("Please Enter only the required inputs")
     except Exception:
             print("Something is Wrong")

     add = Add_expense(description, amount, catagory, date)
     expenses.append(add)
     print("-" * 30)
     print(f"Your Expense ID is: {Add_expense.description_ID}")
     print("Expense Added Successfully!✅")
     print("-" * 30)
   
def view_expenses():

    for view in expenses:
     print()
     print("-" * 30)
     print(f"Description: {view.description}")
     print(f"Amount: {view.amount}")
     print(f"Category: {view.catagory}")
     print(f"Date: {view.date}")
     print("-" * 30)

     print("Here are all your expense🫰")

def search_expenses():
  try:
    enter_ID = int(input("Please Enter your expense ID: "))
    if enter_ID == Add_expense.description_ID:
     for view in expenses:
        print()
        print("-" * 30)
        print(f"Description: {view.description}")
        print(f"Amount: {view.amount}")
        print(f"Category: {view.catagory}")
        print(f"Date: {view.date}")
        print(f"Your Expense ID is: {Add_expense.description_ID}")
        print("-" * 30)
        print("Here are all your expense🫰")

  except ValueError:
      print("Please Enter only the required inputs!")
  except Exception:
     print("Something went Wrong!")

def update_expenses():
   try:
    enter_ID = int(input("Please Enter your Expense ID: "))
    if enter_ID == Add_expense.description_ID:
       try:
        description1 = input("Enter your description... ")
       except ValueError:
         print("Please Enter only the required inputs")
       except UnboundLocalError:
          print("Not Associated with Value")
       except Exception:
         print("Something went Wrong")
       
       try:
         amount1 = int(input("Enter an amount: "))
       except ValueError:
          print("Please Enter only the required inputs")
       except UnboundLocalError:
          print("Not Associated with Value")
       except Exception:
            print("Something went Wrong")
       
       try:        
         catagory1 = input("Enter Catagory: ")
       except ValueError:
          print("Please Enter only the required inputs")
       except UnboundLocalError:
          print("Not Associated with Value")
       except Exception:
          print("Something went Wrong")
       
       try:
          date1 = input("Enter Date: ")
       except ValueError:
          print("Please Enter only the required inputs")
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
   print("==Catagory Summary==")
   for expense in expenses:
      print(f"  {expense.catagory}.............{expense.amount}$")


def monthly_summary():
   pass