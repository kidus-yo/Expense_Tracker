# 💰 Expense Tracker

A console-based **Expense Tracker** built with Python.
The purpose of this project is to practice building a real-world application using Python fundamentals, Object-Oriented Programming, file handling, JSON persistence, data analysis, and error handling.

---

## 📌 About the Project

The Expense Tracker allows users to record and manage their personal expenses through a simple command-line interface.

Users can add expenses, view and search their records, update or delete expenses, analyze their spending, and save their data so it remains available after the program is closed.

This project is also designed as a stepping stone toward building larger applications with databases, APIs, and graphical user interfaces.

---

## ✨ Features

### 💵 Expense Management

* Add new expenses
* View all expenses
* Search for expenses
* Update existing expenses
* Delete expenses
* Clear all expense records

### 🔎 Search

Search expenses by:

* Expense ID
* Description
* Category
* Date

### 📊 Statistics & Analysis

* Calculate total spending
* Calculate average expense
* Find highest expense
* Find lowest expense
* View spending by category
* View monthly spending summaries

### 💾 Data Persistence

* Save expenses to a JSON file
* Load saved expenses when the application starts
* Keep expense records after the program closes
* Handle missing or invalid data files

### 📄 Reports

* Generate expense reports
* Export expense information to files
* View summarized spending information

### 🛡️ Error Handling

The application handles common problems such as:

* Invalid numeric input
* Invalid dates
* Invalid expense IDs
* Negative expense amounts
* Empty descriptions
* Missing data files
* Invalid JSON data

---

## 🖥️ Main Menu

The application provides a menu similar to:

```text
╔══════════════════════════════════╗
║        💰 EXPENSE TRACKER        ║
╚══════════════════════════════════╝

1. Add Expense
2. View Expenses
3. Search Expenses
4. Update Expense
5. Delete Expense
6. Expense Statistics
7. Category Summary
8. Monthly Summary
9. Export Report
10. Clear All Expenses
11. Exit
```

---

## 🧾 Expense Information

Each expense contains information such as:

```text
ID
Description
Amount
Category
Date
```

Example:

```text
ID: 1001
Description: Groceries
Amount: $35.50
Category: Food
Date: 2026-08-14
```

---

## 🗂️ Project Structure

```text
expense-tracker/
│
├── main.py
├── menu.py
├── database.py
├── utils.py
├── reports.py
│
├── models/
│   ├── __init__.py
│   └── expense.py
│
├── data/
│   └── expenses.json
│
├── reports/
│   └── .gitkeep
│
├── README.md
├── requirements.txt
└── .gitignore
```

### File Responsibilities

| File / Directory     | Purpose                                            |
| -------------------- | -------------------------------------------------- |
| `main.py`            | Starts and controls the application                |
| `menu.py`            | Handles the user interface and menu operations     |
| `database.py`        | Handles loading and saving expense data            |
| `utils.py`           | Contains reusable utility and validation functions |
| `reports.py`         | Handles expense statistics and report generation   |
| `models/expense.py`  | Contains the `Expense` class                       |
| `data/expenses.json` | Stores expense records                             |
| `reports/`           | Stores generated reports                           |
| `README.md`          | Project documentation                              |
| `.gitignore`         | Prevents unnecessary files from being committed    |

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming
* Lists and Dictionaries
* Functions
* Exception Handling
* File Handling
* JSON
* `datetime`
* Git & GitHub

Additional libraries may be added as the project develops.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2. Navigate into the project

```bash
cd expense-tracker
```

### 3. Run the application

```bash
python main.py
```

---

## 💡 Example Workflow

A typical session might look like:

```text
1. Add Expense

Description: Groceries
Amount: 35.50
Category: Food
Date: 2026-08-14

Expense added successfully! ✅
```

The user can then view the expense:

```text
════════════════════════════════════════════
ID      DESCRIPTION       CATEGORY    AMOUNT
════════════════════════════════════════════
1001    Groceries         Food        $35.50
════════════════════════════════════════════
```

---

## 🎯 Learning Goals

This project is designed to strengthen my ability to:

* Design a Python application from scratch
* Use Object-Oriented Programming in a real project
* Organize Python code across multiple modules
* Work with JSON data
* Persist application data
* Handle user input safely
* Use exception handling
* Work with dates and times
* Search and manipulate collections of objects
* Calculate and analyze data
* Generate reports
* Structure a project professionally
* Use Git and GitHub effectively

---

## 🔮 Future Improvements

Possible future improvements include:

* [ ] PyQt5 graphical user interface
* [ ] SQLite database
* [ ] User accounts
* [ ] Password protection
* [ ] Budget management
* [ ] Spending limits
* [ ] Recurring expenses
* [ ] Data visualization
* [ ] CSV import/export
* [ ] REST API
* [ ] Web-based version

---

## 📚 Project Status

🚧 **In Development**

This project is being developed incrementally as a practical Python learning project.

New functionality will be added as the project progresses.

---

## 👨‍💻 Author

**Kidus Yonas**

Built as part of my journey toward becoming a software developer and eventually an AI engineer.

---

## 📄 License

This project is available for educational and personal use.
