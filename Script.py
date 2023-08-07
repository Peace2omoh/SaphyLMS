import LCM
import BCM
import LMM
import pprint
import time
book_name_set = "sample"
book_author_set = ""
book_no_set = ""
member_id_set = ""
terminate = True
def setCirculationInput():
    global book_name_set
    global  member_id_set
    global book_author_set
    time.sleep(1)
    book_name_set = input("Enter the book name")
    book_author_set = input("Enter the book author's name")
    member_id_set = input("Enter member id")
def setBookInput():
    global book_name_set
    global  book_no_set
    global book_author_set
    time.sleep(1)
    try:
        book_name_set = input("Enter the book name")
        book_author_set = input("Enter the book author's name")
        book_no_set = int(input("How many?"))
        return True
    except ValueError:
        return False
def resolve(Input):
    global terminate
    print(Input)
    if(Input == 1):
        pprint.pprint(LCM.catalog)
    elif(Input == 2):
        print("Follow the instruction below to add a book")
        if(setBookInput()):
            LCM.add_book(book_name_set,book_author_set,book_no_set)
    elif(Input == 3):
        print("Follow the instruction below to delete a book")
        print("Note that all the book records will be deleted irrespective of the number specified")
        if (setBookInput()):
            LCM.delete_book(book_name_set, book_author_set)
    elif (Input == 4):
        print("Follow the instruction below to restock a book")
        if (setBookInput()):
            LCM.restock_book(book_name_set, book_author_set, book_no_set)
    elif (Input == 5):
        print("Follow the instruction below to borrow a book")
        setCirculationInput()
        BCM.borrow_book(book_name_set, book_author_set, member_id_set)
    elif (Input == 6):
        print("Follow the instruction below to return a borrowed book")
        setCirculationInput()
        BCM.return_book(book_name_set, book_author_set, member_id_set)
    elif(Input == 7):
        time.sleep(1)
        name = input("Enter the new Member Name")
        LMM.add_member(name)
    elif(Input == 8):
        print("Exiting.....................")
        time.sleep(3)
        terminate = False