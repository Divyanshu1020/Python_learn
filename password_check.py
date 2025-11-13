password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long")
elif password.isalpha():
    print("Password must contain at least one number")
elif password.isdigit():
    print("Password must contain at least one letter")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one number")
else:
    print("Password is valid") 