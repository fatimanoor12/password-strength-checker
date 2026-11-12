# Password Strength Checker

This is a beginner-friendly Python program that checks the strength of a password.

It tells the user whether a password is **weak, medium, or strong**. It also gives simple suggestions to make the password better.

## What the program checks

The program checks whether a password has:

- At least 8 characters
- At least 12 characters for better security
- At least one lowercase letter (a–z)
- At least one uppercase letter (A–Z)
- At least one number (0–9)
- At least one special character, such as `!`, `@`, `#`, or `$`

## How it works

1. The program asks the user to enter a password.
2. It checks every character in the password using a `for` loop.
3. It uses Boolean flags to remember whether the password has:
   - A lowercase letter
   - An uppercase letter
   - A number
   - A special character
4. It increases a `count` for every security condition the password meets.
5. If a condition is missing, the program adds a suggestion to the `tips` list.
6. Finally, it shows the password strength and improvement suggestions.

## Password strength rules

| Condition | Result |
|---|---|
| Password has fewer than 8 characters | Weak password |
| Password has 8 or more characters but meets 4 or fewer conditions | Medium password |
| Password meets more than 4 conditions | Strong password |

## Example

If the user enters:

```text
abc
```

The program will show:

```text
Weak password
Suggestions to improve your password:
- Use at least 8 characters
- Use at least 12 characters for better security
- Add a uppercase letter
- Add a number
- Add a special character
```

## Concepts used

This project uses basic Python concepts:

- `input()` to take user input
- `for` loop to check each character
- `if`, `elif`, and `else` statements
- Boolean variables, such as `lowercase_found`
- Lists and `append()` to store suggestions
- String methods: `islower()`, `isupper()`, `isdigit()`, and `isalnum()`
- `len()` to check password length

## How to run

1. Install Python on your computer.
2. Save the file as `password_checker.py`.
3. Open a terminal or command prompt.
4. Run this command:

```bash
python password_checker.py
```

5. Enter a password when the program asks.

## Screenshots

### Weak password example

![Weak password example](screenshots/weak_password.png)

### Medium password example

![Medium password example](screenshots/medium_password.png)

### Strong password example

![Strong password example](screenshots/strong_password.png)

## Important security note

A strong password should be long and unique. Do not use the same password for many accounts.

For better security, use a long password or passphrase and enable two-factor authentication (2FA) when it is available.

## Future improvements

- Add a Streamlit web interface
- Improve the password strength rules
- Add more detailed suggestions

## License

This project is for learning and portfolio purposes.
You may not copy, reuse, modify, distribute, or claim this code as your own without my written permission.
