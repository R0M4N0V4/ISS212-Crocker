'''
JMoody
Commented By: Emmylee Crocker
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use files: ioc-bfa.log, ioc-malexec.log, ioc-unauth.log
'''

import logging  # Standard logging module for tracking events and errors
from logging.handlers import TimedRotatingFileHandler  # Allows automatic log rotation

# Basic logging configuration — writes DEBUG-level logs to the specified file
def basic_logging(output_file):
    logging.basicConfig(filename=output_file, level=logging.DEBUG)

# Logging with file rotation — useful for daily logs or forensic investigations over time
def file_rotation_logging(output_file):
    logger = logging.getLogger(__name__)  # Create a named logger for this module
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Format log entries

    # Create a rotating file handler that creates a new file at midnight and keeps 7 backups
    file_handler = TimedRotatingFileHandler(output_file, when='midnight', backupCount=7)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

# Log an error with full traceback — simulates an exception and logs detailed info
def log_error_with_traceback(output_file):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=output_file, level=logging.DEBUG)

    try:
        open('non_existent_file.txt', 'rb')  # Intentional error: file does not exist
    except Exception as exception:
        # Log the exception with full traceback
        logger.error('Failed to open file', exc_info=True)
        logger.exception('Failed to open file')

# Main function to run each logging method and then combine the logs
if __name__ == "__main__":
    # Ask user to enter names for each log file
    output_file_basic = input("Enter log file name for basic logging: ")
    output_file_rotation = input("Enter log file name for file rotation logging: ")
    output_file_error = input("Enter log file name for logging errors with traceback: ")
    output_file_combined = input("Enter log file name to combine all logs: ")

    # Run each logging method with the user-provided filenames
    basic_logging(output_file_basic)
    file_rotation_logging(output_file_rotation)
    log_error_with_traceback(output_file_error)

    # Combine contents of all individual logs into one file
    with open(output_file_combined, 'w') as combined_file:
        for log_file in [output_file_basic, output_file_rotation, output_file_error]:
            with open(log_file, 'r') as log:
                combined_file.write(log.read())  # Append log contents to the combined file
