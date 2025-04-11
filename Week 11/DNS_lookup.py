"""
Program Name: DNS_lookup.py

Author: Emmylee Crocker

Date: April 11, 2025

Description: Queries A (address) records for a list of public domains using Cloudflare DNS.
The script collects and saves the IP addresses associated with each domain to a text file.
Citation: Expanded on ISS212 Week 11 Walkthrough example.
"""

import dns.resolver  # Used to perform DNS lookups

# Force the script to use Cloudflare's DNS resolver
dns.resolver.default_resolver = dns.resolver.Resolver()
dns.resolver.default_resolver.nameservers = ['1.1.1.1']

# List of public-facing domains to check
domains = ["nvd.nist.gov", "python.org", "uma.edu"]

# Open (or create) the output file to save DNS results
with open("dns_results.txt", "w") as f:
    # Loop through each domain in the list
    for domain in domains:
        try:
            # Query A records (IPv4 addresses) for the domain
            a_records = dns.resolver.resolve(domain, 'A')
            # Write a header to the output file
            f.write(f"\n--- A Records for {domain} ---\n")
            # Write each A record (IP address) to the file
            for record in a_records:
                f.write(record.to_text() + "\n")
            # Print confirmation in the console
            print(f"Resolved {domain}")
        except Exception as e:
            # Print error if DNS query fails
            print(f"Error resolving {domain}: {e}")
