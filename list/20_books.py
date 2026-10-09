# 20. List of books
books = ["Wings of Fire", "The Alchemist", "Atomic Habits"]
while True:
    print("\n1. Add book  2. Search book  3. Remove book  4. Display books  5. Count books  6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        books.append(input("Book name: "))
        print("Book added")
    elif choice == "2":
        name = input("Book to search: ")
        print("Book available" if name in books else "Book not found")
    elif choice == "3":
        name = input("Book to remove: ")
        if name in books:
            books.remove(name)
            print("Book removed")
        else:
            print("Book not found")
    elif choice == "4":
        for i, b in enumerate(books, 1):
            print(i, b)
    elif choice == "5":
        print("Total books:", len(books))
    elif choice == "6":
        break
    else:
        print("Invalid choice")
