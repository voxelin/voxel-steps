user_data = input("Enter your age: ")

try:
    age = int(user_data)
    print("Your age is", age)
except ValueError:
    print("Invalid age!")