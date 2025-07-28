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
    
    print("✅ Maintenance journal entry added successfully.")




# Example call
# create_maintenance_journal_entry("Plumbing", "Fixed leaky faucet", 50)

# Read the maintenance journal entries
# with open("maintenance_journal.txt", "r") as file:
#     print(file.read())

