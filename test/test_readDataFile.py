import sys
sys.path.append(sys.path[0][:-4])
import readDataFile
import unittest
import os

class TestCart(unittest.TestCase):

    path = os.getcwd() + '/cart-json/cart-4560.json'
    
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

    def test_readDataFile(self):
        self.assertEqual(readDataFile.readDataFile(self.path), self.fileData)

if __name__ == '__main__':
    unittest.main()
