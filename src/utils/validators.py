from datetime import datetime
from tkinter import messagebox

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

def validate_date(date_str):
    """
    Validate date string format (MM/DD/YYYY)
    Returns: (bool, str) - (is_valid, error_message)
    """
    if not date_str:
        return False, "Date is required"
    
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
        return True, ""
    except ValueError:
        return False, "Invalid date format. Use MM/DD/YYYY"

def validate_required_field(value, field_name):
    """
    Validate required fields
    Returns: (bool, str) - (is_valid, error_message)
    """
    if not value or value.strip() == "":
        return False, f"{field_name} is required"
    return True, ""