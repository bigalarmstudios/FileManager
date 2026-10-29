import os
import time
import shutil  # standard library, used for moving files across drives

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "setup.txt")
LOG_PATH = os.path.join(SCRIPT_DIR, "sorter.log")
CHECK_INTERVAL = 5  # seconds

# path -> (size, modified time) from the previous check
last_seen = {}


def log(message):
    """Write to a log file (there is no console when running in the background)."""
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "  " + message + "\n")


def load_settings():
    """Read setup.txt and return (monitorDir, {extension: destination})."""
    monitor_dir = None
    destinations = {}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip().lower().lstrip(".")
            value = value.strip().strip('"')

            if key == "monitordir":
                monitor_dir = value
            elif key == "extension":
                continue  # placeholder line from the "use own" example file
            elif "Your" in value:
                continue  # example path the user hasn't edited yet
            else:
                destinations[key] = value

    return monitor_dir, destinations


def is_stable(path):
    """True only if the file looks the same as it did on the previous check."""
    try:
        stat = os.stat(path)
    except OSError:
        return False
    current = (stat.st_size, stat.st_mtime)
    previous = last_seen.get(path)
    last_seen[path] = current
    return previous == current


def unique_path(folder, filename):
    """If a file with the same name exists, return name (1).ext, name (2).ext, ..."""
    target = os.path.join(folder, filename)
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(target):
        target = os.path.join(folder, f"{base} ({counter}){ext}")
        counter += 1
    return target


def sort_files(monitor_dir, destinations):
    names = os.listdir(monitor_dir)

    # Forget files that are no longer in the folder
    current_paths = {os.path.join(monitor_dir, n) for n in names}
    for path in list(last_seen):
        if path not in current_paths:
            del last_seen[path]

    for name in names:
        source = os.path.join(monitor_dir, name)

        if not os.path.isfile(source):
            continue  # skip folders

        ext = os.path.splitext(name)[1].lower().lstrip(".")
        if ext not in destinations:
            continue

        if not is_stable(source):
            continue  # still changing, check again next cycle

        dest_folder = destinations[ext]
        try:
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(source, unique_path(dest_folder, name))
            last_seen.pop(source, None)
            log(f"Moved {name} -> {dest_folder}")
        except (PermissionError, OSError) as e:
            # Usually the file is still open in another program; retry next cycle
            log(f"Could not move {name} (will retry): {e}")


def main():
    log("Sorter started.")
    while True:
        try:
            # Re-read each cycle so edits to setup.txt apply without a restart
            monitor_dir, destinations = load_settings()

            if not monitor_dir or not os.path.isdir(monitor_dir):
                log(f"Monitor directory invalid or missing: {monitor_dir}")
            else:
                sort_files(monitor_dir, destinations)
        except FileNotFoundError:
            log("setup.txt not found. Run setup.py first.")
        except Exception as e:
            log(f"Unexpected error: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()