# Emmylee Crocker - March 15, 2025
# ISS 212 CS Scripting - WK 8 TD 6- Python Suspicious IP Address Extraction
# Bash script using Regex -- Redacting data using pattern matching
# Citation - Uses ISS 212 Walthrough material

import re

# Load the log file
with open('auth.log', 'r') as file:
	log_data = file.read()

# Regex pattern for failed login IP addresses
pattern = r"Failed password .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# Find all matching IP addresses
suspicious_ips = re.findall(pattern, log_data)

# Get unique IP addresses and display them
unique_ips = set(suspicious_ips)
print("Suspicious IP addresses:")
for ip in unique_ips:
	print(ip)
