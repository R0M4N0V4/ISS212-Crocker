'''
JMoody  
Commented By: Emmylee Crocker  
ISS 212  
4.2025 Wk 12 Tool Development 8 - reg1.py  
NOTE: Use command: python reg1.py SOFTWARE  
Remember to run in Windows Command Prompt  
'''

import sys      # Used to get command-line arguments (e.g., hive file path)
import winreg   # Built-in module to access and manipulate Windows registry

try:
    # Connect to the HKEY_LOCAL_MACHINE registry hive
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    # Get the registry key path from command-line argument (e.g., "SOFTWARE")
    key_path = sys.argv[1]

    # Open the specified registry key
    key = winreg.OpenKey(reg, key_path)

    print(f"Analyzing {key_path} in Windows registry...")

    # Get the last modified time of the key
    last_modified = winreg.QueryInfoKey(key)[2]
    print(f"Last modified: {last_modified} [UTC]")

    try:
        # Loop through all subkeys under the main key
        for i in range(winreg.QueryInfoKey(key)[1]):
            subkey_name = winreg.EnumKey(key, i)  # Get the name of the subkey
            print("Subkey:", subkey_name)

            # Open the subkey for reading its values
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                j = 0
                # Loop through all values in the subkey
                while True:
                    try:
                        # Get name and data for each registry value
                        value_name, value_data, _ = winreg.EnumValue(subkey, j)
                        print(f"Name: {value_name}, Value path: {value_data}")
                        j += 1
                    except OSError as e:
                        # Error code 259 means "no more data"
                        if e.errno == 259:
                            break
                        else:
                            raise
            except OSError:
                pass  # If we can't read the values, skip to the next subkey
            print("\n")

    # Handle case where no more subkeys are found
    except OSError as e:
        if e.errno == 259:
            pass
        else:
            raise

# Handle errors if the key path doesn't exist
except FileNotFoundError as e:
    print("Registry key not found:", e)

# Handle errors if user lacks permission to access the key
except PermissionError as e:
    print("Permission error:", e)

# Catch any other unexpected errors
except Exception as e:
    print("An error occurred:", e)
