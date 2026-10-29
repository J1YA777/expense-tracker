import os 

expenses = []  


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_header():
    print("===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")


def add_expense():
    amount = float(input("Enter amount: "))  
    category = input("Enter category: ")

    expense = {"amount": amount, "category": category}

    expenses.append(expense)

    print("\nExpense added!")
    input("\nPress Enter to return to menu...") 


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet!")
        input("\nPress Enter to return to menu...")
        return

    print("\nYour Expenses:")

    for expense in expenses:
        amt = expense["amount"]
        cat = expense["category"]

        print("Amount:", amt, "| Category:", cat)

    input("\nPress Enter to return to menu...")


def total_spending():
    if not expenses:
        print("\nNo expenses recorded yet!")
        input("\nPress Enter to return to menu...")
        return

    total = 0
    categories = []

    for expense in expenses:
        total = total + expense["amount"]
        categories.append(expense["category"])

    categories_str = ", ".join(categories)

    print("\nTotal Spending:", total)
    print("Categories spent on:", categories_str)

    input("\nPress Enter to return to menu...")


while True:
    clear_screen()  
    show_header()   

    choice = input("\nChoose an option: ")

    if choice == "1":
        clear_screen()
        show_header()
        add_expense()

    elif choice == "2":
        clear_screen()
        show_header()
        view_expenses()

    elif choice == "3":
        clear_screen()
        show_header()
        total_spending()

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
        input("\nPress Enter to return to menu...")
