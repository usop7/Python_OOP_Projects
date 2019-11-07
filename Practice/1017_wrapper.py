class Student:
    def __init__(self, name, age, school):
        self._name = name
        self._age = age
        self._school = school
        self._knowledge = 0
        self._happiness = 100

    def study(self):
        print("I'm studying!")
        self._knowledge += 10
        self._happiness -= 5

    def procrastinate(self):
        print("I'm procrastinating.")
        self._happiness += 10

    def __str__(self):
        return f"Name:{self._name} Age:{self._age} School:{self._school} " \
               f"Knowledge:{self._knowledge} Happiness:{self._happiness}"


class ProcrastinatingStudentDecorator:

    def __init__(self, student):
        self.student = student

    def study(self):
        self.student.procrastinate()
        self.student.study()

    def procrastinate(self):
        self.student.procrastinate()

    def __str__(self):
        return self.student.__str__()


def main():
    choice = input("Does the student procrastinate before studying? (Y/N): ")
    if choice.lower() == 'y':
        choice = True
    else:
        choice = False

    student = Student("Rahul", 28, "BCIT")

    if choice:
        student = ProcrastinatingStudentDecorator(student)

    student.study()
    print(student)


if __name__ == "__main__":
    main()
