
import os
import pytest
import numpy as np

@pytest.fixture(scope='function')
def from_list():
    return ["apple", "apples", "appl", "recal", "house", "similarity"]

@pytest.fixture(scope='function')
def to_list():
    return ["apple", "apples", "mouse"]

@pytest.fixture(scope='function')
def from_vector():
    '/Users/dwyk/d2/s4/m7/k_/k5/pyc0502fm/PolyFuzz-master/tst/from_list.npy'
    os_cwd = os.getcwd()
    from_vector=None
    with open(os.path.join(os_cwd, 'from_list.npy'), 'rb') as f:
        from_vector = np.load(f)
    return from_vector

@pytest.fixture(scope='function')
def to_vector():
    os_cwd = os.getcwd()
    to_vector = None
    with open(os.path.join(os_cwd, 'to_list.npy'), 'rb') as f:
        to_vector = np.load(f)
    return to_vector

