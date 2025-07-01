########################## Registration

def registration(name,email,password,registration_date):
    if not name or not email or not password or not registration_date:
        return (f"Registration Details can't be blank")
    else:
        with open('registrationbook.txt','a') as file:
            file.write(f'{name} | {email} | {password}| {registration_date}\n')
        return "Registrion successfuly completed"
    
def read_registration_book():
    try:
        with open("registrationbook",'r') as file:
            user_details = file.readlines()
            if not user_details:
                return (f' User details not Found')
            for i,line in enumerate(user_details,start=1):
                name,email,password,registration_date = line.strip().split("|")
                return (f'{i}. name: {name}, email: {email}, password: {password}, registration_date:{registration_date}')
    except Exception as r:
        print(f'File not found, got error as {r}')
        