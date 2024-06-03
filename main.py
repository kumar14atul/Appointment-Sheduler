from datetime import datetime

class Appointment:
    def __init__(self, patient_name, doctor_name, date_time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date_time = date_time

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient_name, doctor_name, date_time):
        new_appointment = Appointment(patient_name, doctor_name, date_time)
        self.appointments.append(new_appointment)
        print("Appointment scheduled successfully!")

    def list_appointments(self):
        if self.appointments:
            print("Scheduled Appointments:")
            for i, appointment in enumerate(self.appointments, 1):
                print(f"{i}. Patient: {appointment.patient_name}, Doctor: {appointment.doctor_name}, Date & Time: {appointment.date_time}")
        else:
            print("No appointments scheduled yet.")

scheduler = AppointmentScheduler()

def book_appointment():
    print("Book Appointment")
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    try:
        date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        scheduler.schedule_appointment(patient_name, doctor_name, date_time)
    except ValueError:
        print("Invalid date and time format. Please enter in YYYY-MM-DD HH:MM format.")

def list_appointments():
    scheduler.list_appointments()

def menu():
    print("\nMenu:")
    print("1. Book Appointment")
    print("2. List Appointments")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        book_appointment()
    elif choice == "2":
        list_appointments()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose again.")
