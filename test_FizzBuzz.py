from fizzbuzz import fizzbuzz, print_fizzbuzz_1_100


def test_should_return_FizzBuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(7) == 7
    assert fizzbuzz(8) == 8
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(11) == 11
    assert fizzbuzz(12) == "Fizz"
    assert fizzbuzz(13) == 13
    assert fizzbuzz(14) == 14
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(16) == 16


def test_should_print_something_from_1_to_100(mocker):
    m = mocker.MagicMock()

    print_fizzbuzz_1_100(m)
    m.assert_called()
    m.assert_called_with("FizzBuzz")
