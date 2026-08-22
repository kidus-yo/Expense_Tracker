from menu import *
from filewrite import *
import database

def main():
    running = True
    while running:
        choice =  main_menu()

        if choice == 1:
            print("*" * 30)
            print("Welcome to Add Expenses🫰")
            print("*" * 30)
            add_expenses()

        elif choice == 2:
            print("Welcome to View Expenses🪟")
            print()
            view_expenses()

        elif choice == 3:
            print("Welcome to Search Expenses🔎")
            print()
            search_expenses()

        elif choice == 4:
            print("Welcome to Updated Expenses➕")
            print()
            update_expenses()

        elif choice == 5:
            print("Welcome to Delete Expenses➖")
            print()
            delete_expenses()

        elif choice == 6:
            print("Welcome to Expense Satstics📊")
            print()
            expense_statistics(highest, lowest)

        elif choice == 7:
            print("Welcome to Catagory Summary📇")
            print()
            catagory_summary()

        elif choice == 8:
            print("Welcome to monthly summary🈷️")
            print()
            monthly_summary()

        elif choice == 9:
            print("Welcome to Expert Report🤓")
            print()
            expert_report()

        elif choice == 10:
            print()
            clear_expenses()
        elif choice == 11:
            save_files(expenses)
            print("File Saved Successfully!✅")
        elif choice == 12:
            print("-" * 30)
            print("Thnaks for Tracking your Expenes💰")  
            print("Keep it going!")
            running = False
            break 

  
if __name__ == "__main__":
    database.expenses.extend(load_files())
    main()