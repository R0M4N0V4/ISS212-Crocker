"""
Program Name: patchcycle.py
Author: Emmylee Crocker
Date: February 10, 2025
Description: This script determines whether a given year is a 'Patch Year' or a 'Standard Year' based on a specific patch cycle.
Citation: Uses assignment example
"""

# Scenario 4: Patch Cycle Determination
# Prompt user to enter the year to check the patch cycle
year = int(input("Enter the year to check the patch cycle: "))

# Check if the year is within the managed patch period
if year < 2019:
    print("Not within the managed patch period.")
else:
    # Determine if it's a Patch Year or a Standard Year
    if year % 4 != 0:
        print("Standard Year")
    elif year % 100 != 0:
        print("Patch Year")
    elif year % 400 != 0:
        print("Standard Year")
    else:
        print("Patch Year")
