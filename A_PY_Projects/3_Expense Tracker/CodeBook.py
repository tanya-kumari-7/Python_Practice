import pandas as pd

def add_expenses_func(date: str, amount: float, expense_type: str, expense_budget: float):
    """ 
    Expense Tracker with Monthly Summary
    """
    if not date or not amount or not expense_type or not expense_budget:
        return {"Error": "Please Enter Completed Details As All Fields Are Mandatory"}
    with open("expenses_book.txt", 'a') as file:
        file.write(f"{date}|{amount}|{expense_type}|{expense_budget}\n")
    df = pd.read_csv(
        "expenses_book.txt", 
        sep="|", 
        names=["Date", "Amount", "Expense Type", "Expense Budget"]
    )
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df["Month"] = df["Date"].dt.strftime("%B-%Y")
    df["Total_exp"] = df.groupby("Month")["Amount"].transform("sum")
    df["Remaining_budget"] = df["Expense Budget"] - df["Total_exp"]
    df.to_csv("expenses_book.txt", sep="|", index=False, header=False)
    # return df
    to_be_retuned = f"""
    Expense Added Successfully!
    Here is current status of your budget:
    Total Expense for {df.iloc[-1]['Month']}: {df.iloc[-1]['Total_exp']}
    Remaining Budget for {df.iloc[-1]['Month']}: {df.iloc[-1]['Remaining_budget']}
    """
    return to_be_retuned

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
add_expenses_func("2025-12-20", 500, "Snacks", 100000)


