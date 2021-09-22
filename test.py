import pytest
import pandas as pd
import os

def check_existance(filename):
    files = os.listdir()
    assert filename not in files


