'''
JMoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - dca-hw.py
NOTE: Use files: dca-log.csv & dca-db.db .
'''

import csv     # Used to read the log data from a CSV file
import sqlite3 # Used to interact with the SQLite database

# Function to read log data from a CSV file and return it as a list of dictionaries
def retrieve_log_data(log_file):
    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Each row becomes a dictionary
        return list(reader)

# Function to retrieve user data from the SQLite database and return it as a list of dictionaries
def retrieve_database_data(db_file):
    conn = sqlite3.connect(db_file)  # Connect to the SQLite database
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")  # Query all rows from the 'users' table
    rows = cursor.fetchall()  # Get all the results
    conn.close()  # Close the connection

    # Return each row as a dictionary with labeled fields
    return [{'id': row[0], 'username': row[1], 'role': row[2], 'email': row[3], 'website': row[4]} for row in rows]

# Function to display all usernames in the log and allow the user to select one
def prompt_for_username(log_data):
    print("Available usernames:")
    for i, entry in enumerate(log_data):
        print(f"{i + 1}. {entry.get('username')}")  # Display each username with an index

    # Prompt user to select a username by number
    selection = int(input("Select a username by entering its number: ")) - 1
    return log_data[selection].get('username').strip()

# Function to find and print log entries that match the selected username
def correlate_data_based_on_user_input(database, log_data, selected_username):
    # Filter the log data where username matches the selected one
    correlated_data = [entry for entry in log_data if entry.get('username').strip() == selected_username]

    if correlated_data:
        print(f"\nCorrelated data for '{selected_username}':")
        for entry in correlated_data:
            print(entry)  # Print each matching entry
    else:
        print(f"No data found for the entered username '{selected_username}'.")

# Prompt user for filenames of the log and database
log_file = input("Enter the log file name (e.g., logfile.csv): ")
db_file = input("Enter the database file name (e.g., local_db_file.db): ")

# Load data from both sources
log_data = retrieve_log_data(log_file)
database = retrieve_database_data(db_file)

# Allow the user to choose a username from the log
selected_username = prompt_for_username(log_data)

# Display the log entries related to the selected user
correlate_data_based_on_user_input(database, log_data, selected_username)
