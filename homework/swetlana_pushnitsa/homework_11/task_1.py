class Book:
    page_material = "paper"
    there_is_text = True

    def __init__(self, name, author, page_number, isbn, reserved):
        self.name = name
        self.author = author
        self.page_number = page_number
        self.isbn = isbn
        self.reserved = reserved


class SchoolBook(Book):

    def __init__(self, name, author, page_number, isbn, reserved, subject, group, tasks):
        super().__init__(name, author, page_number, isbn, reserved)
        self.subject = subject
        self.group = group
        self.tasks = tasks


book_1 = Book("Dracula", "Brem Stocker", 234, 2365497, True)
book_2 = Book("Magic Rock", "Thomas Mann", 860, 54903647, False)
book_3 = Book("The Day", "Michael Cunningham", 300, 5369854, False)
book_4 = Book("February 1933", "Uwe Wittstock", 169, 9865742, False)
book_5 = Book("Orlando", "Virginia Woolf", 471, 5964236, False)
book_6 = SchoolBook("Mathematics", "Petrov", 400, 869037, True,
                    "Math", 8, True)
book_7 = SchoolBook("English", "Semenov", 600, 569712, False,
                    "English language", 7, True)
book_8 = SchoolBook("History", "Marivanna", 120, 78549, False,
                    "International History", 10, False)


def print_book_info(value):
    if value.reserved is True:
        print(
            f"Name: {value.name}, Author: {value.author}, Number of pages: {value.page_number}, "
            f"Material: {value.page_material}, status: reserved"
        )
    else:
        print(
            f"Name: {value.name}, Author: {value.author}, Number of pages: {value.page_number}, "
            f"Material: {value.page_material}"
        )


def print_school_book_info(value):
    if value.reserved is True:
        print(
            f"Name: {value.name}, Author: {value.author}, Number of pages: {value.page_number}, "
            f"Subject: {value.subject}, Class: {value.group}, status: reserved"
        )
    else:
        print(f"Name: {value.name}, Author: {value.author}, Number of pages: {value.page_number}, "
              f"Subject: {value.subject}, Class: {value.group}")


print_book_info(book_1)
print_book_info(book_2)
print_book_info(book_3)
print_book_info(book_4)
print_book_info(book_5)
print_school_book_info(book_6)
print_school_book_info(book_7)
print_school_book_info(book_8)
