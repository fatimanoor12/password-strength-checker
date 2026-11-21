import math
password = input("Enter the password: ")
lowercase_found = False
uppercase_found = False
special_character_found = False
numbers_found = False
count = 0
tips = []
# Check character types
for character in password:
    if character.islower():
        lowercase_found = True
    if character.isupper():
        uppercase_found = True
    if character.isdigit():
        numbers_found = True
    if not character.isalnum():
        special_character_found = True
# Length rules
if len(password) >= 8:
    count += 1
else:
    tips.append("Use at least 8 characters")
if len(password) >= 12:
    count += 1
else:
    tips.append("Use at least 12 characters for better security")
# Character-type rules
if lowercase_found:
    count += 1
else:
    tips.append("Add a lowercase letter")
if uppercase_found:
    count += 1
else:
    tips.append("Add an uppercase letter")
if numbers_found:
    count += 1
else:
    tips.append("Add a number")
if special_character_found:
    count += 1
else:
    tips.append("Add a special character")
# Entropy calculation(theoretical maximum that assumes random choice)
charset_size = 0
if lowercase_found:
    charset_size += 26
if uppercase_found:
    charset_size += 26
if numbers_found:
    charset_size += 10
if special_character_found:
    charset_size += 32
if charset_size > 0:
    entropy = len(password) * math.log2(charset_size)
else:
    entropy = 0
print("Entropy (theoretical, assumes random choice):", round(entropy, 2), "bits")
# Common passwords that should always be marked Weak
common_passwords = [
    "123456", "password", "12345678", "123456789", "12345",
    "1234567890", "1234567", "12345678910", "qwerty", "qwerty123",
    "abc123", "abcd1234", "111111", "11111111", "000000",
    "admin", "admin123", "welcome", "welcome123", "iloveyou",
    "dragon", "monkey", "sunshine", "computer", "letmein",
    "football", "baseball", "princess", "password1",
    "p@ssw0rd", "pass@123", "aa123456", "qwerty12345", "1q2w3e4r"
]
# Common-password check
if password.lower() in common_passwords:
    print("Warning: This password is easily detectable.")
    print("Password Strength: Weak")
else:
    print("Not found in my small list of common passwords.")
    if len(password) < 8:
        print("Password Strength: Weak")
    elif count <= 5:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")
# Suggestions
if tips:
    print("Suggestions to improve your password:")
    for tip in tips:
        print("-", tip)
else:
    print("This password meets this checker's basic rules")
    print("Use a unique password for every account.")