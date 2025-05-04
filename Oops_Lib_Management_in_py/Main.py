from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    def __init__(self, title):
        self._title = title  # Protected (Encapsulation)

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return f"Item: {self._title}"


# Inheritance + Polymorphism
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def info(self):
        return f"Book: {self._title}, Author: {self.author}"


class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration

    def info(self):
        return f"DVD: {self._title}, Duration: {self.duration} mins"


# User class with Class/Static Methods and Encapsulation
class User:
    user_count = 0  # Class variable

    def __init__(self, name):
        self.__name = name  # Private
        self.borrowed_items = []
        User.user_count += 1

    def borrow_item(self, item: LibraryItem):
        self.borrowed_items.append(item)

    def show_borrowed(self):
        for item in self.borrowed_items:
            print(item.info())

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @staticmethod
    def rules():
        print("Each user can borrow up to 5 items.")


# Using the system
book1 = Book("The Alchemist", "Paulo Coelho")
dvd1 = DVD("Inception", 148)

user1 = User("Alice")
user1.borrow_item(book1)
user1.borrow_item(dvd1)

print("Borrowed Items:")
user1.show_borrowed()

print("\nTotal Users:", User.get_user_count())
User.rules()
