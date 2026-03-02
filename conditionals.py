# Console Library Management System using Conditionals

library = []

# ---------- ADD BOOK ----------
def add_book():
    print("\nADD BOOK")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # check duplicate ID using condition
    for book in library:
        if book["id"] == book_id:
            print("Book ID already exists!\n")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    library.append(book)
    print("Book added successfully!\n")


# ---------- VIEW BOOKS ----------
def view_books():
    print("\nVIEW BOOKS")

    if len(library) == 0:
        print("No books available\n")
    else:
        for book in library:
            if book["issued"] == True:
                status = "Issued"
            else:
                status = "Available"

            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", status)
            print("--------------------")
    print()


# ---------- ISSUE BOOK ----------
def issue_book():
    print("\nISSUE BOOK")
    book_id = input("Enter Book ID: ")

    for book in library:
        if book["id"] == book_id:

            if book["issued"] == True:
                print("Book already issued\n")
            else:
                book["issued"] = True
                print("Book issued successfully\n")

            return

    print("Book not found\n")


# ---------- RETURN BOOK ----------
def return_book():
    print("\nRETURN BOOK")
    book_id = input("Enter Book ID: ")

    for book in library:
        if book["id"] == book_id:

            if book["issued"] == False:
                print("Book was not issued\n")
            else:
                book["issued"] = False
                print("Book returned successfully\n")

            return

    print("Book not found\n")


# ---------- SEARCH BOOK ----------
def search_book():
    print("\nSEARCH BOOK")
    title = input("Enter book title: ").lower()

    found = False

    for book in library:
        if title in book["title"].lower():
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("--------------------")
            found = True

    if found == False:
        print("No book found\n")


# ---------- MAIN MENU ----------
while True:
    print("===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Program Closed")
        break
    else:
        print("Invalid choice\n")