import os

BASE_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

DESTINATIONS = {
    "images": os.path.join(os.path.expanduser("~"), "Pictures"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "media": os.path.join(os.path.expanduser("~"), "Videos"),
    "music": os.path.join(os.path.expanduser("~"), "Music")
}

FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "media": [".mp4", ".mov", ".avi"],
    "music": [".mp3", ".wav", ".flac"]
}