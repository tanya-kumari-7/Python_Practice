########################## Registration

def registration(name,email,password,registration_date):
    if not name or not email or not password or not registration_date:
        return (f"Registration Details can't be blank")
    else:
        with open('registrationbook.txt','a') as file:
            file.write(f'{name} | {email} | {password}| {registration_date}\n')
        return "Registrion successfuly completed"