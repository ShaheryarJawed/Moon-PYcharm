"""
Author : Shaheryar Jawed
"""
"""
Date : 23/2/2023
"""

class Person:
    """
        A class representing a person.

        Attributes:
            name (str): The name of the person.
            age (int): The age of the person.
        """


    def __init__(self, name, age):
        """
                Initializes a person with a name and age.
                """

        self.name = name
        self.age = age
    def greet(self):
        """
               Greets the person with their name.
               """

        print("Hello, my name is", self.name)

class Student(Person):
    """
        A class representing a student.

        Attributes:
            major (str): The major of the student.
            fee (int): The fee of the student.
            sub_1 (int): The marks obtained by the student in subject 1.
            sub_2 (int): The marks obtained by the student in subject 2.
            sub_3 (int): The marks obtained by the student in subject 3.
        """


    def __init__(self, name, age, major, fee, sub_1_marks, sub_2_marks, sub_3_marks):
        """
                Initializes a student with a name, age, major, fee and subject marks.
                """

        super().__init__(name, age)
        self.major = major
        self.__fee = fee
        self.sub_1 = sub_1_marks
        self.sub_2 = sub_2_marks
        self.sub_3 = sub_3_marks

    def total_marks(self):
        """
               Calculates and prints the total marks obtained by the student.
               """

        print(f'The total marks of {self.name} is {self.sub_1 + self.sub_2 + self.sub_3}')

    def study(self):
        """
               Prints what the student is studying.
               """

        print("I am studying", self.major)

    @property
    def get_fee(self):
        """
               Gets the fee of the student.
               """

        print(f"The fee of the student is {self.__fee}")
        return self.__fee

    @get_fee.setter
    def set_fee(self, fee):
        """
               Sets the fee of the student.
               """

        print(f"The fee of the student is now {fee}")
        self.__fee = fee

        """
        Using the display method to show the student's information
        """

    def display(self):
        """
               Displays the student's information.
               """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"Fee: {self.__fee}")
        print(f"Sub_1 marks: {self.sub_1}")
        print(f"Sub_2 marks: {self.sub_2}")
        print(f"Sub_3 marks: {self.sub_3}")

x = Student("Shaheryar", 19, "Computer Science", 50000, 75, 80, 90)

# Call the display() method to show the student's information
x.display()

# Get the current value of fee using the getter
x.get_fee

# Set a new value for fee using the setter
x.set_fee = 100000

# Get the new value of fee using the getter
x.get_fee

x.total_marks()

# Call the display() method again to show the updated student's information
x.display()
