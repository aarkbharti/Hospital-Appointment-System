import csv

filename = "appointments.csv"

while True:
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Date: ")
    time = input("Enter Time: ")

    f = open(filename, "a")
    writer = csv.writer(f)
    writer.writerow([name, age, phone, doctor, date, time])
    f.close()

    print("Appointment saved")

    again = input("Do you want to add another? (yes/no): ")
    if again != "yes":
        break
