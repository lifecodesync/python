# 19. Students present in class
present = ["Amit", "Riya", "Sneha", "Rahul", "Priya"]
while True:
    print("\n1. Total students  2. Search attendance  3. Add student  4. Remove absent student  5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Total students present:", len(present))
    elif choice == "2":
        name = input("Student name: ")
        print(name, "is present" if name in present else "is absent")
    elif choice == "3":
        present.append(input("Name to add: "))
        print("Student added")
    elif choice == "4":
        name = input("Absent student to remove: ")
        if name in present:
            present.remove(name)
            print("Student removed")
        else:
            print("Student not in list")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
    print("Present:", present)
