from files import get_users
from secretary import add_pet, add_appointment


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
        if choice == 1:
            add_pet()
        elif choice == 2:
            add_appointment()
        elif choice == 0:
            break
        else:
            print("Wrong choice")
    elif role == 'veterinary':
        choice = veterinary_menu()
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 0:
            break
        else:
            print("Wrong choice")
    elif role == 'manager':
        choice = manager_menu()
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            break
        else:
            print("Wrong choice")
    else:
        print("Invalid role")
        break
print("End of Pet-Clinic application")


