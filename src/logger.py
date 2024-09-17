import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
logs_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Define the log file name based on the current date and time
log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(logs_directory, log_file_name)

# Get the root logger to avoid duplicate handlers on multiple imports
logger = logging.getLogger()
if not logger.hasHandlers():
    # Configure logging to log both to file and console
    file_handler = logging.FileHandler(log_file_path)
    console_handler = logging.StreamHandler()

    # Define logging format
    log_format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Set the formatter for both handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Set default logging level (can be adjusted as needed)
    logger.setLevel(logging.INFO)

# Example usage:
logger.info("Logging setup complete.")

