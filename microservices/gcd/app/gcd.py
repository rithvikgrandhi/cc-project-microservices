from flask import Flask
from flask_restful import Resource, Api

from math import gcd

class GCD(Resource):
    def get(self, a, b):
        return {'result': gcd(int(a), int(b))}

app = Flask(__name__)
api = Api(app)

api.add_resource(GCD, '/<a>/<b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )