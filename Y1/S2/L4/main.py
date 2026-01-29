class AppointmentScheduler:
    def __init__(self):
        self.__appointments = []

    def view_appointments():
        pass

    def edit_appointment():
        pass

    def delete_appointment():
        pass

    def add_attendance():
        pass    

"""Appointment type: Weekly, name: "Weekly Meeting", date: Wednesday, location:  "Room C", 
with members of the appointment: John Doe, Robert Johnson, Emily Davis. - 
Activity #1 Name “Company Party” Date “2024-03-17” Location “Conference Room” 
- Activity #2 Name “Company Visit” Date “2024-03-19” Location “Conference Room”
"""
#Split (,) & 
    
#Sort polymorphism for notification class
class Appointment():
    def __init__(self, name, location, details, date, attendance = None, notification = None):
        self.name = name
        self.location = location
        self.details = details
        self.date = date
        self.attendance = attendance if attendance is not None else []  
        self.notification = notification

    def notification():
        pass
    
class weekly_Meeting(Appointment):
    def __init__(self, name, location, details, date, attendance, time, notification):
        super().__init__(name, location, details, date, attendance, notification)
        if self.notification is None:
            raise ValueError("Require Notification")
        if not self.attendance:
            raise ValueError("Require Attendance")
        self.time = time

class one_time_meeting(Appointment):
    def __init__(self, name, location, details, date, attendance, notification ):
        super().__init__(name, location, details, date, attendance, notification)
        if not self.attendance:
            raise ValueError("Attendance is mandatory")



class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)





    
        
                

app = AppointmentScheduler()

print("# # Test Case 1 : Add Appointment, add activity information, and add appointment information. ")
app.view_appointments()            # Show all Appointments
print()

print("Test Case 2 : Edit Appointment")
app.edit_appointment(title="Team Meeting #1",to="Team B Meeting #1")
app.edit_appointment(location="Room B",to="Room C")
app.view_appointments()            # Show all Appointments
print()

print("Test Case 3 : Delete Appointment using topic “Team Meeting #2”")
app.delete_appointment(title="Team Meeting #2")
app.view_appointments()            # Show all Appointments
print()

print("Test Case 4 : Add Attendance who receives appointments for one-time appointments and weekly appointments")
app.add_attendance("Team B Meeting #1", john)
app.add_attendance("Weekly Meeting", jane)
app.view_appointments()            # Show all Appointments
print()

print("Test Case 5 : Search Attendance Search for individual appointments using the name Robert Johnson")
app.show_person_in_appointment(john)
print()