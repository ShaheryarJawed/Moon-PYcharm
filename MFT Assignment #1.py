"""Author:Shaheryar Jawed"""

class Car:
    """
    A class representing a car.

    Attributes:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year the car was made.
        speed (int): The current speed of the car in km/h.
    """

    def __init__(self, make, model, year):
        """
        Constructs a new Car object.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The year the car was made.
        """
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        """
        Increases the speed of the car by the given amount.

        Args:
            amount (int): The amount by which to increase the speed.
        """
        self.speed += amount

    def brake(self, amount):
        """
        Decreases the speed of the car by the given amount.

        Args:
            amount (int): The amount by which to decrease the speed.
        """
        self.speed -= amount

    def get_speed(self):
        """
        Returns the current speed of the car.
        """
        return self.speed


class Person:
    """
    A class representing a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person.
    """

    def __init__(self, name, age, gender):
        """
        Constructs a new Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        """
        Prints a greeting to the console.
        """
        print(f"Hello, my name is {self.name}.")

    def get_gender(self):
        """
        Returns the gender of the person.
        """
        return self.gender


def main():
    """
    Creates objects and passes messages.
    """
    # Create a Car object
    car = Car("Toyota", "Cultus", 2021)

    # Create a Person object
    person = Person("Shaheryar", 19, "Male")

    # Accelerate the car
    car.accelerate(50)

    # Print the current speed of the car
    print(f"The car is currently going {car.get_speed()} km/h.")

    # Greet the person
    person.greet()

    # Get the gender of the person
    gender = person.get_gender()

    # Print the gender of the person
    print(f"My gender is {gender}.")


if __name__ == '__main__':
    main()
