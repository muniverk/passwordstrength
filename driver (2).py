"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Muniver Kaur Kharod
******************************
This file is used to run the password strength checking program by prompting the user
for a minimum strength value and calling the process_password function from the login.py file.
The program will continuously ask the user for a password until the entered or generated password
meets the required strength.
"""

# Import the process_password function from login.py
from login import *

# Ask the user for a minimum password strength
# This is the value that the password must meet or exceed in order to be accepted
min_str = int(input("Enter a minimum strength: "))

# Call the function to process password creation or generation
# The process will continue until a strong enough password is entered
process_password(min_str)
