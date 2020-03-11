import json
import pathlib
import random
from flask import Flask, send_file
from flask_restplus import Resource, Api
from flask_cors import CORS


app = Flask(__name__, static_url_path='/static')
CORS(app)
api = Api(app)
app_folder = pathlib.Path(__file__).parent.absolute()

with open(f"{app_folder}/mechs.json", "r+") as fp:
    mechs = json.load(fp)["mechs"]

# Handy name_mapping
name_mapping = {
    mech["name"] : mech["imgPath"]
    for mech in mechs
}


@api.route('/<string:mech_id>')
class MechResource(Resource):
    def get(self, mech_id):
        """ Get a specific mech by name
        """
        print(name_mapping[mech_id])
        return send_file(name_mapping[mech_id])

@api.route('/random')
class RandomResource(Resource):
    def get(self):
        """ Get a random mech
        """
        img_path = random.choice(mechs)['imgPath']
        return img_path

# TODO: Depracate this
@api.route('/random', defaults={'count': 1})
@api.route('/random/<int:count>')
class RandomResource(Resource):
    def get(self, count):
        """ Get a random mech
        """
        img_paths = [
            random.choice(mechs)['imgPath']
            for _ in range(count)
        ]

        return img_paths

# TODO: add tests for this
# TODO: make v1/ a prefix instead of on each route, aka proper views
@api.route('/v1/random', defaults={'count': 1})
@api.route('/v1/random/<int:count>')
class RandomMechResource(Resource):
    def get(self, count):
        """ Get a random mech
        """
        # TODO: make sure there are no duplicates
        # TODO: error when count > number of mechs that exist
        mech_data = [
            random.choice(mechs)
            for _ in range(count)
        ]

        return mech_data


if __name__ == '__main__':
    app.run(debug=True)