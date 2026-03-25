import re

# Prompt user for email
email = input("Enter E-mail: ")

# Prompt user for password
password = input("Enter Password: ")

# Email validation - all small letters
email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
email_valid = re.match(email_pattern, email)

# Password validation
# At least 8 characters, max 12
# At least one uppercase, one lowercase, one digit, one special character
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$'
password_valid = re.match(password_pattern, password)

# Display results
if email_valid:
    print("✓ E-mail is valid")
else:
    print("✗ E-mail is invalid")

if password_valid:
    print("✓ Password is valid")
else:
    print("✗ Password is invalid")