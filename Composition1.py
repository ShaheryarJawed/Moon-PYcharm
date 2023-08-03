class Author:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display_info(self):

        return f"Author: {self.name}, Nationality: {self.nationality}"


class Book:


    def __init__(self, title, author, year):

        self.title = title
        self.author = author
        self.year = year

    def display_info(self):

        return f"Title: {self.title}, {self.author.display_info()}, Year: {self.year}"

author1 = Author("James Hilton", "British")
book1 = Book("GoodBye Mr Chips", author1, 1934)
print(book1.display_info())

