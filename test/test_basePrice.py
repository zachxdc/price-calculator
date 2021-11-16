import sys
sys.path.append(sys.path[0][:-4])
import basePrice

cartObject = {
    'options': {
        'color': 'red',
        'size': 'small'
    }
}

def test_getProductPrices():
    assert 1 == 1


def test_getCartOptions():
    assert basePrice.getCartOptions(cartObject) == ['red', 'small']