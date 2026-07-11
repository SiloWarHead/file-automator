import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .config import BASE_PATH, FILE_CATEGORIES, DESTINATIONS

class FileWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            self.organize_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.organize_file(event.src_path)

    def organize_file(self, file_path):
        if not os.path.exists(file_path):
            return

        filename = os.path.basename(file_path)
        extension = os.path.splitext(filename)[1].lower()

        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                destination_dir = DESTINATIONS[category]
                
                try:
                    time.sleep(1)
                    shutil.move(file_path, os.path.join(destination_dir, filename))
                except Exception:
                    pass
                break

def start_observer():
    event_handler = FileWatcher()
    observer = Observer()
    observer.schedule(event_handler, BASE_PATH, recursive=False)
    observer.start()
    return observer