from main import *

app = AppointmentScheduler()

# Members
john = Member("John Doe", "john.doe@example.com")
jane = Member("Jane Smith", "jane.smith@example.com")
robert = Member("Robert Johnson", "robert.johnson@example.com", "08-1234-5678")
emily = Member("Emily Davis", "emily.davis@example.com", "08-3456-7890")

# Test Case 1 setup
app.add_appointment(one_time_meeting("Team Meeting #1", "Room A", "", "2024-03-15", [jane, john, emily]))
app.add_appointment(one_time_meeting("Team Meeting #2", "Room B", "", "2024-03-17", [jane, john, emily]))
app.add_appointment(weekly_Meeting("Weekly Meeting", "Room C", "", "Wednesday", [john, robert, emily],
                                   notification=EmailNotification("dummy@example.com")))
app.add_appointment(Activity("Company Party", "Conference Room", "2024-03-17"))
app.add_appointment(Activity("Company Visit", "Conference Room", "2024-03-17"))

print("# # Test Case 1 : Add Appointment, add activity information, and add appointment information. ")
app.view_appointments()
print()

print("Test Case 2 : Edit Appointment")
app.edit_appointment(title="Team Meeting #1", to="Team B Meeting #1")
app.edit_appointment(location="Room B", to="Room C")
app.view_appointments()
print()

print("Test Case 3 : Delete Appointment using topic “Team Meeting #2”")
app.delete_appointment(title="Team Meeting #2")
app.view_appointments()
print()

print("Test Case 4 : Add Attendance who receives appointments for one-time appointments and weekly appointments")
app.add_attendance("Team B Meeting #1", john)
app.add_attendance("Weekly Meeting", jane)
app.view_appointments()
print()

print('Test Case 5 : Search Attendance Search for individual appointments using the name Robert Johnson')
app.show_person_in_appointment(robert)
print()

print('Test Case 6 : Notify by using the appointment “Team B Meeting #1"')
app.send_notifications("Team B Meeting #1", "invite for meeting")