# a simple login system
def login_system():
    # To set the username and password
    username = "admin"
    password = "admin123"

    # To take input from user
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    # Check credentials
    if input_username == username and input_password == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Test
if __name__ == "__main__":
    login_system()
