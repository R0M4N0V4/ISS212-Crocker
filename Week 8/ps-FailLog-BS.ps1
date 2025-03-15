# Emmylee Crocker - March 15, 2025
# ISS 212 CS Scripting - WK 8 TD 6- PowerShell - Event Log Monitoring
# PS script using Regex -- Redacting data using pattern matching
# Citation - Uses ISS 212 Walkthrough material

'''
.DESCRIPTION
Emmylee Crocker - March 15, 2025
ISS 212 - CS Scripting - PowerShell Script: ps-FailLog.ps1
Citations: Uses ISS 212 Walkthrough material

.PURPOSE
Week 8 PS script using Regex to match IP data using regex.

.USAGE
Run script from file with command or from terminal. | .\ps-FailLog.ps1
'''

# Week 8 PS script using Regex -- extracting data using regex

# Load log file and find failed login attempts
$logFile = "security.log"
$failedAttempts = Select-String -Path $logFile -Pattern "Login attempt failed from IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" -AllMatches

# Extract IP addresses and count occurrences
$ipCounts = @{}
foreach ($match in $failedAttempts) {
    $ip = $match.Matches.Groups[1].Value
    if ($ipCounts.ContainsKey($ip)) {
        $ipCounts[$ip] += 1
    } else {
        $ipCounts[$ip] = 1
    }
}

# Display IPs with more than 3 failed attempts
Write-Host "Potentially Malicious IPs:"
foreach ($ip in $ipCounts.Keys) {
    if ($ipCounts[$ip] -gt 3) {
        Write-Host "$ip has $($ipCounts[$ip]) failed login attempts"
    }
}
