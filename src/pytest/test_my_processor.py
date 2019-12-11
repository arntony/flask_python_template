"""
test_my_processor.py - this module tests methods inside MyProcessor class
"""

import pytest
from codes.my_processor import MyProcessor
import pandas as pd


@pytest.fixture
def my_processor():
    """
    sets my_processor instance for testing

    Returns
    -------
    None
    """
    my_processor = MyProcessor()
    yield my_processor


def test_run(my_processor):
    """
    :: function : test_run :: assertion test for function run()

    Parameters
    ----------
    my_processor : PyTest fixture instance of class MyProcessor

    Returns
    -------
    None
    """
    df = pd.DataFrame({"num1": [1, 2, 3], "num2": [4, 5, 6]})
    expected_result = pd.DataFrame({"num1": [2.0, 1.0, 3.0], "num2": [5.0, 4.0, 6.0]}, index=['mean', 'min', 'max'])
    actual_result = my_processor.run(df)
    assert expected_result.equals(actual_result)
