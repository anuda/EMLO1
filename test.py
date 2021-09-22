import pytest
import pandas as pd
import os


def test_sum():
    assert(2+3==5)

def test_existance():
    files = os.listdir()
    print(files)
    assert 'data' not in files

