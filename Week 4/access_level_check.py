"""
Author: Emmylee Crocker
Due Date: February 26, 2025
Python Script: Scenario 1 - User Privilege Level Check
Description: This script checks a user's privilege level based on their role.
Key Concepts: Variables & Input Handling, Conditional Statements, String Comparisons
Citation: Uses ISS 212 - Walkthrough example
"""

def check_privilege_level():
    """
    Function to check and display the user's privilege level 
    based on their role input.
    """
    # Prompt the user to enter their role
    # The input is stripped of any leading/trailing whitespace and converted to lowercase for consistency
    role = input("Enter your role (admin, user, guest): ").strip().lower()

    # Conditional statements to determine access level based on the entered role
    if role == "admin":
        # If the user is an admin, grant full privileges
        print("Access Level: Full privileges.")
    elif role == "user":
        # If the user is a regular user, grant limited privileges
        print("Access Level: Limited privileges.")
    elif role == "guest":
        # If the user is a guest, provide read-only access
        print("Access Level: Read-only access.")
    else:
        # Handle cases where the input does not match any valid role
        print("Invalid role entered. Please enter 'admin', 'user', or 'guest'.")

# The following block ensures that the function runs only when the script is executed directly,
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    check_privilege_level()
