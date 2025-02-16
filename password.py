"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Muniver Kaur Kharod
******************************
This file is used to calculate the strength of a password based on the
number of character groups it contains and its length. It includes a helper
function to count the character groups and a main function to compute the password
strength using these group counts and the password's length. The strength is returned
as an integer between 0 and 5.
"""
#Function to count the number of character groups in a password
#It checks for lowercase letters, uppercase letters, digits, and symbols in the password
def count_groups(pwd):

    #Define the groups of characters: lowercase, uppercase, digits, and symbols
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*/?-+=,.|~ "

    # Initialize flags to check if the password contains each type of character group
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    # Loop through each character in the password to check which groups it belongs to
    for char in pwd:
        if char in lowercase:
            has_lower = True # If character is lowercase, mark has_lower as True
        elif char in uppercase:
            has_upper = True # If character is uppercase, mark has_upper as True
        elif char in digits:
            has_digit = True # If character is a digit, mark has_digit as True
        elif char in symbols:
            has_symbol = True # If character is a symbol, mark has_symbol as True

    # The number of character groups is the sum of how many group flags are True
    num_groups = has_lower + has_upper + has_digit + has_symbol
    return num_groups

# Function to calculate the strength of a password
# The strength is based on the length of the password and the number of character groups used
def password_strength(pwd):

    # Check for invalid characters (spaces, tabs, newlines) and return strength of 0 if found
    if ' ' in pwd or '\n' in pwd or '\t' in pwd:
        return 0

    # Count the number of character groups using the helper function
    num_groups = count_groups(pwd)
    # Get the length of the password
    length = len(pwd)

    # Check the length and the number of groups to determine the password strength
    if length < 5:
        return 0 # Passwords shorter than 5 characters get a strength of 0
    elif 5 <= length <= 8:
        # Passwords between 5 and 8 characters
        if num_groups == 0 or num_groups == 1:
            return 1 # Weak if there are 0 or 1 groups
        elif num_groups == 2 or num_groups == 3:
            return 2 # Medium strength if there are 2 or 3 groups
        else:
            return 3 # Strong if all 4 groups are used
    elif 9 <= length <= 12:
        # Passwords between 9 and 12 characters
        if num_groups == 2 or num_groups ==1:
            return 2 # Weak if there is only 1 group
        elif num_groups == 2 or num_groups == 3:
            return 3 # Medium if there are 2 or 3 groups
        else:
            return 4 # Strong if all 4 groups are used
    elif length > 12:
        # Passwords longer than 12 characters
        if num_groups == 0 or num_groups == 1:
            return 3 # Weak if there are 0 or 1 groups
        elif num_groups == 2 or num_groups == 3:
            return 4  # Medium if there are 2 or 3 groups
        else:
            return 5  # Very strong if all 4 groups are used
