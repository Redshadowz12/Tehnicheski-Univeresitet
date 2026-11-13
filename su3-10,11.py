class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def print(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

class EBook(Book):
    def __init__(self, title, author, year, format, size):
        super().__init__(title, author, year)
        self.format = format
        self.size = size
    def print(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Format: {self.format}, Size: {self.size}MB")


print("--- Books ---")
book1 = Book("Under the Yoke", "Ivan Vazov", 1894)
book1.print()

print("\n--- EBooks ---")
ebook1 = EBook("1984", "George Orwell", 1949, "EPUB", 2.1)
ebook1.print()