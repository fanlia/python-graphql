import os
from flask import Flask
from flask_cors import CORS
from strawberry.flask.views import GraphQLView

from schema import schema

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema),
)

if __name__ == "__main__":
    port = os.getenv('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
