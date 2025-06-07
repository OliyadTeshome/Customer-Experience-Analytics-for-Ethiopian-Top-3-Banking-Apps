# src/utils.py

import os
from datetime import datetime

def log_step(message):
    """Prints a timestamped step message to console/log."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] 🔹 {message}")

def ensure_dir(directory):
    """Ensures a directory exists; creates it if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        log_step(f"Created directory: {directory}")
    else:
        log_step(f"Directory already exists: {directory}")

def format_date(date_obj):
    """Converts date object to standardized YYYY-MM-DD string."""
    if date_obj:
        return date_obj.strftime('%Y-%m-%d')
    return None
