from flask import Flask
from flask_restful import Resource, Api

class EXP(Resource):
    def get(self, a, b):
        return {'result': int(a) ** int(b)}

app = Flask(__name__)
api = Api(app)

api.add_resource(EXP, '/<a>/<b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )