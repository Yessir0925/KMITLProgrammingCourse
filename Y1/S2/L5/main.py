class Member:
    def __init__(self, name, email=None, phone_number=None):
        self.name = name
        self.email = email
        self.phone_number = phone_number


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def view_appointments(self):
        for ap in self.appointments:
            print(ap.format_line())
        return self.appointments

    def add_appointment(self, appointment_obj):
        self.appointments.append(appointment_obj)

    def edit_appointment(self, **spargs):
        to_value = spargs.get("to", None)
        if to_value is None:
            return

        field = None
        old_value = None
        for k, v in spargs.items():
            if k != "to":
                field = k
                old_value = v
                break
        if field is None:
            return

        for obj in self.appointments:
            if field == "title":
                if hasattr(obj, "name") and obj.name == old_value:
                    obj.name = to_value
                elif hasattr(obj, "title") and obj.title == old_value:
                    obj.title = to_value

            elif field == "location":
                if getattr(obj, "location", None) == old_value:
                    obj.location = to_value

    def delete_appointment(self, title):
        kept = []
        for obj in self.appointments:
            if hasattr(obj, "name") and obj.name == title:
                continue
            if hasattr(obj, "title") and obj.title == title:
                continue
            kept.append(obj)
        self.appointments = kept

    def add_attendance(self, appointment_title, member):
        for obj in self.appointments:
            if hasattr(obj, "name") and obj.name == appointment_title:
                if not hasattr(obj, "attendance") or obj.attendance is None:
                    obj.attendance = []
                obj.attendance.append(member) 
                return

    def show_person_in_appointment(self, member):
        for obj in self.appointments:
            if hasattr(obj, "attendance") and obj.attendance:
                if any(m.name == member.name for m in obj.attendance):
                    print(obj.format_line())

    def send_notifications(self, appointment_title, message):
        for obj in self.appointments:
            if hasattr(obj, "name") and obj.name == appointment_title:
                for m in obj.attendance:
                    if getattr(m, "phone_number", None):
                        print(f"Sending SMS notification to : {m.phone_number} with message : {message}")
                    else:
                        print(f"Sending email notification to: {m.email} with message : {message}")
                return


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


class Appointment:
    def __init__(self, name, location, details, date, attendance=None, notification=None):
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

    def format_line(self):
        names = ",".join(m.name for m in self.attendance)
        return f"Topic : {self.name} Location : {self.location} on {self.date} Attn: {names}"


class weekly_Meeting(Appointment):
    def __init__(self, name, location, details, date, attendance=None, time=None, notification=None):
        super().__init__(name, location, details, date, attendance, notification)
        if self.notification is None:
            raise ValueError("Require Notification")
        if not self.attendance:
            raise ValueError("Require Attendance")
        self.time = time

    def format_line(self):
        names = ",".join(m.name for m in self.attendance)
        return f"Weekly AP, Topic : {self.name} Location : {self.location} on {self.date} Attn: {names}"


class one_time_meeting(Appointment):
    def __init__(self, name, location, details, date, attendance=None, notification=None):
        super().__init__(name, location, details, date, attendance, notification)
        if not self.attendance:
            raise ValueError("Attendance is mandatory")


class Activity:
    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date

    def format_line(self):
        return f"Activity, Topic : {self.title} Location : {self.location} on {self.date}"