import json
import sys

def readDataFile(path):
    # Using try..catch to prevent raising error
    try:
        with open(path) as f:
            # Using load to parse the file
            data = json.load(f)
            return data
    except:
        print('Please check the file path')
        # Raise the error to ask put the correct file path
        sys.exit(0)