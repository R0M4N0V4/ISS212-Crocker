'''
JMoody  
Commented By: Emmylee Crocker  
ISS 212  
4.2025 Wk 12 Tool Development 8 - reg2.py  
NOTE: Use command: python reg2.py SOFTWARE  
'''

import sys  # Allows the script to accept command-line arguments
from regipy.registry import RegistryHive  # Import RegistryHive from the regipy library

try:
    # Get the registry hive file path from the command-line argument
    hive_path = sys.argv[1]

    # Load the hive using regipy's RegistryHive class
    reg = RegistryHive(hive_path)

    print(f"Analyzing {hive_path}...")

    # Access the specific subkey where Windows version info is stored
    software_key = reg.get_key(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    # If the subkey exists, extract key information
    if software_key:
        print("\tProduct name:", software_key.get_value("ProductName"))
        print("\tCurrentVersion:", software_key.get_value("CurrentVersion"))
        print("\tServicePack:", software_key.get_value("CSDVersion"))
        print("\tProductID:", software_key.get_value("ProductId"))

    else:
        # Print message if the subkey doesn't exist in the hive
        print("Subkey 'CurrentVersion' not found in the provided registry file.")

# Handle case where the hive file cannot be found
except FileNotFoundError as exception:
    print(f"Registry hive file not found: {exception}")

# Handle other unexpected errors
except Exception as exception:
    print(f"An error occurred: {exception}")
