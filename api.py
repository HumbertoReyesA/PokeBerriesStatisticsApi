import json
import requests
from itertools import groupby
from statistics import mean
from statistics import median
from statistics import variance
from typing import List
from flask import Flask
from flask import Response
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

response: dict = {
    "berries_names": None,
    "min_growth_time": None,
    "median_growth_time": None,
    "max_growth_time": None,
    "variance_growth_time": None,
    "mean_growth_time": None,
    "frequency_growth_time": None
}

def get_berries_count() -> int:
    response: Response = requests.get('https://pokeapi.co/api/v2/berry')
    response = response.json()
    return response.get('count')

def get_berries_data(count: int=1) -> List[dict]:
    url: str = 'https://pokeapi.co/api/v2/berry/'
    return [requests.get(url + str(id)).json() for id in range(1, count + 1)]

def get_growth_time_list(collection: List[dict]) -> List[int]:
    return [_dict.get('growth_time') for _dict in collection]

def get_berries_names(collection: List[dict]) -> List[str]:
    return [_dict.get('name') for _dict in collection]

def get_growth_time_freq(collection: List[int]) -> dict[str, int]:
    return {key: len(list(group)) for key, group in groupby(sorted(collection))}
    

class PokeBerries(Resource):

    def get(self):
        # Comments
        berries_count: int = get_berries_count() 
        berries_data: list = get_berries_data(count=berries_count)
        berries_names: list = get_berries_names(collection=berries_data)
        growth_time: list = get_growth_time_list(collection=berries_data)
    
        response["berries_names"] = berries_names
        response["min_growth_time"] = min(growth_time)
        response["median_growth_time"] = median(growth_time)
        response["max_growth_time"] = max(growth_time)
        response["variance_growth_time"] = variance(growth_time)
        response["mean_growth_time"] = mean(growth_time)
        response["frequency_growth_time"] = get_growth_time_freq(collection=growth_time)
        api_response: str = json.dumps(response)
        return Response(response=api_response, content_type='application/json')

api.add_resource(PokeBerries, '/allBerryStats')

if __name__ == '__main__':
    app.run(debug=True)