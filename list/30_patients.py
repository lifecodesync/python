# 30. Patient names and ages using lists
names = ["Ravi", "Meena", "Suresh"]
ages = [45, 32, 60]
while True:
    print("\n1. Add patient  2. Delete patient  3. Search patient  4. Display all  5. Count patients  6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        names.append(input("Patient name: "))
        ages.append(int(input("Patient age: ")))
        print("Patient added")
    elif choice == "2":
        name = input("Patient to delete: ")
        if name in names:
            i = names.index(name)
            names.pop(i)
            ages.pop(i)
            print("Patient deleted")
        else:
            print("Patient not found")
    elif choice == "3":
        name = input("Patient to search: ")
        if name in names:
            print(name, "- Age:", ages[names.index(name)])
        else:
            print("Patient not found")
    elif choice == "4":
        for n, a in zip(names, ages):
            print(n, "-", a)
    elif choice == "5":
        print("Total patients:", len(names))
    elif choice == "6":
        break
    else:
        print("Invalid choice")
