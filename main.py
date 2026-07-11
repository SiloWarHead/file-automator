import time
from src import start_observer

if __name__ == "__main__":
    observer = start_observer()
    print("Automation is running...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()