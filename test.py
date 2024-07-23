#Please open the code in Python IDLE or Windows Powershell for proper functioning

import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = special_count = 0

    # Check password length and adjust strength accordingly
    length_bonus = 0
    if len(password) >= 8:
        length_bonus = 1
        strength += 1  # Award 1 point for meeting minimum length
        remarks += "Length is good (at least 8 characters).\n"

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        else:
            special_count += 1

    # Calculate strength based on character types (excluding whitespaces)
    strength += lower_count >= 1
    strength += upper_count >= 1
    strength += num_count >= 1
    strength += special_count >= 1

    # Modify strength and remarks based on combined score (adjusted for no whitespaces)
    if strength == 1 + length_bonus:
        remarks = "Very Weak Password!!! Change ASAP\n"
    elif strength == 2 + length_bonus:
        remarks = "Weak Password!!! Change ASAP\n"
    elif strength == 3 + length_bonus:
        remarks = "It's a medium password, consider strengthening\n"
    elif strength == 4 + length_bonus:
        remarks = "It's a strong password\n"
    elif strength == 5 + length_bonus:
        remarks = "A very strong password\n"

    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    # Removed line for whitespace characters
    print(f"{special_count} special characters")

    print(f"Password Strength: {strength} ({strength - length_bonus} excluding length bonus)")  # Show both total and length-independent strength
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input('Do you want to enter another pwd (y/n): ')
    else:
        choice = input('Do you want to check pwd (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    print('+++ welcome to PWD checker +++')
    ask_pw = ask_pwd()
    while ask_pw:  # Loop as long as user wants to check another password
        check_pwd()
        ask_pw = ask_pw(True)
