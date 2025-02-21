"""
Author: Emmylee Crocker
Due Date: February 26, 2025
Python Script: Scenario 1 - User Privilege Level Check
Description: This script checks a user's privilege level based on their role.
Key Concepts: Variables & Input Handling, Conditional Statements, String Comparisons
Citation: Uses ISS 212 - Walkthrough example
"""

def check_privilege_level():
    # Prompt the user to enter their role
    role = input("Enter your role (admin, user, guest): ").strip().lower()

    # Determine access level based on the role
    if role == "admin":
        print("Access Level: Full privileges.")
    elif role == "user":
        print("Access Level: Limited privileges.")
    elif role == "guest":
        print("Access Level: Read-only access.")
    else:
        print("Invalid role entered. Please enter 'admin', 'user', or 'guest'.")

# Execute the function if the script is run directly
if __name__ == "__main__":
    check_privilege_level()
