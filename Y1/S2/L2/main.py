class enrollment:
    def __init__(self, student, subject):
        self.student = student
        self.subject = subject
        self.grade = None


class subject:
    def __init__(self, subject_name, subject_id):
        self.subject_name = subject_name
        self.subject_id = subject_id
        self.teacher = None
        self.enrollment = []

    def IsEnrolled(self, student):
        for i in range(len(self.enrollment)):
            if self.enrollment[i].student == student:
                return i
        return -1

    def AddEnrollmentSubject(self, student):
        e = enrollment(student, self)
        if self.IsEnrolled(student) != -1:  
            print(f"{student.student_name} Already enrolled")
            return
        self.enrollment.append(e)
        student.enrollment.append(e)
        print(f"{student} Done")

    def RemoveEnrollmentSubject(self, student):
        idx = self.IsEnrolled(student)
        if idx == -1:
            return
        self.enrollment.pop(idx)
        for i in range(len(student.enrollment)):
            e = student.enrollment[i]
            if e.student == student and e.subject == self:
                student.enrollment.pop(i)
                return

    def AddTeacher(self, teacher):
        self.teacher = teacher
        teacher.teaching_list.append(self)

class student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.enrollment = []

    def AddEnrollmentStudent(self, subject):
        subject.AddEnrollmentSubject(self)

    def DisplayStat(self, subject):
        for e in self.enrollment:
            if e.subject == subject:
                print(f"Name = {self.student_name}")
                print(f"ID = {self.student_id}")
                print(f"{subject.subject_name} = '{e.grade}'")

class teacher:
    def __init__(self, teacher_name, teacher_id):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.teaching_list = []

    def Set_Grade(self, subject, student, grade):
        if subject not in self.teaching_list:
            print(f"{self.teacher_name} - Not Teacher in System")
            return
        for e in subject.enrollment:
            if e.student == student:
                e.grade = grade



Leslie = teacher('Leslie', 10110)
John = teacher('John', 3232)
Mook = teacher('Mook', 4921)

Ethan = student('Ethan', 68012008)
Daniel = student('Daniel', 68016767)
Pat = student('Pat', 68012308)
IOun = student('IOun', 68011384)
Maple = student('Maple', 68013973)
Anda = student('Anda', 68012983)
Tawan = student('Tawan', 68010000)
Bright = student('Bright', 68012398)
Win = student('Win', 68017812)
Josh = student('Josh', 68012084)
Saaw = student('Saaw', 68016969)


Chinese = subject('Chinese', 420)   
Math = subject('Math', 117)
Programming = subject('Programming', 670)


Ethan.AddEnrollmentStudent(Chinese) # - Add Student to Class
Daniel.AddEnrollmentStudent(Chinese)
Ethan.AddEnrollmentStudent(Chinese)
Chinese.AddTeacher(Leslie) # - Add Teacher

Leslie.Set_Grade(Chinese, Ethan, "A") # - Assign Grade
John.Set_Grade(Chinese, Daniel, "C") # - Error Check
Leslie.Set_Grade(Chinese, Daniel, "A")

Ethan.DisplayStat(Chinese)
print()
Daniel.DisplayStat(Chinese)