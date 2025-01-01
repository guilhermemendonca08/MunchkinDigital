import os
import sys


def resource_path(relative_path):
    """Get the absolute path to a resource."""
    if hasattr(sys, "_MEIPASS"):  # Temporary folder in --onefile mode
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

