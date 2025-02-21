# PowerShell Script: Scenario 3 - Execution Policy Check
# Author: Emmylee Crocker
# Due Date: February 26, 2025
# Description: This script checks and reports the system's execution policy.
# Key Concepts: Execution Policies, Conditional Logic, Secure Scripting Awareness
# Citation: Adapted from ISS212 sample scripts, following provided citation guidelines.

# Display the current execution policy using Get-ExecutionPolicy
# Write-Host outputs the policy directly to the console
Write-Host "Current Execution Policy: $(Get-ExecutionPolicy)"

# Check if the current execution policy is either 'Unrestricted' or 'Bypass'
# These policies allow scripts to run without restrictions, which can pose security risks
if ((Get-ExecutionPolicy) -in "Unrestricted", "Bypass") {
    # Warn the user if the execution policy is set to a less secure mode
    Write-Host "WARNING: Your execution policy allows all scripts to run. Ensure you trust the source."

# Check if the execution policy is 'Restricted'
# The 'Restricted' policy prevents any script from running, offering maximum security
} elseif ((Get-ExecutionPolicy) -eq "Restricted") {
    # Inform the user that no scripts can be executed under this policy
    Write-Host "Scripts cannot be executed on this system."
}
