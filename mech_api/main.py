import json
import pathlib
import random
from flask import Flask, send_file
from flask_restplus import Resource, Api


app = Flask(__name__, static_url_path='/static')
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
        return send_file(img_path)


if __name__ == '__main__':
    app.run(debug=True)