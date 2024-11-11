class Book:
    __no_of_copies = 0
    __sonal=0

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.avail = False

    def display_details(self):
        print(f"Title : {self.title}\nAuthor: {self.author}\nYear:{self.year}")
        print(Book.__sonal)

    def borrow_book(self):
        print(f"Book availability : available {self.avail}")

    def return_book(self):
        self.avail = True
        print(f"Book returned")


    @classmethod
    def update_copies(cls):
        Book.__no_of_copies += 1
        print(f"no. of copies available : {cls.__no_of_copies}")

    @staticmethod
    def car_info():
        print("Books are man's best friend")



if __name__ =='__main__':
    b1 = Book("Abc", "efg", 2022)
    b1.display_details()
    b1.borrow_book()
    b1.return_book()
    b1.borrow_book()
    b1.update_copies()

    b2 = Book("hij", "klm", 2024)
    b2.display_details()
    b2.borrow_book()
    b2.return_book()
    b2.borrow_book()
    b2.update_copies()

    b3 = Book("hij", "klm", 2024)
    b3.display_details()
    b3.borrow_book()
    b3.return_book()
    b3.borrow_book()
    b3.update_copies()

    Book.car_info()















