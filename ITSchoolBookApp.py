def add_book():
    book_title = input("Add book title --> ").upper()

    import csv  # importing csv library
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
        book_not_present = True
        for book in list_of_books:
            if book.get("BookTitle") == book_title:
                book_not_present = False
        if book_not_present:
            book_author = input("Add book author --> ").upper()
            with open("BooksDB.csv", mode="a") as file:
                list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                writer.writerow({"BookTitle": book_title, "BookAuthor": book_author, "SharedWith": "", "IsRead": "Not read", "Review": "No review added"})
            print(f"Book '{book_title}' by {book_author} was added successfully!")
        else:
            print("Book already added")


def list_books():
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])  # takes all from DB
        print("Available books are: ")
        index = 0
        for title in list_of_books:
            index += 1
            print(f'{index}. {title["BookTitle"]} by {title["BookAuthor"]}. Shared with: {title["SharedWith"]}. Book read: {title["IsRead"]}. Review: {title["Review"]}')


def update_book():
    title = input("What book are you looking for today? --> ").upper()
    list_of_books = []
    read = "Not read"
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
        for book in list_of_books:
            if book.get("BookTitle") == title:
                book_not_present = False
                while wrong_choice:
                    read = input(f"Did you read {title}? Y/N --> ")
                    if read not in ["y", "Y", "n", "N"]:
                        wrong_choice = True
                        print("That is not a valid option")
                    else:
                        wrong_choice = False
                if read == "Y" or "y":
                    read = "Read"
                    with open("BooksDB.csv", mode="w") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
"SharedWith": book.get("SharedWith"), "IsRead": read, "Review": book.get("Review")})
                else:
                    read = "Not read"
                    with open("BooksDB.csv", mode="w") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                         "SharedWith": book.get("SharedWith"), "IsRead": read, "Review": book.get("Review")})
                print(f"Book {title} was updated successfully!")
                break
            else:
                book_not_present = True
    if book_not_present:
        while wrong_choice:
            add = input('''This book is not in our list. Would you like to add this book? Y/N --> ''')
            if add not in ["y", "Y", "n", "N"]:
                wrong_choice = True
                print("That is not a valid option")
            else:
                wrong_choice = False
        if add == "Y" or "y":
            add_book()

def share_book():
    title = input("What book are you looking for today? --> ").upper()
    list_of_books = []
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
        for book in list_of_books:
            if book.get("BookTitle") == title:
                new_share = input(f"Who would you like to share {title} with? --> ")
                shared_with = book.get("SharedWith") + ", " + new_share
                with open("BooksDB.csv", mode="w") as file:
                    writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                    writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                     "SharedWith": shared_with, "IsRead": book.get("IsRead"), "Review": book.get("Review")})
                print(f"{title} is now shared with {shared_with}")
                book_not_present = False
                break
            else:
                book_not_present = True
    if book_not_present:
        while wrong_choice:
            add = input('''This book is not in our list. Would you like to add this book? Y/N --> ''')
            if add not in ["y", "Y", "n", "N"]:
                wrong_choice = True
                print("That is not a valid option")
            else:
                wrong_choice = False
        if add == "Y" or "y":
            add_book()


def book_review():
    title = input("What book are you looking for today? --> ").upper()
    list_of_books = []
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
        for book in list_of_books:
            if book.get("BookTitle") == title:
                book_not_present = False
                if book.get("IsRead") == "Read":
                    review = input(f"What did you think of {title} --> ")
                    with open("BooksDB.csv", mode="w") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                         "SharedWith": book.get("SharedWith"), "IsRead": book.get("IsRead"), "Review": review})
                    print(f"Review successfully added for {title}")
                else:
                    wrong_choice = True
                    while wrong_choice:
                        read = input(f"Did you read {title}? Y/N --> ")
                        if read not in ["y", "Y", "n", "N"]:
                            wrong_choice = True
                            print("That is not a valid option")
                        else:
                            wrong_choice = False
                    if read == "Y" or "y":
                        read = "Read"
                        with open("BooksDB.csv", mode="w") as file:
                            writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                      "Review"])
                            writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                             "SharedWith": book.get("SharedWith"), "IsRead": read,
                                             "Review": book.get("Review")})
                    else:
                        print("You can't leave a review for a book that is not read. Please select a different option")
                break
            else:
                book_not_present = True
    if book_not_present:
        wrong_choice = True
        while wrong_choice:
            add = input('''This book is not in our list. Would you like to add this book? Y/N --> ''')
            if add not in ["y", "Y", "n", "N"]:
                wrong_choice = True
                print("That is not a valid option")
            else:
                wrong_choice = False
        if add == "Y" or "y":
            add_book()


book_not_present = True
add = ""
wrong_choice = True
menu = True
# Main menu for user
while menu:
    option = input('''Menu:
    1: Add a book
    2: List books
    3: Update a book
    4: Share a book
    5: Add book review
    6: Exit
    Select one option --> ''')

    if option not in ["1", "2", "3", "4", "5", "6"]:
        print("That is not a valid option")
    elif int(option) == 1:
        add_book()
    elif int(option) == 2:
        list_books()
    elif int(option) == 3:
        update_book()
    elif int(option) == 4:
        share_book()
    elif int(option) == 5:
        book_review()
    elif int(option) == 6:
        menu = False
        print("Good bye!")
