from person import Person


class Teacher(Person):
    def __init__(self, id, last_name, first_name, middle_name, type, department, position) -> None:
        self.department = department
        self.position = position

        Person.__init__(self, id, last_name, first_name, middle_name, type)

    def __str__(self) -> str:
        return super().__str__()

    def getDepartment(self):
        return self.department

    def getPosition(self):
        return self.position