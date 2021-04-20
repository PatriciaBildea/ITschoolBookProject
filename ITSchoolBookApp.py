def add_book():
    book_title = input("Add book title --> ")
    book_author = input("Add book author --> ")

    import csv  # importing csv library
    with open("BooksDB.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])
        writer.writerow({"BookTitle": book_title, "BookAuthor": book_author})
    print(f"Book '{book_title}' by {book_author} was added successfully!")


def list_books():
    print("Available books are:")


def update_book():
    print("Update a book")


def share_book():
    print("Share a book")
    

# Main menu for user
option = int(input('''Menu:
1: Add a book
2: List books
3: Update a book
4: Share a book
Select one option --> '''))

if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("That is not a valid option")
