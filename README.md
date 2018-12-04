# RUU
IDS Second Project Code Base

# Usage
## Data Monitor
To start the monitor:
```
    sudo ./auditControlCenter.sh
```
The log would be generated in the /log directory.

## Data Preprocessing
Use scripts in data-processing/ folder to process collected log

# Dependency
## opensnoop
* You have to turn off your system integrity protection. IT IS RISKY. PROCEED WITH CAUTION.

## unbuffer
* Install expect by
```
    brew install expect
```

## Python
We are using Python2 for the project. Make sure you pip install the following packages before executing the scripts.
* psutil
* AppKit (pip install git+git://github.com/nitipit/appkit.git, but be sure to install pyobjc first)
* sklearn
* numpy
* AppScript
