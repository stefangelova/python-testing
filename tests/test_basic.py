import pytest
from applications import basic

def test_basic_bignum():
    assert basic.inc(209876) == 209877