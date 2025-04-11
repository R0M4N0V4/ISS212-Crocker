'''
JMoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use Command: python reg3.py SYSTEM
'''

import winreg  # Allows access to Windows Registry
import sys     # Used to interact with command-line arguments (not used in this script but imported)

# This function identifies which ControlSet is currently active on the system
def getCurrentControlSet():
    try:
        hkey_local_machine = winreg.HKEY_LOCAL_MACHINE
        select_subkey = "SYSTEM\\Select"

        # Open the SYSTEM\Select key to find out the current ControlSet
        with winreg.OpenKey(hkey_local_machine, select_subkey) as key:
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                value_name, value_data, _ = winreg.EnumValue(key, i)
                if value_name == "Current":
                    return value_data  # This returns a number like 1 or 2 (ControlSet001, etc.)
    except FileNotFoundError as exception:
        print("Couldn't find SYSTEM\\Select key ", exception)

# This function prints the details of a service in a readable format
def getServiceInfo(dictionary):
    # Human-readable descriptions for service types
    serviceType = {
        1: "Kernel device driver", 
        2: "File system driver", 
        4: "Arguments for an adapter",
        8: "File system driver interpreter", 
        16: "Own process", 
        32: "Share process",
        272: "Independent interactive program", 
        288: "Shared interactive program"
    }

    print(" Service name: %s" % dictionary["SERVICE_NAME"])
    
    if "DisplayName" in dictionary:
        print(" Display name: %s" % dictionary["DisplayName"])

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType.get(dictionary["Type"], "Unknown"))

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")

# This function gathers all values under a specific service subkey
def serviceParams(subkey):
    service = {}
    service["SERVICE_NAME"] = subkey  # Name of the service
    service["ModifiedTime"] = winreg.QueryInfoKey(subkey)[2]  # Last modification time

    try:
        # Loop through all values in the subkey
        for i in range(0, winreg.QueryInfoKey(subkey)[1]):
            value_name, value_data, _ = winreg.EnumValue(subkey, i)
            service[value_name] = value_data
    except OSError as exception:
        print("Error accessing registry subkey ", exception)

    # Print service info in readable form
    getServiceInfo(service)

# This function opens the Services registry key and loops through all services listed
def servicesKey(controlset):
    serviceskey = "SYSTEM\\ControlSet00%d\\Services" % controlset  # Build key path like SYSTEM\ControlSet001\Services
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, serviceskey) as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)  # Get each service name
                subkey = winreg.OpenKey(key, subkey_name)  # Open each service subkey
                serviceParams(subkey)  # Process and print values
    except FileNotFoundError as exception:
        print("Couldn't find Services key ", exception)

# Entry point of the script
if __name__ == "__main__":
    controlset = getCurrentControlSet()  # Get the active control set number
    if controlset is not None:
        servicesKey(controlset)  # Start reading service entries from that control set
