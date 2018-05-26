#!/usr/bin/python3

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(Error):
    """Exception raised for errors in the validation.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
