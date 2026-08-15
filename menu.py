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
     print("Expense Added Successfully!✅")

   
 

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
    pass