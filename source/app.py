import os
from flask import Flask
from flask_cors import CORS
from strawberry.flask.views import GraphQLView

from schema import schema
from restful import restful

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

restful(app)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema),
)

port = os.getenv('PORT', 5000)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
