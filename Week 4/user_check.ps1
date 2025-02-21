# PowerShell Script: Scenario 4 - User Account Type Checker
# Author: Emmylee Crocker
# Due Date: February 26, 2025
# Description: This script identifies whether the current user is an administrator.
# Key Concepts: User Privileges, Conditional Checks, Output Formatting
# Citation: Adapted from ISS212 sample scripts, following provided citation guidelines.

# Check if the current user belongs to the Administrators group by verifying the group SID "S-1-5-32-544"
# The SID "S-1-5-32-544" corresponds to the built-in Administrators group in Windows
if (([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups -contains "S-1-5-32-544") {
    # If the user is part of the Administrators group, display confirmation of admin privileges
    Write-Host "Administrator Privileges: Yes"
} else {
    # If the user is NOT part of the Administrators group, indicate that admin privileges are not available
    Write-Host "Administrator Privileges: No"
}
