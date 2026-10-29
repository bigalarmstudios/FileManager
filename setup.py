import os
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
        print(preset1[1],"=", pictures_path)
        print(preset1[2], "=", music_path)
        print(preset1[3], "=", videos_path)
        print(preset1[4], "=", videos_path)
        print(preset1[5], "=", documents_path)
        confirm = input("Y/N : ")
        if confirm == "y" or confirm == "Y":
            print("setting...")
            fileTypesToMonitor = preset1
            print(fileTypesToMonitor)
        else:
            print("returning to setup")
            setup()
        
def setup():
    print("Configure your directory to monitor")
    monitorDir = input("User: ")
    print("Which type of files do you want to monitor?")
    print("behavior will be sorted into different directories based on file type")
    print("options:")
    print("view presets")
    print("use own")
    fileTypesToMonitor = input("User: ")
    splitFileTypesToMonitor(fileTypesToMonitor, monitorDir)

setup()