import csv

def get_users():
    file = open("staff.csv")
    reader = csv.DictReader(file)
    users = {}
    for row in reader:
        users[row['username']] = row 
    return users 

def get_pets():
    file = open("pets.csv")
    reader = csv.DictReader(file)
    pets = {}
    for row in reader:
        pets[row['id']] = row 
    return pets 