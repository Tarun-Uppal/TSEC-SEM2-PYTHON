import re

print("Enter a password:")
password = input()

# Validate password criteria
has_length = len(password) >= 8
has_uppercase = re.search(r'[A-Z]', password)
has_lowercase = re.search(r'[a-z]', password)
has_digit = re.search(r'\d', password)
has_special = re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password)

if has_length and has_uppercase and has_lowercase and has_digit and has_special:
    print("Password is valid!")
else:
    print("Password is invalid. It must contain:")
    if not has_length:
        print("- At least 8 characters")
    if not has_uppercase:
        print("- At least one uppercase letter")
    if not has_lowercase:
        print("- At least one lowercase letter")
    if not has_digit:
        print("- At least one digit")
    if not has_special:
        print("- At least one special character")