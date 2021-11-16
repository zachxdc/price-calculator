import sys
sys.path.append(sys.path[0][:-4])
import PriceCalculator
<<<<<<< HEAD
import pytest


@pytest.mark.parametrize("cartPath,expected",
                         [("../cart-json/cart-4560.json", "45.60"), ("../cart-json/cart-9363.json", "93.63"),
                             ("../cart-json/cart-9500.json", "95.00"), ("../cart-json/cart-11356.json", "113.56")]
                         )
def test_execute(cartPath, expected):
    sys.argv = ['PriceCalculator.py', cartPath,
                '../base-prices/base-prices.json']
    main = PriceCalculator.Main()
    assert main.execute() == expected
=======

def test_checkParams():
    assert 1 == 1

def test_execute():
    assert 1 == 1
>>>>>>> 58e8bcf1316240572372132d35972abc057a45c0
