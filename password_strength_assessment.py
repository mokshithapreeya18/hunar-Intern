def assess_password_strength(password):
    length_criteria = len(password) >= 8
    longer_length_criteria = len(password) >= 12
    lowercase_criteria = any(char.islower() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    special_criteria = any(char in special_characters for char in password)

    criteria_met = sum([length_criteria, longer_length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria,
                        special_criteria])

    if criteria_met <= 2:
        return "Weak"
    elif 3 <= criteria_met <= 4:
        return "Okay"
    else:
        return "Strong"
def main():
    print("Enter passwords to evaluate their strength. Type 'exit' to stop.")
    while True:
        password = input("Enter passwords: ")
        if password.lower() == 'exit':
            break

        strength = assess_password_strength(password)
        print(f"The password '{password}' is {strength}.")


if __name__ == "__main__":
    main()
