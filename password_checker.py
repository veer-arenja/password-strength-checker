import math
import re
import string
from getpass import getpass


COMMON_PATTERNS = [
    "password",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "123456",
    "abcdef",
]


def estimate_entropy(password: str) -> float:
    """Estimate password entropy based on the character types used."""
    character_pool = 0

    if re.search(r"[a-z]", password):
        character_pool += 26

    if re.search(r"[A-Z]", password):
        character_pool += 26

    if re.search(r"\d", password):
        character_pool += 10

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        character_pool += len(string.punctuation)

    if character_pool == 0:
        return 0.0

    return len(password) * math.log2(character_pool)


def has_repeated_characters(password: str) -> bool:
    """Return True when the same character appears three times in a row."""
    return bool(re.search(r"(.)\1\1", password))


def has_sequential_pattern(password: str) -> bool:
    """Detect a few common alphabetical and numerical sequences."""
    sequences = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "abc",
        "bcd",
        "cde",
        "qwerty",
    ]

    lowered_password = password.lower()

    return any(sequence in lowered_password for sequence in sequences)


def assess_password(password: str) -> dict:
    """Analyse a password and return its score, rating and feedback."""
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters.")
    else:
        feedback.append("The password is too short. Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    lowered_password = password.lower()

    if any(pattern in lowered_password for pattern in COMMON_PATTERNS):
        score -= 2
        feedback.append("Avoid common words or predictable password patterns.")

    if has_repeated_characters(password):
        score -= 1
        feedback.append("Avoid repeating the same character three or more times.")

    if has_sequential_pattern(password):
        score -= 1
        feedback.append("Avoid simple sequences such as 123, abc or qwerty.")

    entropy = estimate_entropy(password)

    if entropy >= 70:
        score += 1
    elif entropy < 40:
        feedback.append("Use a longer and less predictable combination of characters.")

    score = max(0, min(score, 7))

    if score <= 2:
        rating = "Very Weak"
    elif score <= 4:
        rating = "Weak"
    elif score == 5:
        rating = "Moderate"
    elif score == 6:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "score": score,
        "rating": rating,
        "entropy": round(entropy, 2),
        "feedback": feedback,
    }


def main() -> None:
    print("=" * 45)
    print("PASSWORD STRENGTH ASSESSMENT TOOL")
    print("=" * 45)

    password = getpass("Enter a test password: ")

    if not password:
        print("\nError: Password cannot be empty.")
        return

    result = assess_password(password)

    print("\nAssessment Results")
    print("-" * 45)
    print(f"Strength: {result['rating']}")
    print(f"Score: {result['score']}/7")
    print(f"Estimated entropy: {result['entropy']} bits")

    if result["feedback"]:
        print("\nRecommendations:")

        for recommendation in result["feedback"]:
            print(f"- {recommendation}")
    else:
        print("\nNo major weaknesses were detected.")

    print("\nSecurity note: The password was not saved.")


if __name__ == "__main__":
    main()