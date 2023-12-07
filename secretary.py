from files import get_pets, get_pet_by_id, get_appointments

def add_pet():
    """
    Gets pet data from the user, generated the next id,
    based on the size of the pets file, and then appends
    the new pet to the pets.csv
    """
    name = input("Give name: ")
    species = input("Give Species: ")
    breed = input("Give breed: ")
    year = input("Give birth year: ")
    pets = get_pets()
    new_id = len(pets) + 1
    file = open('pets.csv', 'a')
    file.write(str(new_id)+','+name+','+species+','
               +breed+','+year+'\n')
    file.close()

def add_appointment():
    """
    Adds a new appointment for a pet. Includes the date, time, 
    and reason. 
    """
    pet_id = input("Give pet id: ")
    pet = get_pet_by_id(pet_id)
    if pet is None:
        print("Pet not found, try again.")
    else:
        app_date = input("Give date (yyyy-mm-dd): ")
        app_time = input("Give time (hh:mm): ")
        reason = input("Give reason: ")
        appointments = get_appointments()
        id = len(appointments) + 1
        file = open("appointments.csv", "a")
        file.write(str(id)+','+pet_id+','+app_date+','
                   +app_time+','+reason+',0,-\n')
        file.close()

