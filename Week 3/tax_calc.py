"""
Program Name: tax_calc.py
Author: Emmylee Crocker
Date: February 10, 2025
Description: This script calculates the Data Security Tax (DST) based on data usage according to specified tax brackets.
Citation: Uses assignment example
"""

# Prompt user to enter annual data usage in MB
data_usage = float(input("Enter your annual data usage in MB: "))

# Calculate the tax based on data usage
if data_usage <= 85528:
    tax = (0.18 * data_usage) - 556.02
else:
    tax = 14839.02 + 0.32 * (data_usage - 85528)

# Ensure tax is not negative
tax = max(tax, 0)

# Print the calculated tax rounded to the nearest whole number
print(f"Your Data Security Tax is: {round(tax)} MB")
