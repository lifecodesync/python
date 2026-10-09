# 18. Shopping cart using a list
cart = []
while True:
    print("\n1. Add item  2. Remove item  3. Search item  4. Display cart  5. Count items  6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        cart.append(input("Item to add: "))
        print("Item added")
    elif choice == "2":
        item = input("Item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not in cart")
    elif choice == "3":
        item = input("Item to search: ")
        print("Found in cart" if item in cart else "Not found")
    elif choice == "4":
        print("Cart:", cart if cart else "empty")
    elif choice == "5":
        print("Total items:", len(cart))
    elif choice == "6":
        break
    else:
        print("Invalid choice")
