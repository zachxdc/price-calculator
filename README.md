# Redbubble Coding Test - Price Calculator

## Description

The program is to calculate the total price of all items in the cart. It can load and read the JSON files to get the base price for each product which has its specific options. Then using the specific formula to calulate the total price for the cart.

## Prerequisite

- Python 3.6.8+

## Installation

1. Clone the project: 

   `git clone https://github.com/bobcqs/folder-structure-with-file-count`

2. Enter the project folder: 

   `cd price-calculator`

3. Install project dependencies: 

   python 3.6.8 (Follow instruction here: https://www.python.org/downloads/release/python-368/)

4. Check current python version

   `python3 --version`

## Running instruction

- Run with python command:

    `python3  PriceCalculator.py [cart_json_path] [base_price_json_path]`

- Run one unit test for the program:

    `python3 [test_file_path]`

- Run all unit tests in a directory:

    `python3 -m unittest [test_directory]`

## File Structure

    .
    ├── base-prices
    │   ├──  base-prices.json
    ├── cart-json
    │   ├──  cart-4560.json
    │   ├── cart-9363.json
    │   ├── cart-9500.json
    │   ├── cart-11356.json
    ├── schema
    │   ├──  base-prices.schema.json
    │   ├──  cart.schema.json
    ├── test
    │   ├──  test_basePrice.py
    │   ├──  test_cart.py
    │   ├──  test_PriceCalculator.py
    │   ├──  test_readDataFile.py
    ├── base_price.py
    ├── cart.py
    ├── PriceCalculator.py
    ├── readDataFile.py
    └── README.md

## Solution design concept
1. The program is to calculte the total price for all products in a cart, so the main I/O file, `PriceCalculator.py` is create to output the total price for each cart

2. The product base price and products in the cart are saved in the JSONfile, so create the `readDatafile.py` to load json file

3. Item has its product type, options, and base price. Each item may have different options and different base prices. (For example, a white large hoodie and a white small hoodie may have different prices.) To solve the problem the function in `basePrice.py` file is to get all prices and all options for the product, then match them to get the exact base price

4.  The function in `cart.py` is to calculate total price for one product in the cart and total price of all products in the cart

5. Apply the built in unittest for automation test 
