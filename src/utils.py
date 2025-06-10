# src/utils.py

import os
import logging
<<<<<<< HEAD
from pathlib import Path
from functools import lru_cache
import torch
=======
>>>>>>> Task-2
from datetime import datetime
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
<<<<<<< HEAD
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def log_step(message):
    """Prints a timestamped step message to console/log."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] 🔹 {message}")

def ensure_dir(directory):
    """Ensure directory exists, create if it doesn't."""
    Path(directory).mkdir(parents=True, exist_ok=True)
=======
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
>>>>>>> Task-2

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
<<<<<<< HEAD
    return None

# Model caching utilities
MODEL_CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "models")

def get_model_cache_path(model_name):
    """Get the cache path for a specific model."""
    return os.path.join(MODEL_CACHE_DIR, model_name.replace("/", "--"))

@lru_cache(maxsize=2)
def is_model_cached(model_name):
    """Check if a model is already downloaded and cached."""
    cache_path = get_model_cache_path(model_name)
    return os.path.exists(cache_path)

def log_model_loading(model_name, is_cached=False):
    """Log model loading status."""
    status = "from cache" if is_cached else "downloading"
    log_step(f"Loading {model_name} model ({status})...")

def log_translation(text_length, source_lang=None):
    """Log translation operation details."""
    lang_info = f" from {source_lang}" if source_lang else ""
    log_step(f"Translating text{lang_info} ({text_length} characters)")

def log_sentiment_analysis(text_length, translated=False):
    """Log sentiment analysis operation details."""
    status = "translated" if translated else "original"
    log_step(f"Analyzing sentiment for {status} text ({text_length} characters)")

def get_device_info():
    """Get information about available compute devices."""
    if torch.cuda.is_available():
        device = "cuda"
        device_name = torch.cuda.get_device_name(0)
        memory = torch.cuda.get_device_properties(0).total_memory / 1e9  # Convert to GB
        return f"Using GPU: {device_name} ({memory:.1f}GB)"
    return "Using CPU"
=======
    except Exception as e:
        log_step(f"Failed to format date {date_obj}: {str(e)}", level='error')
        return None
>>>>>>> Task-2
