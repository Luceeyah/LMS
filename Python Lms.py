import datetime
import os


class LMS:
    """ This class is used to keep record of book library.
     It has total four modules: "Display books", "Issue books", "Add books", "Return books" """
    
    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        
        self.library_name = library_name
        
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n", ""), "lender_name": " ", "Issue_date": "","Status":"Available" }})
            Id += 1

    def display_books(self):
        print("------------------List of Books--------------------")  
        print("Books ID"," \t", "Title")
        print("----------------------------------------------------")     
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"), "]") 
# cat= LMS( "List_of_books.txt", "Python's Library")
# print(cat.display_books())

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys(): #f books in list of books
            print("hello")
            if self.books_dict[books_id]["Status"] != "Available": 
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} "
                      f"on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            else:
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Book Issued Successfully !!!")
        else:
            print("Book ID not found !!!")
            return self.Issue_books()
            

    def add_books(self):
        new_books = input("Enter books title: ")
        if new_books == " ":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title length is too long !!! Title length should be 20 chars")
            return self.add_books
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1) : {'books_title':new_books,'lender_name': " ", 'Issue date': "",'Status':"Available"}})
                print (f"This books '{new_books}' has been added successfully!!!")


    def return_books(self):
        books_id =input("Enter books Id: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already availabe in the library. Please check your book ID.")
                return self.return_books()
            elif not self. books_dict[books_id]["Status"]== "Available":
                self.books_dict[books_id]["lender_name"] = " "
                self.books_dict[books_id]["Issue_date"] = " "
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully Updated !!!! \n")
        else:
            print("Book ID is not found")

    
    def delete_books(self):
        book_id = input("Enter your book Id: ")
        if book_id in self.books_dict:
            del self.books_dict[book_id]
            print(f"Book with ID {book_id} has been deleted.")
        else:
            print("Book ID not found.")

            
try:
    myLMS = LMS("list_of_books.txt", "Python's")
    press_key_list ={"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit", "Del": "Delete Books"}
    key_press =False
    while not (key_press == "q"):
        print(f"\n ----------------- Welcome to {myLMS.library_name} Library Management Sysytem----------------------\n")
        for key,value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\n Current Selection: Issue Books\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\n Current Selection: Add Books\n")
            myLMS.add_books()
        elif key_press == "del":
            print("\n Current Selection: Delete Books\n")
            myLMS.delete_books()
        elif key_press == "d":
            print("\n Current Selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\n Current Selection: Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input!!!")




