import sys
sys.path.append(sys.path[0][:-4])
import readDataFile
import unittest
import os

class TestCart(unittest.TestCase):

    # set the path to make program path be adapatable for different os
    path = os.getcwd() + '/cart-json/cart-4560.json'

    # initialise the testing data
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

    # test each function then check if the return value matches the expected result
    def test_readDataFile(self):
        self.assertEqual(readDataFile.readDataFile(self.path), self.fileData)

if __name__ == '__main__':
    unittest.main()
