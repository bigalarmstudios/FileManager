import os
import time
preset1 = "png","jpg","mp3","mp4","mov","zip"

# Get the directory containing this Python script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
path_components = SCRIPT_DIR.split(os.sep)
users_index = path_components.index("Users")
username = path_components[users_index + 1]
pictures_path = os.path.join("C:\\", "Users", username, "Pictures")
music_path = os.path.join("C:\\", "Users", username, "Music")
videos_path = os.path.join("C:\\", "Users", username, "Videos")
documents_path = os.path.join("C:\\", "Users", username, "Documents")
FILE_PATH = os.path.join(SCRIPT_DIR, "setup.txt")


def splitFileTypesToMonitor(fileTypesToMonitor, monitorDir):
    if fileTypesToMonitor == "view presets":
        print("you will use the preset:")
        print(preset1[0], "=", pictures_path)
        print(preset1[1], "=", pictures_path)
        print(preset1[2], "=", music_path)
        print(preset1[3], "=", videos_path)
        print(preset1[4], "=", videos_path)
        print(preset1[5], "=", documents_path)
        print("Choosing 'y' will overwrite existing setup.txt file!")

        confirm = input("Y/N: ")

        if confirm.lower() == "y":
            print("setting and writing...")

            destinations = {
                "png": pictures_path,
                "jpg": pictures_path,
                "mp3": music_path,
                "mp4": videos_path,
                "mov": videos_path,
                "zip": documents_path
            }

            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(f"monitorDir={monitorDir}\n")

                for extension, destination in destinations.items():
                    f.write(f"{extension}={destination}\n")

            print("Settings saved successfully!")
            time.sleep(0.5)
            print("Exit setup and run main.py")
            print("available options: help, quit")
            answer = input("User: ")
            if answer.lower() == "help":
                print("If destninations are wrong for your computer, you can go and manually edit setup.txt")
            elif answer.lower() == "quit":
                print("Quitting...")
                exit()
            else:
                print("exiting")
                exit()
        else:
            print("Returning to setup")
            setup()
    elif fileTypesToMonitor == "use own":
        print("choosing yes overwrites existing setup.txt file!")
        print("Choose only if setup.txt doesnt exist or want to overwrite it:")
        print("choosing yes writes an example file of setup.txt for you to edit on your own.")
        confirm = input("y/n: ")
        if confirm.lower() == "y":
            print("writing example setup.txt...")
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(f"monitorDir={monitorDir}\n")
                f.write("extension=C:\\Users\\YourName\\Pictures\n")
                f.write("jpg=C:\\Your\\desired\\path\n")
                f.write("extension=C:\\Users\\YourName\\Music\n")
                f.write("mp4=C:\\Your\\desired\\path\n")
                f.write("extension=C:\\Users\\YourName\\Videos\n")
                f.write("zip=C:\\Your\\desired\\path\n")

            print("Example setup.txt created. Please edit it with your desired settings.")
            print("Exiting setup...")
            input("Press Enter to exit...")
            exit()
        else:
            print("Returning to setup")
            input("Press Enter to continue...")
            setup()
def setup():
    print("Welcome to the setup wizard for the file monitoring and sorting program.")
    print("Configure your directory to monitor and sort")
    monitorDir = input("User: ")
    print("Which type of files do you want to monitor?")
    print("behavior will be sorted into different directories based on file type")
    print("options:")
    print("view presets")
    print("use own")
    fileTypesToMonitor = input("User: ")
    splitFileTypesToMonitor(fileTypesToMonitor, monitorDir)
setup()