from menu import *

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
            view_expenses()

        elif choice == 3:
            print("Welcome to Search Expenses🔎")
            search_expenses()

        elif choice == 4:
            print("Welcome to Updated Expenses➕")
            update_expenses()

        elif choice == 5:
            print("Welcome to Delete Expenses")
            delete_expenses()
            
        elif choice == 11:
            print("Thnaks for saving up Money💰")  
            print("Keep it going!")
            running = False
            break 


if __name__ == "__main__":
    main()