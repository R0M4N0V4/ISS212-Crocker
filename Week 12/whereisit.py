'''
Jmoody 
Commented by: Emmylee Crocker
4.2025 Wk 12 Tool Development 8 - whereisit.py
Citation: Python for Networking & Security vol 3 - JOrtega
Usage: Command to run the script (if running from directory where script is located):
run in a different terminal: python whereisit.py whereisit.jpg
'''
# Imports needed modules 
import argparse # Handles command-line arguments
from PIL import Image # Allows image file manipulation
from PIL.ExifTags import TAGS, GPSTAGS  # Provides readable EXIF and GPS tag names
import sys # Used for system exit

# Extracts GPS-related data from EXIF metadata
def get_geotagging(exif):
    if not exif:
        # If no metadata is found, raise an error
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    # Loop through all metadata tags and look for the one labeled 'GPSInfo'
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            # If 'GPSInfo' is not present, raise an error
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            # Match readable GPS tag names with actual values
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

# Converts GPS coordinates from degrees/minutes/seconds to decimal format
def dms_to_dd(d, m, s, ref):
    # Formula to convert to decimal degrees
    decimal_degrees = d + float(m)/60 + float(s)/(60*60)
    # Adjust for southern or western coordinates by making the value negative
    if ref in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

# Extracts GPS coordinates and converts them to decimal degrees
def extract_gps_coords(exif_data):
    geotags = get_geotagging(exif_data)
    # If no GPS tags are found, return None
    if not geotags:
        return None, None

    # Convert the latitude to decimal format
    latitude = dms_to_dd(geotags['GPSLatitude'][0], geotags['GPSLatitude'][1], geotags['GPSLatitude'][2], geotags['GPSLatitudeRef'])
    # Convert the longitude to decimal format
    longitude = dms_to_dd(geotags['GPSLongitude'][0], geotags['GPSLongitude'][1], geotags['GPSLongitude'][2], geotags['GPSLongitudeRef'])

    return latitude, longitude

# Main function to open the image, read metadata, and print coordinates
def main():
    # Set up the command-line argument parser with a description    
    parser = argparse.ArgumentParser(description='Metadata from images')
    # Add a required argument for the image file
    parser.add_argument('PICTURE_FILE', help='Path to the image file')
    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Open the image file provided as input
    img_file = Image.open(args.PICTURE_FILE)
    # Get EXIF metadata from the image
    exif_data = img_file._getexif()

    # If the image has no metadata, print a message and exit
    if exif_data is None:
        print("No EXIF data found")
        sys.exit()

    # Extract GPS coordinates from the metadata
    latitude, longitude = extract_gps_coords(exif_data)

    # If both latitude and longitude are found, print them along with a Google Maps URL
    if latitude is not None and longitude is not None:
        print("GPS Coordinates: {}, {}".format(latitude, longitude))
        gmaps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print("Google Maps URL: {}".format(gmaps_url))

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
