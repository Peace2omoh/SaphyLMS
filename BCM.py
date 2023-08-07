import LCM
import LMM
#Book Circulation Management
def borrow_book(book_name, book_author, member_id):
    print("\nborrowing books...............................")
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    book_index = LCM.book_index(book_name,book_author)
    member_index = LMM.member_index(member_id)
    if (book_index>=0 and member_index>=0):
        if (LCM.book_stock_db[book_index]>=1):
            LCM.book_stock_db[book_index]= (LCM.book_stock_db[book_index] - 1);
            LCM.book_borrower_id_db[book_index].append(member_id)
            LCM.book_borrower_name_db[book_index].append(LMM.members_name_db[member_index])
            print(book_name +" by "+book_author+" successfully borrowed by "+LMM.members_name_db[member_index]+" remaining "+str(LCM.book_stock_db[book_index])+" in stock")
        else:
            print(book_name +" by "+book_author+" no longer available")
    else:
        print(book_name +" by "+book_author+" cannot be borrowed")
    print("...........................................\n")

def return_book(book_name, book_author, member_id):
    print("\nreturning books...............................")
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    member_id = str.lower(member_id)
    book_index = LCM.book_index(book_name,book_author)
    member_index = LMM.member_index(member_id)
    member_transact = False
    book_borrower_name_db = ""
    book_borrower_id_db = ""
    book_stock = ""
    borrower_name = ""
    borrower_id = ""

    if (book_index >= 0 and member_index >= 0):
        book_borrower_name_db = LCM.book_borrower_name_db[book_index]
        book_borrower_id_db = LCM.book_borrower_id_db[book_index]
        book_stock = LCM.book_stock_db[book_index]
        borrower_name = LMM.members_name_db[member_index]
        borrower_id = LMM.members_id_db[member_index]
        if borrower_id in book_borrower_id_db:
            member_transact = True
        if(member_transact):
                    book_borrower_id_db.remove(borrower_id)
                    book_borrower_name_db.remove(borrower_name)
                    LCM.book_stock_db[book_index] +=1
                    print(book_name +" by "+book_author+" successfully returned by "+borrower_name+" remaining "+str(LCM.book_stock_db[book_index])+" in stock")
        else:
            print(book_name + " by " + book_author + " wasn't borrowed by " + LMM.members_name_db[member_index])
    else:
        print(book_name + " by " + book_author + " cannot be added/returned to the catalog")
    print("...........................................\n")