from files import get_pet_by_id, get_appointments

def export_pet():
    pid = input("Give pet ID: ")
    pet = get_pet_by_id(pid)
    if pet is None:
        print("Pet not found.")
    else:
        file = open("pet" + pid + ".txt", "w")
        file.write("PET REPORT\n")
        # write the basic pet's data
        file.write("Name: " + pet['name'] + '\n')
        file.write("Specie: " + pet['species'] + '\n')
        file.write("Breed: " + pet['breed'] + '\n')
        file.write("Year: " + pet['year'] + '\n')
        file.write("=================================\n")
        file.write("TREATMENTS\n")
        appointments = get_appointments()
        for key in appointments:
            if appointments[key]['pet_id'] == pid and appointments[key]['completed'] == '1':
                file.write(appointments[key]['date'] + ", " +
                           appointments[key]['reason'] + ", " +
                           appointments[key]['result'] + '\n')
        file.close()

def day_treatments():
    d = input("Give date (yyyy-mm-dd): ")
    appointments = get_appointments()
    for key in appointments:
        if appointments[key]['date'] == d:
            print(appointments[key])
            
