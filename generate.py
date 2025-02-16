"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Muniver Kaur Kharod
******************************
This file is used to randomly generate a password of a specified length.
The password consists of randomly selected characters from four character groups:
lowercase letters, uppercase letters, digits, and symbols. The password is constructed one character at a time
and returned to the calling function.
"""
# Importing the random module to generate random characters for the password
import random

# Function to generate a random password of a given length
# The password will contain random characters from the four character groups: lowercase, uppercase, digits, and symbols
def generate_password(length):
    # Define the groups of characters: lowercase, uppercase, digits, and symbols
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@$%^&*()/?=-+,.|~"

    # Combine all character groups into one string
    all_chars = lowercase + uppercase + digits + symbols

    # Create an empty string to build the password
    # Use a loop to select random characters from all_chars for the desired length of the password
    password = "".join(random.choice(all_chars) for _ in range(length))

    # Return the generated password as the final result
    return password
