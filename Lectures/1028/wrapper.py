"""
This module depicts how a wrapper can be used to wrap around an object and add
behaviour to it without the use of inheritance.

A wrapper must fulfill the following 2 conditions:
- Implement the same interface as the object being wrapped.
- Be composed of the object being wrapped. (Have the object being
  wrapped as one of its attributes.)
"""


class Student:
    """
    Represents a student that studies and procrastinates. The student has a
    name, age, a school, happiness and knowledge score. This class
    implements the following interface:
    + study()
    + procrastinate
    + __str__
    """
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
        print("I'm procrastinating")
        self._happiness += 10

    def __str__(self):
        return f"Name:{self._name} Age:{self._age} School:{self._school} " \
               f"Knowlege:{self._knowledge} Happiness:{self._happiness}"


class ProcrastinatingStudentDecorator:
    """
    A wrapper that wraps around a student. Adds additional procrastination
    behaviour to a Student without using inheritance.

    A wrapper implements the same interface as the object being wrapped
    around (wrappee). All implementations of that interface just call
    the corresponding methods in the wrappee.
    """

    def __init__(self, student):
        self.student = student

    def study(self):
        """
        Makes the student procrastinate before making the student study.
        :return: None
        """
        self.procrastinate()
        self.student.study()

    def procrastinate(self):
        self.student.procrastinate()

    def __str__(self):
        return self.student.__str__()


def main():
    """
    Creates the appropriate student based on user input and makes them study.
    :return:
    """
    choice = input("Does the student procrastinate before studying? (Y/N)")
    if choice.lower() == 'y':
        choice = True
    else:
        choice = False

    student = Student("Rahul", 28, "BCIT")
    if choice:
        student = ProcrastinatingStudentDecorator(student)

    student.study()


if __name__ == '__main__':
    main()
