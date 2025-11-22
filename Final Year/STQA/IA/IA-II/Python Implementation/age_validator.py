# age_validator.py

def check_age(age):
    """
    Validates if a user's age is between 18 and 60, inclusive.
    Returns:
        True: if age is valid
        False: if age is invalid (too young or too old)
    """
    if 18 <= age <= 60:
        return True
    else:
        return False