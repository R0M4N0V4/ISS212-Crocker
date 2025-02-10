"""
Program Name: protocol_love.py
Author: Emmylee Crocker
Date: February 10, 2025
Description: This script checks for the correct protocol name input and provides different responses based on the input.
Citation: Uses assignment example
"""

# Scenario 2: Protocol Love
# Prompt user to enter the protocol name
protocol_name = input("Enter the protocol name: ")

# Conditional logic to handle the protocol name input
if protocol_name == "Cyphersec":
    print("Cyphersec is the only supported protocol!")
elif protocol_name == "cybersec":
    print("DENIED. Cyphersec protocol ONLY!")
else:
    print(f"Cyphersec! Not {protocol_name}!")
