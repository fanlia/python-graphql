
from load_models import sys, printjson

from test import test

result = {
    'data': test(),
}

printjson(result)

