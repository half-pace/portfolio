#validation functions with prpoper docstrings and type hints, each returning a tuple of (bool, str) where bool indicates if the validation passed and str is an error message if it failed

def validate_age(age: int) -> bool | str:
    """
    Validates that the age is between 0 and 150.

    Args:
        age (int): The age to validate.

    Returns:
        (bool, str): A tuple where the first element is True if validation passed, False otherwise,
                     and the second element is an error message if validation failed.
    """
    if 0 <= age <= 120:
        return True, ""
    else:
        return False, "Age must be between 0 and 150."
    
def validate_email(email: str) -> bool | str:
    """
    Validates that the email is in a proper format.

    Args:
        email (str): The email to validate.
    Returns:        (bool, str): A tuple where the first element is True if validation passed, False otherwise,
                     and the second element is an error message if validation failed.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, ""
    else:
        return False, "Invalid email format." % email
    
def validate_password(password: str) -> bool | str:
    """
    Validates that the password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one digit.

    Args:
        password (str): The password to validate.
    Returns:        (bool, str): A tuple where the first element is True if validation passed, False otherwise,
                     and the second element is an error message if validation failed.
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter."
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."
    return True, ""


def validate_username(username: str) -> bool | str:
    """
    Validates that the username is between 3 and 20 characters long and contains only alphanumeric characters and underscores.

    Args:
        username (str): The username to validate.
    Returns:        (bool, str): A tuple where the first element is True if validation passed, False otherwise                   and the second element is an error message if validation failed.
    """ 
    import re
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    if re.match(pattern, username):
        return True, ""
    else:
        return False, "Username must be between 3 and 20 characters long and can only contain alphanumeric characters and underscores."
    
def main():
    #registration form taht uses all 4 and keeps asking until all inputs are valid
    while True:
        username = input("Enter username: ")
        valid, message = validate_username(username)
        if not valid:
            print(message)
            continue
        
        email = input("Enter email: ")
        valid, message = validate_email(email)
        if not valid:
            print(message)
            continue
        
        password = input("Enter password: ")
        valid, message = validate_password(password)
        if not valid:
            print(message)
            continue
        
        age = int(input("Enter age: "))
        valid, message = validate_age(age)
        if not valid:
            print(message)
            continue
        
        print("Registration successful!")
        break
    
if __name__ == "__main__":
    main()

