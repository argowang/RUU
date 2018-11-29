# RUU
IDS Second Project Code Base

# Dependency
## KeyLogger
We will use opensource [keylogger](https://github.com/GiacomoLaw/Keylogger) to record the keystroke typed.
## Python
We are using Python2 for the project. Make sure you pip install the following packages before executing the scripts.
* psutil
* AppKit (pip install git+git://github.com/nitipit/appkit.git, but be sure to install pyobjc first)
* [filewatcher](https://github.com/meliot/filewatcher)
    * To make the log file more clear, we modified two lines in lib/token.c:
        - [1] in line 54, change
            ```
            "%s ["C_CYAN"%s"C_RESET"] Detected "C_YELLOW"%s"C_RESET" event from "C_GREEN"%s"C_RESET" -> %s\n",
            ```
            to
            ```
            "%s [%s] Detected %s event from %s -> %s\n"
            ```
        - [2] in line 64, change
            ```
            "%s ["C_CYAN"%s"C_RESET"] Detected "C_YELLOW"%s"C_RESET" event from "C_GREEN"%s"C_RESET"\n"
            ```
            to
            ```
            "%s [%s] Detected %s event from %s\n"
            ```
        then _make_ the file again.
 
