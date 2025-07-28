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

def read_maintenance_journal():
    try:
        with open("maintenance_journal.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("📭 No maintenance journal entries found.")
            else:
                print("📝 Maintenance Journal Entries:")
                for i, entry in enumerate(entries, start=1):
                    print(f"{i}. {entry.strip()}")
    except FileNotFoundError:
        print("⚠️ Maintenance journal file not found. Add an entry first.")


# read = read_maintenance_journal()
# print(read)