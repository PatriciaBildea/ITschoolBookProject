def add_book():
    book_title = input("Add book title (Type 'R' to return to main menu) --> ").upper()
    if book_title != "R":
        import csv  # importing csv library
        with open("BooksDB.csv", mode="r") as file:
            list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
            book_not_present = True
            for book in list_of_books:
                if book.get("BookTitle") == book_title:
                    book_not_present = False
            if book_not_present:
                book_author = input("Add book author (Type 'R' to return to main menu) --> ").upper()
                if book_author != "R":
                    with open("BooksDB.csv", mode="a") as file:
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
            print(f'{index}. {title["BookTitle"]} by {title["BookAuthor"]}. '
                  f'Shared with: {title["SharedWith"]}. '
                  f'Book read: {title["IsRead"]}. '
                  f'Review: {title["Review"]}')


def update_book():
    title = input("What book are you looking to update today? (Type 'R' to return to main menu) --> ").upper()
    if title != "R":
        book_not_present = True # used to check if book is in the list
        import csv
        with open("BooksDB.csv", mode="r") as file:
            list_of_books = list(csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"]))
            delete = open("BooksDB.csv", mode="w+")
            delete.truncate()  # clears the CSV
            for book in list_of_books:
                if book.get("BookTitle") == title:
                    book_not_present = False
                    wrong_choice = True
                    read = ""
                    while wrong_choice:
                        read = input(f"Did you read {title}? Y/N --> ").upper()
                        if read != "Y" and read != "N":
                            wrong_choice = True
                            print("That is not a valid option")
                        else:
                            wrong_choice = False
                    if read == "Y":
                        read = "Read"
                        with open("BooksDB.csv", mode="a") as file:
                            writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                      "Review"])
                            writer.writerow(
                                {"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                 "SharedWith": book.get("SharedWith"), "IsRead": read, "Review": book.get("Review")})
                    elif read == "N":
                        read = "Not read"
                        with open("BooksDB.csv", mode="a") as file:
                            writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                      "Review"])
                            writer.writerow(
                                {"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                 "SharedWith": book.get("SharedWith"), "IsRead": read, "Review": book.get("Review")})
                    print(f"Book {title} was updated successfully!")
                else:
                    with open("BooksDB.csv", mode="a") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                  "Review"])
                        writer.writerow(
                            {"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                             "SharedWith": book.get("SharedWith"), "IsRead": book.get("IsRead"), "Review": book.get("Review")})
            if book_not_present:
                wrong_choice = True
                while wrong_choice:
                    add = input('''This book is not in our list. 
Would you like to add this book? Y/N (Type 'R' to return to main menu) --> ''').upper()
                    if add != "R":
                        if add != "Y" and add != "N":
                            wrong_choice = True
                            print("That is not a valid option")
                        elif add == "Y":
                            wrong_choice = False
                            book_title = title
                            book_author = input("Add book author (Type 'R' to return to main menu) --> ").upper()
                            if book_author != "R":
                                with open("BooksDB.csv", mode="a") as file:
                                    writer = csv.DictWriter(file,
                                                            fieldnames=["BookTitle", "BookAuthor", "SharedWith",
                                                                        "IsRead",
                                                                        "Review"])
                                    writer.writerow(
                                        {"BookTitle": book_title, "BookAuthor": book_author, "SharedWith": "",
                                         "IsRead": "Not read", "Review": "No review added"})
                                print(f"Book '{book_title}' by {book_author} was added successfully!")
                        else:
                            wrong_choice = False
                    else:
                        wrong_choice = False


def share_book():
    title = input("What book are you looking for today? (Type 'R' to return to main menu) --> ").upper()
    if title != "R":
        book_not_present = True
        import csv
        with open("BooksDB.csv", mode="r") as file:
            list_of_books = list(csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"]))
            delete = open("BooksDB.csv", mode="w+")
            delete.truncate()  # clears the CSV
            for book in list_of_books:
                if book.get("BookTitle") == title:
                    new_share = input(f"Who would you like to share {title} with? --> ").upper()
                    shared_with = book.get("SharedWith") + new_share + ", "
                    with open("BooksDB.csv", mode="a") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"), "SharedWith": shared_with, "IsRead": book.get("IsRead"), "Review": book.get("Review")})
                        print(f"{title} is now shared with {shared_with}")
                        book_not_present = False
                else:
                    with open("BooksDB.csv", mode="a") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                  "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                         "SharedWith": book.get("SharedWith"), "IsRead": book.get("IsRead"),
                                         "Review": book.get("Review")})
        if book_not_present:
            wrong_choice = True
            while wrong_choice:
                add = input('''This book is not in our list. 
Would you like to add this book? Y/N (Type 'R' to return to main menu) --> ''').upper()
                if add != "R":
                    if add != "Y" and add != "N":
                        wrong_choice = True
                        print("That is not a valid option")
                    elif add == "Y":
                        wrong_choice = False
                        book_title = title
                        book_author = input("Add book author (Type 'R' to return to main menu) --> ").upper()
                        if book_author != "R":
                            with open("BooksDB.csv", mode="a") as file:
                                writer = csv.DictWriter(file,
                                                        fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                    "Review"])
                                writer.writerow({"BookTitle": book_title, "BookAuthor": book_author, "SharedWith": "",
                                                 "IsRead": "Not read", "Review": "No review added"})
                            print(f"Book '{book_title}' by {book_author} was added successfully!")
                    else:
                        wrong_choice = False
                else:
                    wrong_choice = False

def book_review():
    title = input("What book are you looking for today? (Type 'R' to return to main menu) --> ").upper()
    if title != "R":
        import csv
        with open("BooksDB.csv", mode="r") as file:
            list_of_books = list(csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"]))
            delete = open("BooksDB.csv", mode="w+")
            delete.truncate()  # clears the CSV
            book_not_present = True
            for book in list_of_books:
                if book.get("BookTitle") == title:
                    book_not_present = False
                    if book.get("IsRead") == "Read":
                        review = input(f"What did you think of {title}? --> ").upper()
                        with open("BooksDB.csv", mode="a") as file:
                            writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                            writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"), "SharedWith": book.get("SharedWith"), "IsRead": book.get("IsRead"), "Review": review})
                            print(f"Review successfully added for {title}")
                    else:
                        wrong_choice = True
                        while wrong_choice:
                            read = input(f"Did you read {title}? Y/N --> ").upper()
                            if read != "Y" and read != "N":
                                wrong_choice = True
                                print("That is not a valid option")
                            else:
                                wrong_choice = False
                        if read == "Y":
                            read = "Read"
                            review = input(f"What did you think of {title}? --> ").upper()
                            with open("BooksDB.csv", mode="a") as file:
                                writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead", "Review"])
                                writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"), "SharedWith": book.get("SharedWith"), "IsRead": read, "Review": review})
                            print(f"Review successfully added for {title}")
                        elif read == "N":
                            print('''You can't leave a review for a book that is not read. 
Please select a different option''')
                else:
                    with open("BooksDB.csv", mode="a") as file:
                        writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                  "Review"])
                        writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                         "SharedWith": book.get("SharedWith"), "IsRead": book.get("IsRead"), "Review": book.get("Review")})
        if book_not_present:
            wrong_choice = True
            while wrong_choice:
                add = input('''This book is not in our list. 
Would you like to add this book? Y/N (Type 'R' to return to main menu) --> ''').upper()
                if add != "R":
                    if add != "Y" and add != "N":
                        wrong_choice = True
                        print("That is not a valid option")
                    elif add == "Y":
                        wrong_choice = False
                        book_title = title
                        book_author = input("Add book author (Type 'R' to return to main menu) --> ").upper()
                        if book_author != "R":
                            with open("BooksDB.csv", mode="a") as file:
                                writer = csv.DictWriter(file,
                                                        fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead",
                                                                    "Review"])
                                writer.writerow({"BookTitle": book_title, "BookAuthor": book_author, "SharedWith": "",
                                                 "IsRead": "Not read", "Review": "No review added"})
                            print(f"Book '{book_title}' by {book_author} was added successfully!")
                    else:
                        wrong_choice = False
                else:
                    wrong_choice = False


menu = True  # Used for menu loop
# Main menu for user:
while menu:
    option = input('''Menu:
    1: Add a book
    2: List books
    3: Update a book
    4: Share a book
    5: Add book review
    6: Exit
    Select one option --> ''')

    try:
        option = int(option)
    except:
        print("That is not a valid option")
    else:
        if option not in range(1, 7):
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
