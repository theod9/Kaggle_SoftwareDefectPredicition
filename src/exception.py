import sys
import os
import traceback
from src.logger import logging


def error_message_detail(error: str, error_detail: Exception) -> str:
    """
    Extracts and formats the error message with details including filenames and line numbers.
    Converts absolute paths to relative paths.
    """
    # Extract the full traceback details
    tb = traceback.extract_tb(error_detail.__traceback__)
    
    # List to hold formatted traceback entries
    formatted_traceback = []
    
    for frame in tb:
        filename = frame.filename
        # Convert absolute paths to relative paths if they are within the project directory
        relative_filename = os.path.relpath(filename, os.getcwd())
        formatted_traceback.append(f"File '{relative_filename}', line {frame.lineno}, in {frame.name}")
    
    # Join all traceback entries into a single string
    traceback_str = "\n".join(formatted_traceback)
    
    error_message = f"Error: '{error}' occurred:\n{traceback_str}\nException Type: [{type(error_detail).__name__}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: Exception):
        super().__init__(error_message)
        # Generate a detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        # Optional: Log the error automatically
        # logging.error(self.error_message)
      
    def __str__(self) -> str:
        return self.error_message

    
# if __name__ == "__main__":
#     try:
#         # Example of a code block that may raise an exception
#         raise ValueError("This is a ValueError")
#     except Exception as e:
#         # Create a custom exception with the error message and the exception object
#         custom_exception = CustomException(str(e), e)
        
#         # Print the custom exception
#         print(custom_exception)
#         # Optional: Log the custom exception
#         # logging.error(custom_exception)
#         logging.info(custom_exception)




    
        
