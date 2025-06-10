# src/utils.py

import os
import logging
from datetime import datetime
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def log_step(message: str, level: str = 'info') -> None:
    """Logs a timestamped step message with specified logging level."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] 🔹 {message}"
    
    if level == 'error':
        logger.error(log_message)
    elif level == 'warning':
        logger.warning(log_message)
    else:
        logger.info(log_message)

def ensure_dir(directory: str) -> bool:
    """Ensures a directory exists; creates it if it doesn't."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            log_step(f"Created directory: {directory}")
            return True
        log_step(f"Directory already exists: {directory}")
        return True
    except Exception as e:
        log_step(f"Failed to create directory {directory}: {str(e)}", level='error')
        return False

def format_date(date_obj: Optional[datetime]) -> Optional[str]:
    """Converts date object to standardized YYYY-MM-DD string."""
    if not date_obj:
        return None
        
    try:
        if isinstance(date_obj, str):
            date_obj = datetime.strptime(date_obj, '%Y-%m-%d')
        return date_obj.strftime('%Y-%m-%d')
    except Exception as e:
        log_step(f"Failed to format date {date_obj}: {str(e)}", level='error')
        return None
