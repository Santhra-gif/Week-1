# palindrome_check.py

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert string to lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# To test the given string
string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
