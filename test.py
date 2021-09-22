import pytest
import pandas as pd
import os




def test_data_existance():
    files = os.listdir()
    assert 'data' not in files

def test_model_existance():
    files = os.listdir()
    assert 'model.h5' not in files

def test_model_accuracy():
    metrics = pd.read_csv('metrics.csv')
    max_acc = metrics.accuracy.max()
    assert max_acc>= .80

