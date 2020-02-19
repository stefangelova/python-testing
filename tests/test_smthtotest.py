import pytest
from applications import smthtotest

def test_smthtotest_num():
    assert smthtotest.test_test(5,4) == 18