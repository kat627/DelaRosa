class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"'{self.title}' by {self.author}, published in {self.year_published}.")

book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("Brave New World", "Aldous Huxley", 1932)
book3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)

book1.describe()
book2.describe()
book3.describe()
