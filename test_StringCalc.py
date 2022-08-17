from io import StringIO
from unittest.mock import patch
from StringCalc import *
import pytest

def test_empty_string_returns_zero():
    assert StringCalc().add("") == 0

def test_single_number_string_returns_value():
    assert StringCalc().add("1") == 1

def test_two_number_string_returns_sum():
    assert StringCalc().add("1,2") == 3

def test_large_number_of_large_numbers_returns_sum():
    assert StringCalc().add("100,53,0,65,3541") == 3759

def test_should_return_sum_when_numbers_are_separated_by_newline():
    assert StringCalc().add("1\n2,3") == 6

def test_should_return_sum_for_user_defined_separator():
    assert StringCalc().add("//;\n1;2") == 3

def test_should_return_sum_for_long_user_defined_separator():
    assert StringCalc().add("//;;\n1;;2") == 3

def test_should_throw_exception_for_negative_numbers_1():
    # passes if Exception (or any subclass) is raised
    with pytest.raises(Exception):
        StringCalc().add("-1")

#@pytest.mark.skip(reason="no reason")
def test_should_throw_exception_for_negative_numbers_2():
    # passes if Exception (or any subclass) is raised AND the message is correct
    with pytest.raises(Exception) as e:
        StringCalc().add("-1")
    assert str(e.value) == "Negatives not allowed: -1"

def test_should_throw_exception_for_negative_numbers_3():
    # passes if CustomException (or any subclass) is raised
    with pytest.raises(CustomException):
        StringCalc().add("-1")

def test_should_throw_exception_for_negative_numbers_4():
    # passes if CustomException (or any subclass) is raised AND the message is correct
    with pytest.raises(CustomException) as e:
        StringCalc().add("-1")
    assert str(e.value) == "Negatives not allowed: -1"

def test_should_print_numbers_and_sum_on_display_1():
    # github copilot gave this... ;-)
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        StringCalc().add("1,2,3")
        assert fake_stdout.getvalue() == "1 + 2 + 3 = 6\n"
