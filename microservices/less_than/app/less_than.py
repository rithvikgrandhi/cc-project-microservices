from flask import Flask
from flask_restful import Resource, Api

class LESS_THAN(Resource):
    def get(self, a, b):
        if a < b:
            return {'result': "True"}
        else:
            return {'result': "False"}

app = Flask(__name__)
api = Api(app)

api.add_resource(LESS_THAN, '/<a>/<b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )