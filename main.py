
import os
import time
from datetime import datetime

# Directory you want to monitor
WATCH_DIR = r"C:\Users\YourName\Downloads"

# How often to check, in seconds
CHECK_INTERVAL = 5


def get_snapshot(directory):
    """Return the current state of files in a directory."""
    snapshot = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)

            try:
                stat = os.stat(path)
                snapshot[path] = (
                    stat.st_mtime_ns,
                    stat.st_size
                )
            except (FileNotFoundError, PermissionError):
                pass

    return snapshot


def main():
    if not os.path.isdir(WATCH_DIR):
        print(f"Directory does not exist: {WATCH_DIR}")
        return

    print(f"Watching: {WATCH_DIR}")
    print(f"Checking every {CHECK_INTERVAL} seconds.")
    print("Press Ctrl+C to stop.\n")

    previous = get_snapshot(WATCH_DIR)

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            current = get_snapshot(WATCH_DIR)

            # New files
            for path in current.keys() - previous.keys():
                print(f"[NEW]     {path}")

            # Deleted files
            for path in previous.keys() - current.keys():
                print(f"[DELETED] {path}")

            # Modified files
            for path in current.keys() & previous.keys():
                if current[path] != previous[path]:
                    print(f"[CHANGED] {path}")

            previous = current

    except KeyboardInterrupt:
        print("\nStopped watching.")


if __name__ == "__main__":
    main()
