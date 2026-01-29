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

class Notification:
    def send(self, message):
        raise NotImplementedError("Subclass must implement send()")
    
class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"[EMAIL] {message}")

class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"[SMS] {message}")

class Appointment():
    def __init__(self, name, location, details, date, attendance = None, notification = None):
        self.name = name
        self.location = location
        self.details = details
        self.date = date
        self.attendance = attendance if attendance is not None else []  
        self.notification = notification

    def notify(self, message):
        if self.notification is None:
            raise ValueError("No notification set")
        self.notification.send(message)

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