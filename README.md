<div align="center">

# 📁 FileManager

**A tiny, dependency-free Python tool that quietly sorts your files in the background.**

![Python](https://img.shields.io/badge/python-3.6%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6?logo=windows&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

</div>

---

## ✨ What is it?

FileManager watches a folder you choose (like `Downloads`) and, every **5 seconds**, moves any files it recognises into the right place: pictures to `Pictures`, music to `Music`, videos to `Videos`, and so on.

You configure it once with a friendly setup wizard, then let it run in the background and forget about it.

## 🚀 Features

- 🔁 **Automatic**: checks your folder every 5 seconds, no interaction needed
- 🧙 **Setup wizard**: pick a preset or write your own rules
- 🛡️ **Safe moves**: never overwrites; duplicates become `name (1).ext`, `name (2).ext`, …
- ⏳ **Download-aware**: waits until a file has stopped changing before moving it
- 🔄 **Live config**: edit `setup.txt` and changes apply without restarting
- 📝 **Logging**: everything it does is written to `sorter.log`
- 🪶 **Zero dependencies**: only Python's standard library (`os`, `time`, `shutil`)

## 📦 Requirements

- Windows
- Python 3.6 or newer
- The project folder must be somewhere inside your user profile (a path containing `Users`), such as `C:\Users\YourName\Documents\FileManager`. The setup wizard uses this to find your username.

## 🛠️ Installation

```bash
git clone https://github.com/<your-username>/FileManager.git
cd FileManager
```

No `pip install` needed.

## ⚙️ Setup

Run the wizard:

```bash
python setup.py
```

1. Enter the **folder to monitor** (for example `C:\Users\YourName\Downloads`).
2. Choose how to sort your files:
   - **`view presets`** uses the built-in rules below and writes `setup.txt` for you.
   - **`use own`** writes an example `setup.txt` for you to edit by hand.

### Default preset

| Extension | Destination |
|-----------|-------------|
| `png`, `jpg` | `Pictures` |
| `mp3` | `Music` |
| `mp4`, `mov` | `Videos` |
| `zip` | `Documents` |

> ⚠️ Confirming a choice **overwrites** any existing `setup.txt`.

## ▶️ Usage

Start the sorter:

```bash
python main.py
```

### Run silently in the background

Rename `main.py` to `main.pyw`, or launch it with:

```bash
pythonw main.py
```

There is no console window. Check `sorter.log` to see what it's doing. See [Stopping the sorter](#%EF%B8%8F-stopping-the-sorter) below to shut it down.

### Start automatically at login

1. Press `Win + R`, type `shell:startup`, and press Enter.
2. Put a shortcut to `main.pyw` in the folder that opens.

## ⏹️ Stopping the sorter

Because it runs without a console window, stop it from Task Manager:

1. Press `Ctrl + Shift + Esc` to open **Task Manager**.
2. Open the **Details** tab.
3. Find **`pythonw.exe`** in the list.
4. Right-click it and choose **End task**.

> 💡 **Running other Python scripts too?** You may see more than one `pythonw.exe`. On the **Details** tab, right-click a column header, choose **Select columns**, and tick **Command line**. The entry whose command line ends in `main.pyw` (or `main.py`) is the sorter.

Prefer the command line? This stops **every** `pythonw.exe` process, so use it only if the sorter is the only one running:

```bash
taskkill /im pythonw.exe /f
```

## 🧾 Configuring `setup.txt`

`setup.txt` is a simple list of `key=value` lines. The first line is the folder to watch; every other line maps a file extension to a destination folder.

```ini
monitorDir=C:\Users\YourName\Downloads
png=C:\Users\YourName\Pictures
jpg=C:\Users\YourName\Pictures
mp3=C:\Users\YourName\Music
mp4=C:\Users\YourName\Videos
pdf=C:\Users\YourName\Documents\PDFs
```

- Extensions are written without a dot and are case-insensitive.
- Missing destination folders are created automatically.
- Add as many extensions as you like.
- Changes are picked up on the next 5-second check.

## 🔍 How it works

```
every 5 seconds
   │
   ├─ read setup.txt
   ├─ list files in monitorDir (subfolders are ignored)
   ├─ skip files whose extension isn't configured
   ├─ skip files that are still changing (e.g. downloading)
   └─ move the rest to their destination (renaming on name clashes)
```

## 📂 Project structure

```
FileManager/
├── setup.py     # interactive setup wizard, creates setup.txt
├── main.py      # the background sorter
├── setup.txt    # your rules (generated)
└── sorter.log   # activity log (generated)
```

## ❓ Troubleshooting

| Problem | Fix |
|---------|-----|
| `setup.txt not found` in the log | Run `python setup.py` first |
| `Monitor directory invalid or missing` | Check the `monitorDir` path in `setup.txt` |
| `ValueError: 'Users' is not in list` when running setup | Move the project folder somewhere inside `C:\Users\<you>\` |
| A file isn't moving | It may still be open in another program; it will retry automatically. Check `sorter.log` |
| Files go to the wrong place | Edit the paths in `setup.txt` |

## ⚠️ Limitations

- Windows only (paths are built around `C:\Users\<name>`).
- Only files directly inside the monitored folder are sorted, not subfolders.
- Sorting is by file extension only. Duplicate files are renamed, not detected or removed.

## 🗺️ Ideas for the future

- Support for subfolders
- Cross-platform paths (macOS and Linux)
- Duplicate detection
- Optional desktop notifications

---

<div align="center">

Made with 🐍 and a love of tidy folders.

</div>