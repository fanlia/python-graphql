
from waitress import serve
from app import app, port
 
print("server started at http://localhost:{}".format(port))
serve(app, host='0.0.0.0', port=port)
