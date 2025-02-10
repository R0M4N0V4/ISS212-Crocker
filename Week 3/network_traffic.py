"""
Program Name: network_traffic.py
Author: Emmylee Crocker  
Date: February 10, 2025
Description: This script analyzes network packet size and checks if the size meets the threshold for further inspection.
Citation: Uses assignment example""" 

# Prompt user to enter packet size in bytes
packet_size = int(input("Enter the packet size in bytes: "))

# Print False if packet size is less than 1337 bytes, and True if it is 2600 bytes or more
print(packet_size >= 2600)
