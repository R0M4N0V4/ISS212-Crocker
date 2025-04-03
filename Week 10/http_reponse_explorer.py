"""
Program Name: http_reponse_explorer.py
Author: Emmylee Crocker
Date: April 3, 2025
Description: This script explores HTTP responses by requesting and displaying headers from 
multiple websites using both default and custom User-Agent values. It also 
retrieves and prints cookie data from httpbin.org.
The script demonstrates basic use of Python's urllib library for HTTP requests, header inspection, 
and error handling.
Citation: Expands on ISS212 Week 10 Walkthrough example. Used Chat GPT to fix syntax errors within code
"""

# Import the needed modules to handle HTTP requests, handle execptions, and parse data
import urllib.request
import urllib.error
import json

# Function to get and print HTTP headers from a URL
def get_headers(url, user_agent=None):
    # Create a Request object using the provided URL
    req = urllib.request.Request(url)

    # If a custom User-Agent is provided, add it to the headers
    if user_agent:
        req.add_header('User-Agent', user_agent)

    # Try to open the URL and handle errors if they occur
    try:
        # Send the request and open the response
        with urllib.request.urlopen(req) as response:
            #Print the information
            print(f"URL: {url}")
            print("Status Code:", response.status)
            print("Response Headers:")
            # Get all headers as a list of (key, value) tuples
            headers = response.getheaders()
            # Iterate through headers and print each one
            for header, value in headers:
                print(f"  {header}: {value}")
            print("\n")
            return headers
    # If an error occurs (e.g., network issue or bad URL), catch and print the reason
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e.reason}\n")
        return None

# Function to retrieve and print cookie data from httpbin.org
def get_cookies():
    # Define the URL that returns cookie info
    url = "http://httpbin.org/cookies"
    req = urllib.request.Request(url)
    # Add a custom User-Agent header to the request
    req.add_header('User-Agent', 'CustomBrowser/1.0')

    # Try to make the request and handle errors
    try:
        # Send the request and open the response
        with urllib.request.urlopen(req) as response:
            # Print the information
            print("Fetching cookies from httpbin.org...")
            print("Status Code:", response.status)
            # Read and decode the body of the response
            body = response.read().decode('utf-8')
            # Parse the JSON data to extract cookies
            cookie_data = json.loads(body)
            print("Cookie Data:", cookie_data)
            print("\nResponse Headers:")
            # Get and print each response header
            headers = response.getheaders()
            for header, value in headers:
                print(f"  {header}: {value}")
            print("\n")
            # Return the cookie data and headers
            return cookie_data, headers
    # If an error occurs, print the reason and return None values
    except urllib.error.URLError as e:
        print(f"Error fetching cookies: {e.reason}\n")
        return None, None

# Main function to run the HTTP header and cookie checks
def main():
    # Print a title for the script
    print("HTTP Response Explorer\n")

    # List of URLs to test
    urls = ["http://example.com", "http://uma.edu"]
    user_agents = [None, "CustomBrowser/1.0"]

    # Loop over each User-Agent
    for user_agent in user_agents:
        # Set a label to describe the User-Agent type
        ua_label = "default User-Agent" if user_agent is None else "custom User-Agent"
        # Loop over each URL
        for url in urls:
            # Print which URL and User-Agent is being used
            print(f"Requesting headers from {url} with {ua_label}...\n")
            # Call the get_headers function
            get_headers(url, user_agent=user_agent)

    # Get and print cookies from httpbin
    print("Extracting cookies from httpbin.org...\n")
    get_cookies()

    # Print a completion message
    print("HTTP Response exploration complete.")

# Run the main function if this file is executed directly
if __name__ == '__main__':
    main()
