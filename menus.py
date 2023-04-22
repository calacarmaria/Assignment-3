from teacher import Teacher
from grade import Grade

teachers = []
students = []

def deleteTeachers():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()
def deleteStudents():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()
def deleteAll():
    global teachers, students
    teachers = []
    students = []
    print('All records have been deleted.')
    menu()
def addTeachers():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        department = input('Enter department: ')
        position = input('Enter position: ')

        tc = Teacher(id, lastName, firstName, middleName, type, department, position)

        teachers.append(tc)

        print()
        a = input('Enter another? [y/n]: ')
        ans = a.lower()
        if (ans != 'y'):
            break

    menu()
def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        history = input('Grade history: ')
        architecture = input('Grade architecture: ')
        network = input('Grade network: ')
        communication = input('Grade communication: ')

        stud = Grade(history, architecture, network, communication)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()
def searchStudent():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    menu()
def searchTeacher():
    i = int(input('Enter index: '))
    print(f'{i} \t {teachers[i].getName()} \t | {teachers[i].getDepartment()} \t | {teachers[i].getPosition()}')

    menu()

def displayStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()
def displayTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()
def displayAll():
    print()
    print('-------------------------------------------------------------------------------')
    print('Students:')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    print('Teachers:')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def menu():
    print()
    print()
    print('::Menu::')
    print('D - delete student          T - delete teacher')
    print('A - add student             R - add teacher')
    print('S - search student          H - search teacher')
    print('U - display student         E - display teacher')
    print('L - display all             I - delete all')
    print()

    c = input('Enter a function: ')
    choice = c.upper()
    if choice == 'D':
        deleteStudents()
    elif choice == 'A':
        addStudents()
    elif choice == 'S':
        searchStudent()
    elif choice == 'U':
        displayStudent()
    elif choice == 'T':
        deleteTeachers()
    elif choice == 'R':
        addTeachers()
    elif choice == 'H':
        searchTeacher()
    elif choice == 'E':
        displayTeacher()
    elif choice == 'L':
        displayAll()
    elif choice == 'I':
        deleteAll()
    print()

menu()