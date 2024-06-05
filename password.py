import re
import string

def password_strength(password):
    # Initialize the score
    score = 0

    # Check the length of the password
    if len(password) < 8:
        print("Password length is weak. It should be at least 8 characters.")
    elif len(password) >= 8:
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        print("Password contains at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        print("Password contains at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
        print("Password contains at least one number.")

    # Check for special characters
    if re.search(r"\W", password):
        score += 1
        print("Password contains at least one special character.")

    # Check for dictionary words
    if re.search(r"\b\w{4,}\b", password):
        print("Password contains a dictionary word. It's weak.")

    # Check for password reuse
    if re.search(r"\b\w{8,}\b", password):
        print("Password is too similar to previous passwords. It's weak.")

    # Check for consecutive characters
    if re.search(r"(.)\1{2,}", password):
        print("Password contains consecutive characters. It's weak.")

    # Check for common patterns
    if re.search(r"(abc|def|ghi|jkl|mno|pqr|stu|vwx|yz)", password):
        print("Password contains a common pattern. It's weak.")

    # Provide feedback based on the score
    if score < 2:
        print("Password strength: Weak")
    elif score == 2:
        print("Password strength: Medium")
    else:
        print("Password strength: Strong")

# Ask for user input
password = input("Enter a password: ")

# Check the password strength
password_strength(password)
