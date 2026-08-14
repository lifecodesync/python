email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email")
else:
    print("Invalid email")