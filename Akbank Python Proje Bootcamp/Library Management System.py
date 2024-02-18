
class Library:
    def __init__(self, filename):
        self.filename = open(filename, "a+")
        filename ="books.txt"
    def list_books(self):
        with open("books.txt", "r") as self.filename:
            book_s = self.filename.read().splitlines()
            for book in book_s:
                book = book.split(",")
                print("Book Name:", book[0], "Author:", book[1])

    def add_book(self):
        new_book_name = input("Book Name: ") 
        new_book_author = input("Author: ") 
        new_book_relase_year =input("Relase Year: ") 
        new_book_number_of_pages = input("Number of Pages: ")
        new_book = f"{new_book_name}, {new_book_author}, {new_book_relase_year}, {new_book_number_of_pages} \n"
        with open("books.txt","a+") as self.filename:
            self.filename.write(new_book)
            print("Book added successfully!")
    
    def delete_book(self):
        delete_book_name = input("Please enter a book name to delete:")
        with open("books.txt", "r") as self.filename:
            lines = self.filename.readlines()    
        with open("books.txt", "w") as self.filename:
            for index, line in enumerate(lines):
                delete_book = line.split(",")[0].strip()
                if delete_book_name == delete_book:
                    del lines[index]
                    self.filename.seek(0)
                    self.filename.truncate()
                    self.filename.writelines(lines)
                    print("Book deleted successfully!")
                    return

lib = Library("books.txt")

while True:
    print("*****MENU*****")
    print("1)List Books")
    print("2)Add Book")
    print("3)Delete Book")
    print("4)Exit")
    choice = input("Please enter a number 1-4: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.delete_book()
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid number!")
   
