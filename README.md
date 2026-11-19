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
cd /path/to/VSIM
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

The entry-point filename is `main.py` with a capital `M`. On Linux and macOS, `main.py` is a different filename.

Use menu option `8` to quit. CSV inventory data is stored in the filename you enter when importing or exporting.

### Usage

At the main menu, enter the option number and follow the prompts. For example, choose **1** to add a record, then enter an item name, quantity, and unit price:

```text
Please select an option: 1
Name of Item: Coffee
Quantity of Item: 12
Price of Item: $4.50
```

### Main menu options

1. **Add Record** — Add an item with a unique name, a whole-number quantity, and a price.
    (Ex. add `Coffee` with quantity `12` and price `4.50`.)
2. **View Records** — Choose a simple or advanced chart, then optionally search for an item.
    (Ex. choose `1` for the simple chart and answer `yes` to search for `Coffee`.)
3. **Edit Record** — Enter the exact item name, then answer whether you want to change its name, quantity, or price. Answer `no` to keep a field unchanged.
4. **Delete Record** — Enter the exact item name and confirm with `yes` to remove it.
5. **Create Order** — Enter an item name and the quantity to order. Enter `done` when finished, then confirm with `yes`. The ordered quantities are deducted from inventory; items that reach zero are removed.
6. **Import Records** — Enter a CSV filename, such as `inventory.csv`, or press Enter to use the default. After importing, choose whether to enable auto-save.
7. **Export Records** — Choose **1** to save inventory records to a CSV file, or **2** to export analytics as a chart image. For records, enter a filename such as `inventory.csv`; for analytics, enter an image filename or press Enter for `inventory_analytics.png`.
8. **Quit** — If the inventory has records, choose whether to save them before exiting.

Changes are kept in the current session until you export the records or save when quitting. After importing or saving records, enabling auto-save writes later changes to that CSV file.


### Running Tests

With the virtual environment activated:

```bash
python -m pytest
```

### Troubleshooting

- If `python` is not found, use `python3` on Linux/macOS or `py` on Windows.
- If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Unrestricted` and activate the environment again.
- If you change directories, the terminal must be in the project directory (the directory containing `main.py` and `requirements.txt`) when running the commands above.
