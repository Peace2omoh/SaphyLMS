# catalog is a dictionary to hold info about all books at once
# borrower_id is a list datatype that holds library members who borrowed the book, the library members is of set datatype
#Library Catalog Management
import LC
catalog = LC.catalog


# sggsg
book_names_db = LC.catalog["book_name"]
book_authors_db = LC.catalog["book_author"]
book_stock_db = LC.catalog["stock"]
book_borrower_id_db = LC.catalog["borrower_id"]
book_borrower_name_db = LC.catalog["borrower_name"]
def book_index(book_name, book_author):
    # This function detects the index of the book specified, a book might have same name but different
    # or one author for multiple books, this function sustains the ability to resolve this and detect
    # the exact book specified irrespective of same name/author problem
    indx = -1
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    book_found = False
    for i in book_names_db:
        if(i==book_name):
            indx = book_names_db.index(i)
            book_found = LC.catalog["book_author"][indx] == book_author
            if book_found: break

    if book_found:
        print(book_name+" by "+book_author+" found")
    else:
        print(book_name+" by "+book_author+" not found")
        indx = -1;
    return indx
def add_book(book_name, book_author, no):
    print("\nadding books...............................")
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    if (no >= 1):
        LC.catalog["book_name"].append(book_name)
        LC.catalog["book_author"].append(book_author)
        LC.catalog["stock"].append(no)
        LC.catalog["borrower_id"].append([])
        LC.catalog["borrower_name"].append([])
        print(book_name +" by "+book_author+" successfully added to the LMS Catalog")
    else:
        print(book_name +" by "+book_author+" can't be added the LMS Catalog")
    print("...........................................\n")
def delete_book(book_name, book_author):
    print("\ndeleting books...............................")
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    indx = book_index(book_name,book_author)
    if (indx>= 0):
        LC.catalog["book_name"].pop(indx)
        LC.catalog["book_author"].pop(indx)
        LC.catalog["stock"].pop(indx)
        LC.catalog["borrower_id"].pop(indx)
        LC.catalog["borrower_name"].pop(indx)
        print(book_name +" by "+book_author+" successfully deleted from the LMS Catalog")
    else:
        print(book_name +" by "+book_author+" can't be deleted from the LMS Catalog")
    print("...........................................\n")
#def restock - a cousin to add() to add more to the stock available
def restock_book(book_name, book_author, no):
    print("\nrestocking...............................")
    book_name = str.lower(book_name)
    book_author = str.title(book_author)
    indx = book_index(book_name, book_author)
    if (no >= 1 and indx>=0):
        book_stock_db[indx]+=no
        print(str(no)+" "+book_name+" by "+book_author+" successfully added to the LMS Catalog")
    else:
        print(book_name +" by "+book_author+" can't be added the LMS Catalog")
    print("...........................................\n")
