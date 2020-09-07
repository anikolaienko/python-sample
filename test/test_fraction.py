import pytest
from src.fraction import Fraction

def test_repr():
    assert repr(Fraction(4, 5)) == "Fraction(4, 5, False)"
    assert repr(Fraction(6, 8, True)) == "Fraction(6, 8, True)"
    assert eval(repr(Fraction(5, 9))) == Fraction(5, 9)
    assert eval(repr(Fraction(1, 4, True))) == Fraction(1, 4, True)

