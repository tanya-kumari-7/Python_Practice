import pandas as pd
import os

def add_expenses_func(date: str, amount: float, expense_type: str, expense_budget: float):
    """ 
    Expense Tracker with Monthly Summary
    - Appends new expense to expenses_book.txt
    - Writes full data including calculated fields to expenses_book_new.txt
    - Returns status message
    """
    # Validation
    if not date or expense_type.strip() == "" or amount is None or expense_budget is None:
        return {"Error": "Please enter complete details. All fields are mandatory."}

    file_path = "expenses_book.txt"
    new_file_path = "expenses_book_new.txt"

    # Ensure raw file exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")

    # Append new raw record
    with open(file_path, 'a') as file:
        file.write(f"{date}|{amount}|{expense_type}|{expense_budget}\n")

    # Load all data
    df = pd.read_csv(
        file_path,
        sep="|",
        names=["Date", "Amount", "Expense Type", "Expense Budget"],
        parse_dates=["Date"]
    )

    # Add calculated columns
    df["Month"] = df["Date"].dt.strftime("%B-%Y")
    df["Total_exp"] = df.groupby("Month")["Amount"].transform("sum")
    df["Remaining_budget"] = df["Expense Budget"] - df["Total_exp"]

    # Save full dataset with calculated fields to new file
    df.to_csv(new_file_path, sep="|", index=False, header=True)

    # Latest entry for return message
    last = df.iloc[-1]
    to_be_returned = f"""
    Expense Added Successfully!
    Month: {last['Month']}
    Total Expense: {last['Total_exp']}
    Remaining Budget: {last['Remaining_budget']}

    Full summary saved to: {new_file_path}
    """
    return to_be_returned


add_expenses_func("2025-09-01", 1200, "Food", 10000)
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
add_expenses_func("2025-12-20", 500, "Snacks", 100000)


