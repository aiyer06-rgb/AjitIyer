# Bash Zip File Selector
This is an interactive command-line utility that allows users to safely select files from the current directory and package them into a ZIP archive. It is designed to correctly handle filenames containing spaces and special characters without relying on GNU-specific tools.

---

#1 Features

* Interactive numbered file list
* User-driven file selection
* Safe handling of filenames with spaces and special characters
* macOS / BSD-compatible (works with default Bash 3.2)
* Input validation to prevent errors
* Clean, single-pass ZIP creation

---
Requirements

* macOS (or any Unix-like system with BSD tools)
* Bash (default macOS Bash 3.2 supported)
* `zip` utility (installed by default on macOS)

---

#2 Installation

Clone the repository or copy the script:

```bash
chmod +x script.sh
```

(Optional) Move it somewhere on your PATH:

```bash
mv script.sh /usr/local/bin/zipselect
```

---

#3 Usage

Run the script in any directory containing files:

```bash
./script.sh
```

or, if installed globally:

```bash
zipselect
```

### Example Run

```
Select files to zip:
1) Daily Movie.html
2) Movie Ideas.pdf
3) script.sh

Enter file numbers separated by spaces (e.g. 1 3 5): 1 3
Enter name for zip file (without .zip): myfiles

✅ Created myfiles.zip with 2 files.
```

---

#4 How It Works

1. Enumerates files in the current directory using `find`
2. Showcases a numbered menu for user selection
3. Converts selected indices into filenames
4. Passes filenames safely to the `zip` utility

The script avoids common Bash pitfalls such as word splitting and unsafe `ls` parsing.

---

#5 Limitations

* Operates only on the current directory
* Does not include subdirectories (by design)
* Requires numeric input for file selection
* Does not currently register other files in the current directory
