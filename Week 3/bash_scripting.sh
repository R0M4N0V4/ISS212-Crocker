#!/bin/bash
#Program name: bash_scripting.sh
#Author: Emmylee Crocker
#Date: February 10, 2025
#Description: This Bash script handles user input for packet size, protocol name, data usage, and year, following the given logic and specifications.
#Citiation: Follows the assignment examples

# Block 1: Network Traffic Analysis
network_traffic_analysis() {
    # Prompting user to input packet size in bytes
    read -p "Enter the packet size in bytes: " packet_size
	# Check if the packet size is greater than or equal to 100 bytes
    if [ "$packet_size" -ge 100 ]; then
        echo "True - Packet meets the threshold for analysis."
    else
        echo "False - Packet is too small to analyze."
    fi
}

# Block 2: Protocol Identification
protocol_identification() {
    # Prompt the user to input the protocol name
    read -p "Enter the protocol name: " protocol_name
    # Check if the protocol name is exactly "Cyphersec"
    if [ "$protocol_name" == "Cyphersec" ]; then
        echo "Yes - Cyphersec is the best protocol ever!"
    # Check if the protocol name is exactly "Cyphersec" with the uppercase
    elif [ "$protocol_name" == "cyphersec" ]; then
        echo "No, I want a big Cyphersec!"
    # If the protocol name does not match exact speling
    else
        echo "Cyphersec! Not $protocol_name!"
    fi
}

# Block 3: Data Security Tax Calculation
data_security_tax_calculation() {
    # Prompt the user to input annual data usage in MB
    read -p "Enter your annual data usage in MB: " data_usage
    # If the data usage is less than or equal to 85528 MB, calculate tax accordingly
    if [ "$data_usage" -le 85528 ]; then
        tax=$((data_usage * 18 / 100 - 556))
    # If data usage exceeds 85528 MB, calculate tax with a surplus rate
    else
        surplus=$((data_usage - 85528))
        tax=$((14839 + surplus * 32 / 100))
    fi
    # If the calculated tax is negative, set it to 0
    if [ "$tax" -lt 0 ]; then
        tax=0
    fi
    # Print the calculated Data Security Tax
    echo "Your Data Security Tax is: $tax MB"
}

# Block 4: Patch Cycle Determination
patch_cycle_determination() {
    # Prompt the user to input the year to check the patch cycle
    read -p "Enter the year to check the patch cycle: " year
    # If year is less than 2000, it is not within the managed patch period
    if [ "$year" -lt 2000 ]; then
        echo "Not within the managed patch period."
    else
		# The year is a Standard Year if it's not divisible by 4.
        if (( year % 4 != 0 )); then
            echo "Standard Year"
        # A year divisible by 4 but not by 100 is considered a "Patch Year".
        elif (( year % 100 != 0 )); then
            echo "Patch Year"
        # If the year is divisible by 100, but not divisible by 400, it's considered a Standard Year.
        elif (( year % 400 != 0 )); then
            echo "Standard Year"
        # If the year is divisible by 400, it is a "Patch Year".
        else
            echo "Patch Year"
        fi
    fi
}

# Main function to execute all blocks
main() {
    network_traffic_analysis		#call block 1
    protocol_identification			#call block 2
    data_security_tax_calculation	#call block 3
    patch_cycle_determination		#call block 4
}

# Execute main function
main
