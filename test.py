import pytest
import pandas as pd
import os


def check_sum():
    assert(2+3==5)

def check_existance():
    files = os.listdir()
    print(files)
    assert 'data' not in files
