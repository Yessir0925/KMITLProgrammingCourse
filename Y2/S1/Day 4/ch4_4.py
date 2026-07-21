"""A company's cafeteria has staff who organize the queue for buying food based on the 
department of each employee. The rule is that if an employee from a department joins
the queue and there are already other employees from the same department in the 
queue, they will be inserted behind the last employee of the same department. 
For example:

Front | 1 2 2 2 2 3 3 3 | Rear If an employee from department 1 joins the queue, 
it will become: Front | 1 1 2 2 2 2 3 3 3 | Rear
Input:

The input is divided into two parts separated by a /. The left side contains 
the department and ID of each employee, while the right side contains the operations, 
either D or E <id>.

    E <id>: Adds the employee to the queue.
    D: Removes the first employee from the queue and displays their ID. If the 
queue is empty, it displays "Empty".

Example TestCase_1:

    There are 4 employees: department 1 with IDs 101 and 102, and department 2 with IDs 201 and 202.
    The output shows "Empty" because there are no employees in the queue initially.
    Employees with IDs 101 and 201 are added to the queue in that order.
    The output shows 101 because employee 101 is at the front of the queue, followed by 201 
as they are now the first in the queue.

Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
Empty
101
201
"""

inp = input("Enter Input : ")
employees, commands = inp.split("/")

emp_to_dept = {}
for item in employees.split(","):
    dept, emp = map(int, item.split())
    emp_to_dept[emp] = dept

dept_queue = []
member_queue = {}

for cmd in commands.split(","):
    if cmd == "D":
        if len(dept_queue) == 0:
            print("Empty")
        else:
            dept = dept_queue[0]
            emp = member_queue[dept].pop(0)
            print(emp)
            if len(member_queue[dept]) == 0:
                dept_queue.pop(0)
                del member_queue[dept]
    else:
        _, emp = cmd.split()
        emp = int(emp)
        dept = emp_to_dept[emp]
        if dept not in member_queue:
            member_queue[dept] = []
            dept_queue.append(dept)
        member_queue[dept].append(emp)