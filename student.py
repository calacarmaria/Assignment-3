from person import Person


class Student(Person):
    def __init__(self, id, last_name, first_name, middle_name, type, year, course, section) -> None:
        self.year = year
        self.course = course
        self.section = section

        Person.__init__(self, id, last_name, first_name, middle_name, type)
        # super(self).__init__(self, id, last_name, first_name, middle_name, type)

    def __str__(self) -> str:
        return super().__str__()

    def getYrCourseSec(self):
        return f'{self.year}/{self.course}/{self.section}'