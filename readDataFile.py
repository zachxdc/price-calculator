import json
import sys

def readDataFile(path):
    try:
        with open(path) as f:
            data = json.load(f)
            return data
    except:
        print('Please check the file path')
        sys.exit(0)