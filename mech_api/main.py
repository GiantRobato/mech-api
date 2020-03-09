from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/<mech_id>')
class MechResource(Resource):
    def get(self, mech_id):
        return {"id": mech_id}


if __name__ == '__main__':
    app.run(debug=True)