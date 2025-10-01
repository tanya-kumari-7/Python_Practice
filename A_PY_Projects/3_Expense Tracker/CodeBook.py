"""
Expense Tracker (CLI)
Input expenses (category, amount, date).
Store them in a CSV file.
Calculate monthly totals.
"""

# import pandas as pd
  
def add_expenses_func(date: str, amount: float, expense_type: str, expense_budget: float):
    """ 
    Welcome to Your Expenses Tracker !!!
    
    Please Follow the Filed Format
    date: in format yyyy-mm-dd
    amount: number (float or int)
    expense_type: string (like Food, Rent, Travel)
    expense_budget for Month: number (float or int)
    """
    if not date or not amount or not expense_type or not expense_budget:
        return {"Please Enter Completed Details As All Fileds Are Mandatory"}
    else:
        with open("expenses_book.txt",'a') as file:
            file.write(f"{date}|{amount}|{expense_type}|{expense_budget}\n")
            df = pd.read_csv("expenses_book.txt",
                             sep="|",
                             header=None,
                             names=["Date", "Amount", "Type", "Budget"])
            df["Date"] = pd.to_datetime(df["Date"],format="%Y-%m-%d")
            df["Date_month"] = pd.to_datetime(df["Date"],format="%m-%y").dt.strftime("%b-%y")
            df["Monthly_expense_till_date"] = df.groupby("Date_month")["Amount"].transform("sum")
            df["Remaning_amount"] = df["Budget"]-df["Monthly_expense_till_date"]
            df.to_csv("expenses_book.csv", index=False)
            return df
  
# add_expenses_func("2025-09-01", 1200, "Food", 10000)
# add_expenses_func("2025-09-02", 2500, "Rent", 10000)
# add_expenses_func("2025-09-03", 800, "Travel", 10000)
# add_expenses_func("2025-09-04", 600, "Entertainment", 10000)
# add_expenses_func("2025-09-05", 400, "Snacks", 10000)
# add_expenses_func("2025-09-06", 300, "Bills", 10000)
# add_expenses_func("2025-09-07", 900, "Shopping", 10000)
# add_expenses_func("2025-09-08", 700, "Medicine", 10000)
# add_expenses_func("2025-09-09", 1000, "Fuel", 10000)
# add_expenses_func("2025-09-10", 1200, "Food", 10000)
# add_expenses_func("2025-09-11", 1500, "Travel", 10000)
# add_expenses_func("2025-09-12", 500, "Snacks", 10000)
# add_expenses_func("2025-09-13", 600, "Bills", 10000)
# add_expenses_func("2025-09-14", 750, "Entertainment", 10000)
# add_expenses_func("2025-09-15", 850, "Shopping", 10000)
# add_expenses_func("2025-10-01", 3000, "Rent", 12000)
# add_expenses_func("2025-10-02", 1200, "Food", 12000)
# add_expenses_func("2025-10-03", 1500, "Travel", 12000)
# add_expenses_func("2025-10-04", 800, "Shopping", 12000)
# add_expenses_func("2025-10-15", 5000, "Snacks", 12000)

