import re
import torch
import logging

def clean_text(text):
    return text.strip().lower().replace("'", "").replace('"', "").replace("/", " ").replace("|", " ").replace("-", " ").replace(",", "").replace(".", "").replace("&", "and").replace(" ", "_")


def normalize_year(cell_value):
    """
    Converts year strings like '800 BCE' to -800
    and '1999' or '1999 CE' to 1999
    """
    if cell_value is None:
        return None

    value = str(cell_value).strip().upper()

    # Extract the numeric year
    match = re.search(r'\d+', value)
    if not match:
        return None

    year = int(match.group())

    # Check for BCE
    if "BCE" in value or "BC" in value:
        return -year

    return year


def get_device():
    if torch.backends.mps.is_available():
        print("Using MPS")
        return torch.device("mps")
    elif torch.cuda.is_available():
        print("Using GPU")
        return torch.device("cuda")
    else:
        print("Using CPU")
        return torch.device("cpu")
    
def setup_logging(log_filename="application.log"):
    """Initializes the standard logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(message)s',
        handlers=[
            logging.FileHandler(log_filename, mode='w'), # 'w' overwrites each run
            logging.StreamHandler()                      # Also print to console
        ]
    )
    return logging.getLogger(__name__)