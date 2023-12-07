from files import get_appointments, get_appointment_by_id
import shutil
import os

def print_open_appointments():
    appointements = get_appointments()
    for key in appointements:
        if appointements[key]['completed'] == '0':
            print(key, appointements[key]['date'],
                  appointements[key]['time'], 
                  appointements[key]['reason'])
            
def add_result():
    aid = input("Give appointment ID: ")
    appointment = get_appointment_by_id(aid)
    if appointment is None:
        print("Appointment not found.")
    else:
        result = input("Give result: ")
        temp_file = open("temp_appointments.csv", "w")
        appointments = get_appointments()
        temp_file.write("id,pet_id,date,time,reason,completed,result\n")
        for key in appointments:
            if key == aid:
                temp_file.write(key+','+appointments[key]['pet_id']+','
                                +appointments[key]['date']+','
                                +appointments[key]['time']+','
                                +appointments[key]['reason']+','
                                +'1,'+result+'\n')
            else: 
                temp_file.write(key+','+appointments[key]['pet_id']+','
                                +appointments[key]['date']+','
                                +appointments[key]['time']+','
                                +appointments[key]['reason']+','
                                +appointments[key]['completed']+','
                                +appointments[key]['result']+'\n')
        temp_file.close()
        shutil.copyfile("temp_appointments.csv", "appointments.csv")
        os.remove("temp_appointments.csv")
