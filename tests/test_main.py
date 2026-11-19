# tests/test_main.py
"""
“Per me si va ne la città dolente,
per me si va ne l’eterno dolore,
per me si va tra la perduta gente.
Giustizia mosse il mio fattore;
fatto mi avea la divina podestate,
la somma sapïenza e ‘l primo amore.
Dinanzi a me non fuor cose create
se non etterne, e io etterno duro.
Lasciate ogne speranza, voi ch’intrate.”
"""

'''
IMPORTS
'''
import sys
from pathlib import Path

import pandas as pd
import pytest as pt

# add the project root so Main can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Main import (
    calculate_average_item_value,
    calculate_chart_value,
    calculate_highscores,
    calculate_item_value,
    calculate_item_values,
    load_records,
    save_records,
)

'''
TEST DATA
'''
# Remove this if you don't end up using it

# NO EDGE CASES
TestInv = pd.read_csv(  # import csv into dataframe
    Path(__file__).parent / "fixtures" / "test_inventory.csv",  # locate w/ relative path
    index_col=0,  # use the item name as the index
).to_dict(orient="index")  # convert sorted rows into dictionary

# LARGE PRICE, ZERO PRICE, ZERO STOCK, 
WeirdInv = pd.read_csv(
    Path(__file__).parent / "fixtures" / "weird_inventory.csv",
    index_col=0,
).to_dict(orient="index")

# LARGE PRICE, ZERO PRICE, ZERO STOCK, 
WeirdInv = pd.read_csv(
    Path(__file__).parent / "fixtures" / "weird_inventory.csv",
    index_col=0,
).to_dict(orient="index")

'''
Function tests
'''
def test_calculate_item_value():
    for inv in (TestInv, WeirdInv):
        for item in inv.values():
            assert calculate_item_value(item) == item["quantity"] * item["price"]

def test_calculate_chart_value():
    for inv in (TestInv, WeirdInv):
        value = 0
        for item in inv.values():
            value += calculate_item_value(item)
        assert calculate_chart_value(inv) == value

def test_calculate_item_values():
    for inv in (TestInv, WeirdInv):
        item_values = calculate_item_values(inv)
        for item_name, item in inv.items():
            assert item_values[item_name] == calculate_item_value(item)

def test_calculate_average_item_value():
    for inv in (TestInv, WeirdInv):
        average_value = calculate_average_item_value(inv)
        # manual calc
        item_values = calculate_item_values(inv) 
        expected_average = sum(item_values.values()) / len(item_values)
        assert average_value == expected_average # checks manual against function

def test_calculate_highscores():
    for inv in (TestInv, WeirdInv):
        highscores = calculate_highscores(inv)
        expected_highscores = (
            min(inv, key=lambda name: inv[name]["index"]), # first item
            max(inv, key=lambda name: inv[name]["index"]), # last item
            max(inv, key=lambda name: calculate_item_value(inv[name])), # highest item value
            min(inv, key=lambda name: calculate_item_value(inv[name])), # lowest item value
            max(inv, key=lambda name: inv[name]["price"]), # highest price
            min(inv, key=lambda name: inv[name]["price"]), # lowest price
            max(inv, key=lambda name: inv[name]["quantity"]), # highest quantity
            min(inv, key=lambda name: inv[name]["quantity"]), # lowest quantity
        )
        assert highscores == expected_highscores

def test_save_records_handles_save_errors(tmp_path):
    saved, message = save_records(TestInv, tmp_path)
    assert saved is False
    assert "Could not save inventory" in message

def test_load_records_handles_invalid_encoding(tmp_path):
    bad_file = tmp_path / "bad.csv"
    bad_file.write_bytes(b"\xff\xfe\xfa")
    current = {"existing": {"quantity": 1, "price": 2.0, "index": 1}}

    loaded, message = load_records(str(bad_file), current)

    assert loaded is current
    assert "could not be decoded" in message

'''
MAIN
'''
def test_main():
    test_calculate_item_value()
    test_calculate_chart_value()
    test_calculate_item_values()
    test_calculate_average_item_value()
    test_calculate_highscores()

if __name__ == "__main__":
    pt.main([__file__])  # run pytest on this file