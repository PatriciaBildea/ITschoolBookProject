def list_books():
    print("Available books are:")
def add_book():
    print("Add a book")
def update_book():
    print("Update a book")
def share_book():
    print("Share a book")

# Main menu for user
option = int(input('''Menu:
1: List books
2: Add a book
3: Update a book
4: Share a book
Select one option --> '''))

if option == 1:
    list_books()
elif option == 2:
    add_book()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("That is not a valid option")
