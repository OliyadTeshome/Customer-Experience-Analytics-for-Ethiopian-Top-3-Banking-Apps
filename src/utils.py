# src/utils.py

import os
import logging
from pathlib import Path
from functools import lru_cache
import torch
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
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

def format_date(date_obj):
    """Converts date object to standardized YYYY-MM-DD string."""
    if date_obj:
        return date_obj.strftime('%Y-%m-%d')
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
