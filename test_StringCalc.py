from StringCalc import *

def test_empty_string_returns_zero():
    assert StringCalc().add("") == 0

def test_single_number_string_returns_value():
    assert StringCalc().add("1") == 1

def test_two_number_string_returns_sum():
    assert StringCalc().add("1,2") == 3

def test_large_number_of_large_numbers_returns_sum():
    assert StringCalc().add("100,53,-8,65,3541") == 3751

def test_should_return_sum_when_numbers_are_separated_by_newline():
    assert StringCalc().add("1\n2,3") == 6

def test_should_return_sum_for_user_defined_separator():
    assert StringCalc().add("//;\n1;2") == 3

def test_should_return_sum_for_long_user_defined_separator():
    assert StringCalc().add("//;;\n1;;2") == 3
