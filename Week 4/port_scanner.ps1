# PowerShell Script: Scenario 6 - Port Scanner Simulation
# Author: Emmylee Crocker
# Due Date: February 26, 2025
# Description: This script simulates a simple port scanner.
# Key Concepts: Loops, Test-NetConnection, Handling User Input
# Citation: Adapted from ISS212 sample scripts, following provided citation guidelines.

# Prompt the user to enter the IP address to scan and store the input in the variable $ip
$ip = Read-Host "Enter IP Address"

# Define an array of common ports to scan: 
# 22 (SSH), 80 (HTTP), and 443 (HTTPS)
$ports = @(22, 80, 443)

# Iterate through each port in the $ports array
foreach ($port in $ports) {
    # Use Test-NetConnection to check if the port is open on the specified IP address
    # -ComputerName specifies the target IP
    # -Port specifies the port to test
    # -WarningAction SilentlyContinue suppresses warning messages for cleaner output
    $result = Test-NetConnection -ComputerName $ip -Port $port -WarningAction SilentlyContinue
    
    # Check if the TCP connection to the port was successful
    if ($result.TcpTestSucceeded) {
        # If successful, indicate that the port is OPEN
        Write-Host "Port ${port}: OPEN"
    } else {
        # If unsuccessful, indicate that the port is CLOSED
	Write-Host "Port ${port}: CLOSED"
    }
}
