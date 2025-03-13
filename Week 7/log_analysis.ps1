# Log Analysis PowerShell Script
# Author: Emmylee Crocker
# Date: March 13, 2025
# Description: This script processes log files to analyze severity levels, extract failed authentication attempts, and filter logs by date.
# Resources: ISS212 Week 7 Tool Development Exercise 4 Sample Script


# Define the log file path
$logFilePath = "WK7LOG.txt"

# Check if the log file exists
if (-Not (Test-Path $logFilePath)) {
    Write-Host "Log file not found! Exiting script."
    exit
}

# Read log entries
$logEntries = Get-Content $logFilePath

# Initialize data structures
$logStats = @{}
$failedLogins = @()

# Process log entries
foreach ($entry in $logEntries) {
    # Use regex to extract log details
    if ($entry -match "^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (.*)$") {
        $timestamp = $matches[1]
        $logLevel = $matches[2]
        $ipAddress = $matches[3]
        $message = $matches[4]

        # Count log levels
        if ($logStats.ContainsKey($logLevel)) {
            $logStats[$logLevel]++
        } else {
            $logStats[$logLevel] = 1
        }

        # Detect failed authentication attempts
        if ($message -like "*failed authentication*") {
            $failedLogins += "$timestamp | $ipAddress | $message"
        }
    }
}

# Display log level breakdown
Write-Host "Log Level Breakdown:"
$logStats.GetEnumerator() | ForEach-Object { Write-Host "$($_.Key): $($_.Value)" }

# Display first 10 failed login attempts
Write-Host "`nFirst 10 Failed Login Attempts:"
$failedLogins | Select-Object -First 10
