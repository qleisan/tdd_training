class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        gcd = self._gcd()
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def __add__(self, other):
        ret = None
        if self.denominator == other.denominator:
            ret = Fraction(self.numerator + other.numerator, self.denominator)
        else:
            ret = Fraction(
                self.numerator * other.denominator + self.denominator * other.numerator,
                self.denominator * other.denominator,
            )
        return ret

    def __eq__(self, other):
        # reduce both fractions to their lowest terms
        a = Fraction(self.numerator, self.denominator) + Fraction(0, 1)
        b = Fraction(other.numerator, other.denominator) + Fraction(0, 1)
        return a.numerator == b.numerator and a.denominator == b.denominator

    def __str__(self):
        ret = ""
        if self.denominator == 1:
            ret = str(self.numerator)
        else:
            ret = f"{self.numerator}/{self.denominator}"
        return ret

    def _gcd(self):
        # find the greatest common divisor of the numerator and denominator
        # using Euclid's algorithm
        a = self.numerator
        b = self.denominator
        while b != 0:
            a, b = b, a % b
        return a
