def add_book():
    book_title = input("Add book title --> ")
    book_author = input("Add book author --> ")

    import csv  # importing csv library
    with open("BooksDB.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])
        writer.writerow({"BookTitle": book_title, "BookAuthor": book_author, "SharedWith": "Nobody", "IsRead": "No"})
    print(f"Book '{book_title}' by {book_author} was added successfully!")


def list_books():
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])  # takes all from DB
        print("Available books are: ")
        index = 0
        for title in list_of_books:
            index += 1
            print(f'{index}. {title["BookTitle"]} by {title["BookAuthor"]}. Shared with: {title["SharedWith"]}. Book read: {title["IsRead"]}')


def update_book():
    title = input("What book are you looking for today? --> ")
    list_of_books = []
    read = "No"
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])
        for book in list_of_books:
            if book.get("BookTitle") != title:
                add = input('''This book is not in our list.
Would you like to add this book? Y/N --> ''')
                if add == "Y":
                    add_book()
                else:
                    print("Good bye!")
            else:
                read = input(f"Did you read {title}? Y/N --> ")
                if read == "Y":
                    read = "Yes"
                    with open("BooksDB.csv", mode="w") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
"SharedWith": book.get("SharedWith"), "IsRead": read})
                    print(f"Book {title} was updated successfully!")
                break




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
