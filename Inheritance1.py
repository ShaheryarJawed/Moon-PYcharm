class Air():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_air(self):
        print("My name is moon")


class Bir(Air):
    def __init__(self, name, age, game):
        super().__init__(name, age)
        self.game = game

    def display_bir(self):
        print("My age is 19")


obj1 = Air("Moon",19)
obj2= Bir("Umer", 20, "COD")
print(obj2.name)
print(obj2.game)
print(obj1.name)
print(obj1.age)