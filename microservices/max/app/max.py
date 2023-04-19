from flask import Flask
from flask_restful import Resource, Api
import math

def maximum(n1, n2):
    return max(n1,n2)

class Add(Resource):
    def get(self, a, b):
        return {'result': max(int(a) , int(b))}

app = Flask(__name__)
api = Api(app)

api.add_resource(Add, '/<a>/<b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )