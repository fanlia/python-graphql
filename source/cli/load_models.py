
import os
import sys
directory = os.path.abspath(os.path.join(__file__, '../../models'))
sys.path.append(directory)

import json

def printjson(result):
    print('__')
    print(json.dumps(result))
