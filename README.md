# Password Strength Assessment Tool

A Python-based cybersecurity project that evaluates password strength based on length, character variety, common patterns, repeated characters, sequential patterns, and estimated entropy.

## Features

- Scores passwords from 0 to 7
- Rates passwords from Very Weak to Very Strong
- Checks for uppercase and lowercase letters
- Checks for numbers and special characters
- Detects common password patterns
- Detects repeated characters
- Detects simple sequences such as `123`, `abc`, and `qwerty`
- Estimates password entropy
- Provides improvement recommendations
- Hides password input while typing
- Does not save or store passwords

## Technologies Used

- Python
- Regular expressions
- `getpass`
- `math`
- `string`

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in a terminal.
3. Run:

```bash
python password_checker.py
```

4. Enter a fake test password.

## Example Output

```text
Strength: Very Weak
Score: 0/7
Estimated entropy: 56.87 bits

Recommendations:
- Use at least 12 characters.
- Add at least one uppercase letter.
- Add at least one special character.
- Avoid common words or predictable password patterns.
- Avoid simple sequences such as 123, abc, or qwerty.
```

## Project Structure

```text
password-strength-checker/
├── password_checker.py
├── README.md
└── screenshots/
    ├── weak-result.png
    └── strong-result.png
```

## What I Learned

- Password security principles
- Python input validation
- Regular expressions
- Modular programming
- Entropy estimation
- Secure handling of sensitive input
- Rule-based security scoring

## Security Notice

This project is for educational purposes. Use fake passwords when testing. Never enter or upload a password that you use for a real account.