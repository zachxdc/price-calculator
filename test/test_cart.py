import sys
sys.path.append(sys.path[0][:-4])
import basePrice

cartObject = {
    'options': {
        'color': 'red',
        'size': 'small'
    }
}

def test_getOneProductPrice():
    assert 1 == 1


def test_getCartTotalPrices():
    assert 1 == 1
