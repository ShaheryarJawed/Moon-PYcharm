class Author:
    """
    Represents an author with a name and nationality.

    Attributes:
        name (str): The name of the author.
        nationality (str): The nationality of the author.
    """

    def __init__(self, name, nationality):
        """
        Initialize the Author object.

        Args:
            name (str): The name of the author.
            nationality (str): The nationality of the author.
        """
        self.name = name
        self.nationality = nationality

    def display_info(self):
        """
        Display information about the author.

        Returns:
            str: A formatted string containing the name and nationality of the author.
        """
        return f"Author: {self.name}, Nationality: {self.nationality}"


class Book:
    """
    Represents a book with a title, author, and publication year.

    Attributes:
        title (str): The title of the book.
        author (Author): An instance of the Author class representing the book's author.
        year (int): The year of publication of the book.
    """

    def __init__(self, title, author, year):
        """
        Initialize the Book object.

        Args:
            title (str): The title of the book.
            author (Author): An instance of the Author class representing the book's author.
            year (int): The year of publication of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        """
        Display information about the book.

        Returns:
            str: A formatted string containing the book's title, author's information, and publication year.
        """
        return f"Title: {self.title}, {self.author.display_info()}, Year: {self.year}"

author1 = Author("James Hilton", "British")
book1 = Book("GoodBye Mr Chips", author1, 1934)
print(book1.display_info())

