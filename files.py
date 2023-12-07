import csv

def get_users():
    """
    Reads users from the users.csv file and returns a 
    dictionary with username as the key and a the respective user's
    record as a value.
    """
    file = open("staff.csv")
    reader = csv.DictReader(file)
    users = {}
    for row in reader:
        users[row['username']] = row 
    return users 

def get_pets():
    """
    Reads pets from the pets.csv file and returns a 
    dictionary with id as the key and a the respective pet's
    record as a value.
    """
    file = open("pets.csv")
    reader = csv.DictReader(file)
    pets = {}
    for row in reader:
        pets[row['id']] = row 
    file.close()
    return pets 

def get_appointments():
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    appointments = {}
    for row in reader:
        appointments[row['id']] = row
    file.close()
    return appointments

def get_pet_by_id(pid):
    """
    Finds the pet of the given id and return it. 
    If is not in the file, return None.
    """
    file = open("pets.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] == pid:
            return row 
    file.close()
    return None

def get_appointment_by_id(aid):
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] == aid:
            return row
    return None