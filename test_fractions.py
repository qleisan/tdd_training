from fractions import Fraction


def test_should_print_fractions_correctly():
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(2, 1)) == "2"
    assert str(Fraction(2)) == "2"
    assert str(Fraction(3, 3)) == "1"
    assert str(Fraction(2, 4)) == "1/2"


def test_should_support_comparison_for_equality():
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(1, 2) != Fraction(1, 3)
    assert Fraction(1, 2) == Fraction(2, 4)


def test_should_add_fractions_with_common_denominator():
    assert str(Fraction(1, 5) + Fraction(2, 5)) == "3/5"


def test_should_add_fractions_with_different_denominator():
    assert str(Fraction(1, 3) + Fraction(1, 4)) == "7/12"


def test_should_add_fractions_into_irreducible_form():
    assert str(Fraction(1, 2) + Fraction(1, 2)) == "1"
