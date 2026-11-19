# VSIM
## Very Simple Inventory Manager

### Overview
VSIM is a command-line inventory software with a focus on record management and analytics. Compatible .csv files can be imported, but it is recommended to create and save an inventory file first to understand the format.

### Requirements
- Python 3.11 or newer
- `pip`
- A terminal

The graphical analytics chart requires a desktop session.

### Fresh Installation

Open a terminal and enter the project directory:

```bash
cd /path/to/PyCapstone
```

Create a virtual environment:

**Linux or macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt)**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Upgrade `pip` and install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Running VSIM

Run the application from the project directory:

```bash
python main.py
```

Use menu option `8` to quit. CSV inventory data is stored in the filename you enter when importing or exporting.

### Running Tests

With the virtual environment activated:

```bash
python -m pytest
```

### Troubleshooting

- If `python` is not found, use `python3` on Linux/macOS or `py` on Windows.
- If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Unrestricted` and activate the environment again.
- If you change directories, the terminal must be in the project directory (the directory containing `main.py` and `requirements.txt`) when running the commands above.
