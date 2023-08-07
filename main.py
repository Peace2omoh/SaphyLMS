import LCM
import BCM
import LMM
import pprint
import Script
import time
print("Welcome to Saphy Library Management System (SLMS)")
print("What would you like to do today?")
end = True
def intro():

    print("--Library Catalog Management--\n")
    print("1. View the catalog")
    print("2. Add books to the catalog")
    print("3. Delete books from the catalog")
    print("4. Restock the catalog\n")
    print("--Books Circulation Management--")
    print("5. Borrow books from the library")
    print("6. Return borrowed books\n")
    print("--Library Members Management--\n")
    print("7. Add a new member to the Library Database")
    print("8. Exit")
    Command = input("Enter A Command")
    try:
        Command = int(Command)
        if(Command>=1 and Command<=8):
            Script.resolve(Command)
            return Script.terminate
        else:
            print("Only enter a Number from 1-7")
            time.sleep(3)
            return True
    except ValueError:
        print("Only enter a Number")
        time.sleep(3)
        return True

while(end):
    end=intro()
print("\n Thank you for using Saphy Library Management System\n")
#LCM.add_book("AlgoRevX","Adepoju Damilare",7)
#BCM.borrow_book("AlgoRevx","AdePOju damilARe","slms0")
#BCM.borrow_book("algobeast","donatus","slms0")
#BCM.borrow_book("algobeast","donatus","slms0")
#BCM.borrow_book("algobeast","donatus","slms0")
#BCM.borrow_book("algobeast","donatus","slms0")
#pprint.pprint(LCM.catalog)
#LCM.delete_book("algorevx","Adepoju Damilare")
#pprint.pprint(LCM.catalog)
#LCM.restock_book("algobeast","donatus",18)
#pprint.pprint(LCM.catalog)
#LMM.member_index("SLMS1")
#LMM.add_member("precious")
#BCM.borrow_book("algobeast","Donatus","slms2")
#pprint.pprint(LCM.catalog)
#BCM.return_book("algobeast","Donatus","slms1")
#pprint.pprint(LCM.catalog)

