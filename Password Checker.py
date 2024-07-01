import string

# Function to assess password strength
def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    # Evaluate strength based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_criteria:
        return "Very Strong"
    elif length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria:
        return "Strong"
    elif length_criteria and uppercase_criteria and lowercase_criteria:
        return "Moderate"
    elif length_criteria and lowercase_criteria and digit_criteria:
        return "Moderate"
    elif length_criteria and uppercase_criteria and digit_criteria:
        return "Moderate"
    elif length_criteria and special_criteria:
        return "Moderate"
    elif length_criteria and lowercase_criteria:
        return "Weak"
    else:
        return "Very Weak"

# Main function for interactive usage
def main():
    print("Password Strength Evaluator")
    print("Criteria:")
    print("- At least 8 characters long")
    print("- Contains uppercase and lowercase letters")
    print("- Contains numbers")
    print("- Contains special characters")

    while True:
        password = input("\nEnter a password to assess (or 'quit' to exit): ")

        if password.lower() == 'quit':
            break

        strength = assess_password_strength(password)
        print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
