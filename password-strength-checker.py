password =input("Enter the password:")
lowercase_found = False
uppercase_found = False
special_character_found = False
numbers_found = False
count = 0
tips = []
for character in password:
    if character.islower():
            lowercase_found = True
    if character.isupper():
            uppercase_found = True
    if character.isdigit():
            numbers_found = True
    if not character.isalnum():
            special_character_found = True
if len(password) >= 8:
    count += 1
else:
    tips.append("Use at least 8 characters")
if len(password) >=12:
    count += 1
else:
     tips.append("Use at least 12 characters for better security")
if lowercase_found:
     count += 1
else:
    tips.append("Add a lowercase letter")
if uppercase_found:
    count += 1
else:
    tips.append("Add a uppercase letter")
if numbers_found:
    count += 1
else:
    tips.append("Add a number")
if special_character_found:
        count += 1
else:
    tips.append("Add a special character")
if len(password) < 8:
    print("Weak password")
elif count <= 4:
        print("Medium Password")
else:
        print("Strong Password")
if tips:
     print("Suggestions to improve your password:")
     for tip in tips:
          print("-", tip)
else:
     print("Good password! Use a unique password for every account")
    