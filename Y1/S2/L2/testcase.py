class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name


class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.credit = credit
        self.teacher = None

    def assign_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            return "Error"
        self.teacher = teacher
        return "Done"


class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name


class Enrollment:
    def __init__(self, student, subject):
        self.student = student
        self.subject = subject
        self.grade = None


student_list = []
subject_list = []
teacher_list = []
enrollment_list = []


# TODO 1
def search_subject_by_id(subject_id):
    for s in subject_list:
        if s.subject_id == subject_id:
            return s
    return None


# TODO 2
def search_student_by_id(student_id):
    for s in student_list:
        if s.student_id == student_id:
            return s
    return None


# TODO 5 (helper used by others)
def search_enrollment_subject_student(subject, student):
    if not isinstance(subject, Subject) or not isinstance(student, Student):
        return "Error"
    for e in enrollment_list:
        if e.subject == subject and e.student == student:
            return e
    return "Not Found"


# TODO 3
def enroll_to_subject(student, subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    found = search_enrollment_subject_student(subject, student)
    if isinstance(found, Enrollment):
        return "Already Enrolled"
    enrollment_list.append(Enrollment(student, subject))
    return "Done"


# TODO 4
def drop_from_subject(student, subject):
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    for i in range(len(enrollment_list)):
        e = enrollment_list[i]
        if e.student == student and e.subject == subject:
            enrollment_list.pop(i)
            return "Done"
    return "Not Found"


# TODO 6
def search_student_enroll_in_subject(subject):
    if not isinstance(subject, Subject):
        return "Error"
    result = []
    for e in enrollment_list:
        if e.subject == subject:
            result.append(e)
    return result


# TODO 7
def search_subject_that_student_enrolled(student):
    if not isinstance(student, Student):
        return "Error"
    result = []
    for e in enrollment_list:
        if e.student == student:
            result.append(e)
    return result


# TODO 8
def assign_grade(student, subject, grade):
    if not isinstance(student, Student) or not isinstance(subject, Subject) or not isinstance(grade, str):
        return "Error"
    grade = grade.upper().strip()
    if grade not in ["A", "B", "C", "D", "F"]:
        return "Error"

    enroll = search_enrollment_subject_student(subject, student)
    if enroll == "Error":
        return "Error"
    if enroll == "Not Found":
        return "Not Found"

    if enroll.grade is not None:
        return "Error"   # already has grade

    enroll.grade = grade
    return "Done"


# TODO 9
def get_teacher_teach(subject_search):
    if not isinstance(subject_search, Subject):
        return "Error"
    if subject_search.teacher is None:
        return "Not Found"
    return subject_search.teacher


# TODO 10
def get_no_of_student_enrolled(subject):
    if not isinstance(subject, Subject):
        return "Error"
    count = 0
    for e in enrollment_list:
        if e.subject == subject:
            count += 1
    return count


# TODO 11 (output dict allowed)
def get_student_record(student):
    if not isinstance(student, Student):
        return "Error"
    record = {}
    for e in enrollment_list:
        if e.student == student and e.grade is not None:
            record[e.subject.subject_id] = [e.subject.subject_name, e.grade]
    return record


def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)


# TODO 12
def get_student_GPS(student):
    rec = get_student_record(student)
    if rec == "Error":
        return "Error"
    if len(rec) == 0:
        return 0.0

    total = 0
    n = 0
    for subject_id in rec:
        grade = rec[subject_id][1]
        total += grade_to_count(grade)
        n += 1
    return total / n
    
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    enrolls = search_student_enroll_in_subject(subject)
    student_dict = {}
    for e in enrolls:
        student_dict[e.student.student_id] = e.student.student_name
    return student_dict


def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    enrolls = search_subject_that_student_enrolled(student)
    subject_dict = {}
    for e in enrolls:
        subject_dict[e.subject.subject_id] = e.subject.subject_name
    return subject_dict

# -------------------------
# CREATE INSTANCES
# -------------------------
student_list.append(Student('66010001', "Keanu Welsh"))
student_list.append(Student('66010002', "Khadijah Burton"))
student_list.append(Student('66010003', "Jean Caldwell"))
student_list.append(Student('66010004', "Jayden Mccall"))
student_list.append(Student('66010005', "Owain Johnston"))
student_list.append(Student('66010006', "Isra Cabrera"))
student_list.append(Student('66010007', "Frances Haynes"))
student_list.append(Student('66010008', "Steven Moore"))
student_list.append(Student('66010009', "Zoe Juarez"))
student_list.append(Student('66010010', "Sebastien Golden"))

subject_list.append(Subject('CS101', "Computer Programming 1", 3))
subject_list.append(Subject('CS102', "Computer Programming 2", 3))
subject_list.append(Subject('CS103', "Data Structure", 3))

teacher_list.append(Teacher('T001', "Mr. Welsh"))
teacher_list.append(Teacher('T002', "Mr. Burton"))
teacher_list.append(Teacher('T003', "Mr. Smith"))

subject_list[0].assign_teacher(teacher_list[0])
subject_list[1].assign_teacher(teacher_list[1])
subject_list[2].assign_teacher(teacher_list[2])

# -------------------------
# REGISTER STUDENTS
# -------------------------
enroll_to_subject(student_list[0], subject_list[0])
enroll_to_subject(student_list[0], subject_list[1])
enroll_to_subject(student_list[0], subject_list[2])
enroll_to_subject(student_list[1], subject_list[0])
enroll_to_subject(student_list[1], subject_list[1])
enroll_to_subject(student_list[1], subject_list[2])
enroll_to_subject(student_list[2], subject_list[0])
enroll_to_subject(student_list[2], subject_list[1])
enroll_to_subject(student_list[2], subject_list[2])
enroll_to_subject(student_list[3], subject_list[0])
enroll_to_subject(student_list[3], subject_list[1])
enroll_to_subject(student_list[4], subject_list[0])
enroll_to_subject(student_list[4], subject_list[2])
enroll_to_subject(student_list[5], subject_list[1])
enroll_to_subject(student_list[5], subject_list[2])
enroll_to_subject(student_list[6], subject_list[0])
enroll_to_subject(student_list[7], subject_list[1])
enroll_to_subject(student_list[8], subject_list[2])

#===================================================

# =========================
# TEST CASES (TRUE / FALSE)
# =========================

# Test Case #1
expected_1 = {
    '66010001': 'Keanu Welsh',
    '66010002': 'Khadijah Burton',
    '66010003': 'Jean Caldwell',
    '66010004': 'Jayden Mccall',
    '66010005': 'Owain Johnston',
    '66010007': 'Frances Haynes'
}
print("Test Case #1 :", list_student_enrolled_in_subject('CS101') == expected_1)


# Test Case #2
print("Test Case #2 :", enroll_to_subject('66010001', 'CS101') == "Error")


# Test Case #3
print("Test Case #3 :", enroll_to_subject(student_list[0], subject_list[0]) == "Already Enrolled")


# Test Case #4
print("Test Case #4 :", drop_from_subject('66010001', 'CS101') == "Error")


# Test Case #5
print("Test Case #5 :", drop_from_subject(student_list[8], subject_list[0]) == "Not Found")


# Test Case #6
drop_from_subject(student_list[0], subject_list[0])
expected_6 = {
    '66010002': 'Khadijah Burton',
    '66010003': 'Jean Caldwell',
    '66010004': 'Jayden Mccall',
    '66010005': 'Owain Johnston',
    '66010007': 'Frances Haynes'
}
print("Test Case #6 :", list_student_enrolled_in_subject(subject_list[0].subject_id) == expected_6)


# Test Case #7
expected_7 = ['66010002','66010003','66010004','66010005','66010007']
lst = search_student_enroll_in_subject(subject_list[0])
print("Test Case #7 :", [e.student.student_id for e in lst] == expected_7)


# Test Case #8
print("Test Case #8 :", get_no_of_student_enrolled(subject_list[0]) == 5)


# Test Case #9
expected_9 = ['CS102','CS103']
lst = search_subject_that_student_enrolled(student_list[0])
print("Test Case #9 :", [e.subject.subject_id for e in lst] == expected_9)


# Test Case #10
print("Test Case #10 :", get_teacher_teach(subject_list[0]).teacher_name == "Mr. Welsh")


# Test Case #11
enroll = search_enrollment_subject_student(subject_list[0], student_list[1])
print("Test Case #11 :", enroll.subject.subject_id == "CS101" and enroll.student.student_id == "66010002")


# Test Case #12
assign_grade(student_list[1], subject_list[0], 'A')
assign_grade(student_list[1], subject_list[1], 'B')
print("Test Case #12 :", assign_grade(student_list[1], subject_list[2], 'C') == "Done")


# Test Case #13
expected_13 = {
    'CS101': ['Computer Programming 1', 'A'],
    'CS102': ['Computer Programming 2', 'B'],
    'CS103': ['Data Structure', 'C']
}
print("Test Case #13 :", get_student_record(student_list[1]) == expected_13)


# Test Case #14
print("Test Case #14 :", get_student_GPS(student_list[1]) == 3.0)