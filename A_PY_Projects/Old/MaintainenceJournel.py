## Create a Maintenance Journal Entry
from datetime import datetime


def create_maintenance_journal_entry(category, description, amount, added_on=None):
    if not category or not description or not amount:
        print("All fields are required to add a task.")
        return
    
    if added_on is None:
        added_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("maintenance_journal.txt", "a") as file:
        entry = f"{category} | {description} | {amount} |{added_on}\n"
        file.write(entry)
    print("Maintenance journal entry added successfully.")



# Example call
#create_maintenance_journal_entry("Shopping", "Home Exp", 6000,"2025-09-28")

# # Read the maintenance journal entries
# with open("maintenance_journal.txt", "r") as file:
#     print(file.read())

def read_maintenance_journal():
    try:
        with open("maintenance_journal.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("No maintenance journal entries found.")
            else:
                print("Maintenance Journal Entries:")
                for i, entry in enumerate(entries, start=1):
                    print(f"{i}. {entry.strip()}")
    except FileNotFoundError:
        print("Maintenance journal file not found. Add an entry first.")


def get_monthly_exp():
    monthly_exp = {}
    with open("maintenance_journal.txt", "r") as file:
        data = file.readlines()
        if not data:
            print("Data Not Found")
            return
        else:
            for i, content in enumerate(data, start=1):
                category, description, amount, added_on = content.strip().split("|")
                dt = datetime.strptime(added_on.strip(), "%Y-%m-%d %H:%M:%S") if " " in added_on else datetime.strptime(added_on.strip(), "%Y-%m-%d")
                added_on_formatted = dt.strftime("%d-%m-%Y")
                month = dt.strftime("%Y-%m")
                amount = int(amount.strip())
                if month in monthly_exp:
                    monthly_exp[month] += amount
                else:
                    monthly_exp[month] = amount
        return monthly_exp


def get_exp_by_category():
    with open("maintenance_journal.txt", "r") as file:
        exp_by_category = {}
        data = file.readlines()
        if not data:
            print("No Data Found")
            return
        else:
            for i , content in enumerate(data ,start=1):
                category, description, amount, added_on = content.strip().split("|")
                exp_amount = int(amount)
                if category in exp_by_category:
                    exp_by_category[category] += exp_amount
                else:
                    exp_by_category[category] = exp_amount
                continue
        return exp_by_category
    
def get_monthly_exp_by_category():
    monthly_exp_by_category = {}
    with open ("maintenance_journal.txt", "r") as file:
        data = file.readlines()
        if not data:
            print("Data Not found")
            return
        else:
            for i , content in enumerate(data,start=1):
                category, description, amount, added_on = content.strip().split("|")
                dt = datetime.strptime(added_on.strip(), "%Y-%m-%d %H:%M:%S") if " " in added_on else datetime.strptime(added_on.strip(), "%Y-%m-%d")
                added_on_formatted = dt.strftime("%d-%m-%Y")
                month = dt.strftime("%Y-%m")
                amount = int(amount.strip())
                category = category.strip()

                key = (month,category)

                if key in monthly_exp_by_category:
                    monthly_exp_by_category[key] += amount
                else:
                    monthly_exp_by_category[key] = amount
                continue
        return monthly_exp_by_category
    
# def delete_data_from_txt_file():
#     with open("maintenance_journal.txt", "w") as file:
#         file.write("")



        
################ Create a menu
1
    

   






