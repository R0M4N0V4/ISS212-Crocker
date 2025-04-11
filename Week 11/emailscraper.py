"""
Program Name: emailscraper.py

Author: Emmylee Crocker

Date: April 11, 2025

Description: Scrapes emails from multiple public-facing pages. 

Citation: Expanded on ISS212 Week 11 Walkthrough example.
"""

import re  # Regular expressions for email matching
import requests  # Handles HTTP requests
from bs4 import BeautifulSoup  # Parses HTML content

# List of publicly available URLs to scrape
urls = [
    "https://www.augustaschools.org/staff/",
    "https://www.rsu64schools.org/o/chs/staff",
    "https://www.bu.edu/contact/"
]

# Open (or create) the output file where emails will be saved
with open("emails_found.txt", "w") as f:
    # Loop through each URL
    for url in urls:
        try:
            # Send HTTP GET request to the URL
            response = requests.get(url)
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")
            # Define regular expression to find email addresses
            email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
            # Use regex to find all unique emails in the page text
            emails = set(re.findall(email_pattern, soup.text))
            # Write the source URL and found emails to the output file
            f.write(f"\n--- Emails from {url} ---\n")
            for email in emails:
                f.write(email + "\n")
            # Print result summary to console
            print(f"Found {len(emails)} emails on {url}")
        except Exception as e:
            # Print error message if the request or parsing fails
            print(f"Error scraping {url}: {e}")
