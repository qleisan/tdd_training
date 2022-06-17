from StringCalc import *

def test_test_empty_string_returns_zero():
    assert StringCalc().add("") == 0

def test_test_single_number_string_returns_value():
    assert StringCalc().add("1") == 1

def test_test_two_number_string_returns_sum():
    assert StringCalc().add("1,2") == 3

def test_test_large_number_of_large_numbers_returns_sum():
    assert StringCalc().add("100,53,-8,65,3541") == 3751
