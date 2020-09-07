import pytest
import decimal

def test_context():
    ctx = decimal.getcontext()
    ctx.prec = 3
    assert str(decimal.Decimal(1) / decimal.Decimal(3)) == "0.333"