
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