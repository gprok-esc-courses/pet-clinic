from files import get_pets

def add_pet():
    name = input("Give name: ")
    species = input("Give Species: ")
    breed = input("Give breed: ")
    year = input("Give birth year: ")
    pets = get_pets()
    new_id = len(pets) + 1
    file = open('pets.csv', 'a')
    file.write(str(new_id)+','+name+','+species+','+breed+','+year+'\n')
