
def add_income_details(month,income,incomefrom):
    if not month  or not income  or not incomefrom:
        return ("Fill complete the details: month,income,and incomefrom")
    try:
        with open("monthly_income_book.txt","a") as file:
            file.write(f"{month.strip()} | {income.strip()} | {incomefrom.strip()}\n")
            print("Details Added")
    except Exception as e:
        print("Error found",e)
        
# print(add_income_details("01-04-2025","100000", "salary"))


# Step 1: Read and print content
with open("monthly_income_book.txt", "r") as file:
    content = file.read()
    print(content)

# Step 2: Delete content
# with open("monthly_income_book.txt", "w") as file:
#     pass  # This clears the file



def expenses_book(month,description,amount):
    if not month or not description or not amount:
        return ("Fill complete the details: month,description,and amount")
    with open("expensebook.txt",'a') as file:
        file.write(f'{month.strip()} | {description.strip()} | {amount.strip()}\n')
        print("Expenses Added")
        
print(expenses_book("03-04-2025","21000", "MF investment"))

with open("expensebook.txt", "r") as file:
    content = file.read()
    print(content)


      
        