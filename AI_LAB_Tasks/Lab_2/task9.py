# 9. (1 point) A library wants to manage its book records using a Python dictionary where each book
# has a unique ISBN as the key.
# 1. Store book information in a dictionary with details like title, author, year, and availability
# status.
# 2. Implement a function that allows a user to search for a book by ISBN.
# 3. Implement a function to check out a book(mark it as unavailable).
# 4. Implement a function to return a book(mark it as available).
# 5. Display the total number of available and borrowed books.


library = {
    "978-0132350884": {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "available": True},
    "978-0201616224": {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999, "available": True},
    "978-1491950357": {"title": "The Clean Coder", "author": "Robert C. Martin", "year": 2011, "available": True},
    "978-0131103627": {"title": "The C Programming Language", "author": "Brian W. Kernighan", "year": 1978, "available": False},
    "978-0134494166": {"title": "Effective Java", "author": "Joshua Bloch", "year": 2017, "available": True},
}


def search_book(isbn):
    if isbn in library:
        book = library[isbn]
        status = "Available" if book["available"] else "Not Available"
        print(
            f"\nBook Found:\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nStatus: {status}")
    else:
        print("\nBook not found!")


def checkout_book(isbn):
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            print(
                f"\nBook '{library[isbn]['title']}' has been checked out successfully!")
        else:
            print("\nThis book is already checked out!")
    else:
        print("\nInvalid ISBN. Book not found!")


def return_book(isbn):
    if isbn in library:
        if not library[isbn]["available"]:
            library[isbn]["available"] = True
            print(
                f"\nBook '{library[isbn]['title']}' has been returned successfully!")
        else:
            print("\nThis book is already available!")
    else:
        print("\nInvalid ISBN. Book not found!")


def display_book_counts():
    available_books = sum(1 for book in library.values() if book["available"])
    borrowed_books = len(library) - available_books
    print(f"\nTotal Available Books: {available_books}")
    print(f"Total Borrowed Books: {borrowed_books}")


search_book("978-0132350884")
checkout_book("978-0132350884")
return_book("978-0132350884")
display_book_counts()
