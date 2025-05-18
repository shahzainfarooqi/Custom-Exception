# Custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

# Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        print("Age is valid.")

# Using try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError caught:", e)
except ValueError:
    print("Please enter a valid integer for age.")
