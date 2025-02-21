#!/bin/bash
# Author: Emmylee Crocker
# Due Date: February 26, 2025
# Bash Script: Scenario 2 - System Health Check
# Description: This script performs a basic system health check.
# Key Concepts: Variables, Command Execution, Echo Statements for Output Formatting, Functions
# Citation: Date conversion information gained from https://www.baeldung.com/linux/convert-timestamps-column-date  
#           Also used ISS212 example code as a starting point. 

# Function: Check if wmic is available, since runing again windows machine
check_wmic() {
    # Returns 0 (success) if wmic is available, 1 (failure) otherwise
    if command -v wmic &> /dev/null; then
        return 0
    else
        return 1
    fi
}

echo "======================="
echo "   System Health Check"
echo "======================="

# System Uptime
echo -e "\nSystem Uptime:"
if check_wmic; then
    BOOT_TIME=$(wmic os get lastbootuptime | awk 'NR==2 {print $1}')
    # Format: YYYYMMDDHHMMSS -> YYYY-MM-DD HH:MM:SS
    FORMATTED_BOOT_TIME=$(echo $BOOT_TIME | sed -E 's/([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2}).*/\1-\2-\3 \4:\5:\6/')
    echo "Last Boot Time: $FORMATTED_BOOT_TIME"
else
    echo "Uptime information not available."
fi

# Available Disk Space
echo -e "\nAvailable Disk Space:"
if command -v df &> /dev/null; then
    df -h /c 2>/dev/null || echo "Disk space information not available."
else
    echo "Disk space information not available."
fi

# Available RAM
echo -e "\nAvailable RAM:"
if check_wmic; then
    # Get free RAM in KB, convert to MB
    wmic OS get FreePhysicalMemory | awk 'NR==2 {printf "%.2f MB free\n", $1/1024}'
else
    echo "RAM information not available."
fi

# CPU Load Percentage
echo -e "\nCPU Load Percentage:"
if check_wmic; then
    wmic cpu get loadpercentage | awk 'NR==2 {print $1 "%"}'
else
    echo "CPU load information not available."
fi

echo "======================="
