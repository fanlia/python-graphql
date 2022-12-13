
from models.test import test

def restful(app):
    @app.route('/hello')
    def hello_world():
       return "hello world"

    @app.route('/test')
    def test_route():
       return test()
