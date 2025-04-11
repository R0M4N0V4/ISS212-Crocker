'''
Jmoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - bowser.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

import os  # Used to check if the history file exists
import sqlite3  # Used to connect to and query the Chrome SQLite database
from datetime import datetime  # For converting timestamps to readable format

# Function to analyze Chrome browser history and write results to a file
def analyze_chrome_history(history_path, output_file):
    # Check if the given path is a valid file
    if not os.path.isfile(history_path):
        print("Invalid file path. Please make sure the file exists.")
        return

    try:
        # Connect to the Chrome history SQLite database
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()

        # Execute SQL query to get all rows from the 'urls' table
        cursor.execute("SELECT * FROM urls")
        rows = cursor.fetchall()

        print("[--- Browser History Analysis ---]\n")

        # Open the output file for writing results
        with open(output_file, 'w', encoding='utf-8') as file:
            for row in rows:
                url = row[1]  # The URL is in the second column
                last_visit_time_microseconds = row[5]  # Chrome stores visit time in microseconds since Jan 1, 1601

                # Convert the visit time to human-readable format if it's a valid number
                if last_visit_time_microseconds and last_visit_time_microseconds < 2**63:
                    try:
                        # Chrome's time format is based on Windows epoch — need to convert to Unix time
                        visit_time = datetime.fromtimestamp(
                            (last_visit_time_microseconds - 11644473600000000) / 1000000
                        ).strftime('%Y-%m-%d %H:%M:%S')
                    except (ValueError, TypeError) as e:
                        print(f"Error converting visit time: {e}")
                        visit_time = "N/A"
                else:
                    visit_time = "N/A"

                # Format and print the result
                output_line = f"[+] URL: {url}\n   Last Visit Time: {visit_time}\n"
                print(output_line)
                file.write(output_line)  # Write result to output file

        print(f"\nBrowser history has been saved to {output_file}")

    except sqlite3.Error as e:
        # If there's a problem with the database connection or query
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection to avoid locking the file
        if connection:
            connection.close()

# Run the script only if it's executed directly (not imported)
if __name__ == "__main__":
    # Ask the user for the path to the Chrome history database file
    chrome_history_path = input("Enter the path to the Chrome history database: ")

    # Ask where to save the extracted history output
    output_file_path = input("Enter the path to save the output file (e.g., output.txt): ")

    # Call the function with user-provided paths
    analyze_chrome_history(chrome_history_path, output_file_path)
