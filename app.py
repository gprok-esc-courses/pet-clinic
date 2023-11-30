import csv

def get_users():
    file = open("staff.csv")
    reader = csv.DictReader(file)
    users = {}
    for row in reader:
        users[row['username']] = row 
    return users 


def login():
    username = input("Username: ")
    password = input("Password: ")
    users = get_users()
    if username in users:
        if password == users[username]['password'] and users[username]['active'] == '1':
            role = users[username]['role']
        else:
            role = None
    else:
        role = None
    return username, role

def secretary_menu():
    print("<<< SECRETARY >>>")
    print("1. Add Pet")
    print("2. Add appointment")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

def veterinary_menu():
    print("<<< VETERINARY >>>")
    print("1. View Pending Appointments")
    print("2. Add Results")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

def manager_menu():
    print("<<< MANAGER >>>")
    print("1. Export Pet History")
    print("2. Treatments on a date")
    print("3. View Staff")
    print("4. Add Staff")
    print("5. Remove Staff")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice


username, role = login()
while True:
    if role == 'secretary':
        choice = secretary_menu()
    elif role == 'veterinary':
        choice = veterinary_menu()
    elif role == 'manager':
        choice = manager_menu()
    else:
        print("Invalid role")
        break
print("End of Pet-Clinic application")


