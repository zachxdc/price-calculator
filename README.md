# Redbubble Coding Test - Price Calculator

## Description

The program is to calculate the total price of all items in the cart

## Prerequisite
- Python 3.0.0 or later

## Installation
- aaa

## Running instruction

- Run with python command

        python3  PriceCalculator.py [cart_json_path] [base_price_json_path]

- Run one unit test for the program

        python3 [test_file_path]

- Run all unit tests in a directory

        python3 -m unittest [test_directory]

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