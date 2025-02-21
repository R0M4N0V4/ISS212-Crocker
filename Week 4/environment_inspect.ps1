# PowerShell Script: Scenario 5 - Environment Variable Inspector
# Author: Emmylee Crocker
# Due Date: February 26, 2025
# Description: This script lists common environment variables.
# Key Concepts: Environment Variables, String Formatting, Output Customization
# Citation: Adapted from ISS212 sample scripts, following provided citation guidelines.

# Display the current username from the environment variable $env:USERNAME
Write-Host "Username: $env:USERNAME"

# Display the domain name associated with the user account from $env:USERDOMAIN
Write-Host "User Domain: $env:USERDOMAIN"

# Display the computer's name from the environment variable $env:COMPUTERNAME
Write-Host "Computer Name: $env:COMPUTERNAME"

# Display the system's PATH variable ($env:Path), which contains directories for executable files
Write-Host "System Path: $env:Path"
