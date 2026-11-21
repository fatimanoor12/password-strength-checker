# Password Strength Checker (v2)

A small command-line Python program that rates a password as **Weak, Medium or Strong** and gives suggestions to improve it.

This is a beginner project. I built it while learning Python, and I used AI tools to help me with explanations and debugging. This version improves on v1 by adding an entropy estimate and a common-password check.

## What it does

When you enter a password, the program:

1. Checks the password character by character (lowercase, uppercase, number, special character).
2. Checks length (at least 8 and at least 12 characters).
3. Prints a **theoretical entropy estimate** in bits.
4. Compares the lowercase version of the password against a small built-in list of common passwords.
5. Prints a rating and a list of suggestions.

## How the rating works
| Situation | Result |
|---|---|
| The lowercase password is in the built-in common-password list | Weak |
| The password is empty | Weak |
| The password is shorter than 8 characters | Weak |
| The password meets all 6 checks (8+ characters, 12+ characters, lowercase, uppercase, number, special character) | Strong |
| Anything else | Medium |

The entropy number is printed for information only. It does **not** change the rating.
## Example runs
Common password (caught even with different capital letters):

```text
Enter the password: PASSWORD
Entropy (theoretical, assumes random choice): 37.6 bits
Warning: This password is easily detectable.
Password Strength: Weak
Suggestions to improve your password:
- Use at least 12 characters for better security
- Add a lowercase letter
- Add a number
- Add a special character
```

Medium password:

```text
Enter the password: correcthorsebatterystaple
Entropy (theoretical, assumes random choice): 117.51 bits
Not found in my small list of common passwords.
Password Strength: Medium
Suggestions to improve your password:
- Add an uppercase letter
- Add a number
- Add a special character
```

Strong password:

```text
Enter the password: Summer2024!!
Entropy (theoretical, assumes random choice): 78.66 bits
Not found in my small list of common passwords.
Password Strength: Strong
This password meets this checker's basic rules
Use a unique password for every account.
```

## Known limitations

This tool is a learning project and is **not** a reliable way to judge real password security. Known problems:

- **Small common-password list.** It only checks a short list of common passwords. A password like `password123` or `p@ssw0rd2024` is not in the list, so it is not caught.
- **Predictable patterns score as Strong.** `Summer2024!!` is rated Strong because it meets all the rules, but a word, a year and symbols is a very predictable pattern.
- **Long passphrases can score only Medium.** `correcthorsebatterystaple` is long and hard to guess, but it has only lowercase letters, so the rules rate it Medium.
- **Entropy is a theoretical maximum.** The formula assumes every character was chosen randomly. People do not choose passwords randomly, so the number overestimates real strength.
- **No pattern checks.** It does not look for repeated characters, keyboard patterns (like `qwerty`) or sequences (like `abcd` or `1234`), except for the few that are in the list.
- **Passwords in other scripts.** Letters from scripts like Urdu are not counted as lowercase or uppercase, so the suggestions can be wrong for them.
- **The password is visible when typed.** The program uses `input()`, so the password shows on screen.
- **Not a security tool.** It checks only the password text. It cannot tell whether a password has appeared in a data breach.

## How to run

1. Install Python 3.
2. Download `password_strength_checker_v2.py`.
3. Open a terminal in the folder with the file.
4. Run:

```bash
python password_strength_checker_v2.py
```

5. Type a password when asked.

The program does not store or send the password anywhere. It only reads it and prints a result.

## Concepts used

- `input()`, `print()` and `len()`
- `for` loops and `if` / `elif` / `else`
- Boolean variables and a counter
- Lists and `append()`
- String methods: `islower()`, `isupper()`, `isdigit()`, `isalnum()`, `lower()`
- `math.log2()` for the entropy estimate

## Future improvements

Things I plan to learn and add:

- Use `getpass` so the password is not shown on screen
- Put the checks into functions and write simple tests
- Load a larger common-password list from a file
- Catch simple tricks such as `@` for `a` and trailing numbers
- Check for repeated characters and sequences

## Version history

- **v1:** length and character-type checks, with weak / medium / strong rating.
- **v2:** added entropy estimate, common-password check (case-insensitive), clearer tips and a limitations section.