from fractions import Fraction


def test_fractions_print_correctly():
    assert str(Fraction(1, 2)) == "1/2"
    # don't reduce fractions to their lowest terms
    assert str(Fraction(3, 3)) == "3/3"


def test_fractions_are_equal():
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(1, 2) != Fraction(1, 3)
    assert Fraction(1, 2) == Fraction(2, 4)


def test_add_fractions_with_common_denominator():
    assert Fraction(1, 5) + Fraction(2, 5) == Fraction(3, 5)


def test_add_fractions_with_different_denominator():
    assert Fraction(1, 3) + Fraction(1, 4) == Fraction(7, 12)


def test_added_fractions_should_be_in_irreducible_form():
    assert str(Fraction(1, 2) + Fraction(1, 2)) == "1/1"
