import sys
sys.path.append(sys.path[0][:-4])
import readDataFile

path = '../cart-json/cart-4560.json'

fileData = [
    {
        "product-type": "hoodie",
        "options": {
            "size": "small",
            "colour": "white",
            "print-location": "front"
        },
        "artist-markup": 20,
        "quantity": 1
    }
]


def test_readDataFile():
    assert readDataFile.readDataFile(path) == fileData