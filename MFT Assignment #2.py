class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def __init__(self, name, age, major,fee,sub_1_marks,sub_2_marks,sub_3_marks):
        super().__init__(name, age)
        self.major = major
        self.__fee = fee
        self.sub_1 = sub_1_marks
        self.sub_2 = sub_2_marks
        self.sub_3 = sub_3_marks

    def total_marks(self):
        print (f'The total marks of {self.name} is {self.sub_1 + self.sub_2 + self.sub_3} ')



    def study(self):
        print("I am studying", self.major)

# Getter for fee
    def get_fee(self):
        return self.__fee

        # Setter for fee

    def set_fee(self, fee):
        self.__fee = fee

x = Student("Shaheryar", 19, "Computer Science",50000,75,80,90)

# Get the current value of fee using the getter
print(x.get_fee())

# Set a new value for fee using the setter
x.set_fee(55000)

# Get the new value of fee using the getter
print(x.get_fee())

x.total_marks()


