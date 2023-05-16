from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class PokeBerries(Resource):

    def get(self):
        response = requests.get('https://pokeapi.co/api/v2/berry/')
        print("test")
        return response.json()

api.add_resource(PokeBerries, '/allBerryStats')

if __name__ == '__main__':
    app.run(debug=True)