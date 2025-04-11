"""
Program Name: linkscraper.py

Author: Emmylee Crocker

Date: April 11, 2025

Description: Scrapes links from multiple public-facing pages. 

Citation: Expanded on ISS212 Week 11 Walkthrough example.
"""

import requests  # Sends HTTP requests to the target websites
from bs4 import BeautifulSoup  # Parses HTML content from responses
from urllib.parse import urlparse  # Helps identify domain parts in URLs

# List of public-facing URLs to analyze
urls = [
    "https://www.python.org",
    "https://www.mozilla.org",
    "https://www.djangoproject.com"
]

# Open (or create) a file to store all external links found
with open("external_links.txt", "w") as f:
    # Loop through each target URL
    for url in urls:
        try:
            # Send GET request to the URL
            response = requests.get(url)
            # Parse the page content with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            # Get the base domain of the target website
            domain = urlparse(url).netloc
            external_links = []

            # Find all anchor tags with href attributes
            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                # Check if the link points to a different domain (external)
                if href.startswith("http") and urlparse(href).netloc != domain:
                    external_links.append(href)

            # Write a section header and the found links to the output file
            f.write(f"\n--- External links from {url} ---\n")
            for link in external_links:
                f.write(link + "\n")

            # Print how many external links were collected for this site
            print(f"{len(external_links)} external links from {url}")
        except Exception as e:
            # Print error if there
