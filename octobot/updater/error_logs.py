import logging

# Create a logger for the error logs
logger = logging.getLogger(__name__)

# Set the log level to capture all errors
logger.setLevel(logging.ERROR)

# Create a file handler to log errors to a file
file_handler = logging.FileHandler('error_logs.txt')
file_handler.setLevel(logging.ERROR)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Example usage: log an error
try:
    # Code that may raise an error
    raise Exception("An error occurred")
except Exception as e:
    logger.error(str(e))
