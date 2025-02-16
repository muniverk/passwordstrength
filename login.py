"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Muniver Kaur Kharod
Student ID: mkharod2
File created: October 20, 2024
******************************
This file prompts the user to create a new password or generate a random one. It checks the password strength using functions
from the password.py and generate.py files. The program continues to prompt the user until a password meeting the minimum
strength requirement is provided. It displays messages based on the password's strength and the user's input.
"""

# Import functions from the password.py and generate.py files
from password import *
from generate import *

# Function to process the creation of a new password
# It asks the user for a password and checks its strength, repeating until the password meets the minimum strength
def process_password(min_strength):
    # Loop continuously until a strong enough password is created or generated
    while True:

         # Prompt the user to either input a new password or type 'X' to generate a random password
        user_input = input("Enter a new password or type 'X' for a random password:")

        # Check if the user entered 'X' (or 'x') to generate a random password
        if user_input.lower() == 'x':
            # Generate a random password of length 15
            password = generate_password(15)
            # Calculate the strength of the generated password
            strength = password_strength(password)
            # Display the generated password and its strength
            print(f"Generated password: {password}, Strength:{strength}")
        else:
            # If the user typed a password, calculate its strength
            password = user_input
            strength = password_strength(password)
            # Display the entered password and its strength
            print(f"Entered password: {password}, Strength: {strength}")

        # Check if the password strength meets the minimum required strength
        if strength >= min_strength:
            # If strong enough, print a success message and break the loop
            print("Password is strong enough.")
            break
        else:
            # If not strong enough, prompt the user to try again
            print("Password is not strong enough. Try again")