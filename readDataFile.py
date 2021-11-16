import json
import sys

def readDataFile(path):
    # Using try..catch to prevent raising error
    try:
        with open(path) as f:
            # Using load to parse the file
            data1 = json.load(f)
            path.read(data1)
            return data1
    except:
        print('Please check the file path')
        # Raise the error to ask put the correct file path
        sys.exit(0)