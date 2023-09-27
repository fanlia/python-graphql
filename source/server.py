
import time
import sys
from waitress import serve
from app import app, port
 
print("server started at http://localhost:{} [{}][python:{}]".format(port, time.asctime(), sys.version))
serve(app, host='0.0.0.0', port=port)
