import requests
from itertools import groupby
from statistics import mean
from statistics import median
from statistics import variance
from typing import List
from flask import Flask
from flask import jsonify
from flask_restful import Resource
from flask_restful import abort
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Mold object
response: dict = {
    "berries_names": None,
    "min_growth_time": None,
    "median_growth_time": None,
    "max_growth_time": None,
    "variance_growth_time": None,
    "mean_growth_time": None,
    "frequency_growth_time": None
}

def abort_if_status_code_is_not_200(status_code: int, res_url: str):
    """ Abort the api process if the status code is not 200[OK]"""
    if status_code == 403:
        abort(403, message=f"The resource '{res_url}' is forbidden.")
    elif status_code == 404:
        abort(404, message=f"The requested url '{res_url}' was not found on the server.")

def get_berries_count(res_url: str) -> int:
    """ Get th count of all available berries in the specific resoure"""
    response = requests.get(res_url)
    abort_if_status_code_is_not_200(status_code=response.status_code, res_url=res_url)
    response = response.json()
    return response.get('count')

def get_berries_data(count: int=1, res_url: str='') -> List[dict]:
    """ Get the complete data for the specific resource and a specific number of berries"""
    berries_data = []
    for id in range(1, count + 1):
        response = requests.get(res_url + str(id))
        abort_if_status_code_is_not_200(status_code=response.status_code, res_url=res_url)
        berries_data.append(response.json())
    return berries_data

def get_growth_time_list(collection: List[dict]) -> List[int]:
    """ Get all the values for the growth_time field"""
    return [_dict.get('growth_time') for _dict in collection]

def get_berries_names(collection: List[dict]) -> List[str]:
    """ Get all the names of all berries"""
    return [_dict.get('name') for _dict in collection]

def get_growth_time_freq(collection: List[int]) -> dict[str, int]:
    """ Get the frequency for each growth_time value"""
    return {key: len(list(group)) for key, group in groupby(sorted(collection))}
    

class PokeBerries(Resource):
    """ Class resource regarding to poke berries"""

    def get(self, url: str='https://pokeapi.co/api/v2/berry/'):
        """ Get all the statistics for the poke berries"""
        # Getting all the data from berries with the methods below
        berries_count: int = get_berries_count(res_url=url) 
        berries_data: list = get_berries_data(count=berries_count, res_url=url)
        berries_names: list = get_berries_names(collection=berries_data)
        growth_time: list = get_growth_time_list(collection=berries_data)
        # Response in dictionary format
        response["berries_names"] = berries_names
        response["min_growth_time"] = min(growth_time)
        response["median_growth_time"] = median(growth_time)
        response["max_growth_time"] = max(growth_time)
        response["variance_growth_time"] = variance(growth_time)
        response["mean_growth_time"] = mean(growth_time)
        response["frequency_growth_time"] = get_growth_time_freq(collection=growth_time)
        # Serializing the response object as JSON
        api_response = jsonify(response)
        api_response.status_code = 200
        api_response.content_type = 'application/json'
        return api_response

api.add_resource(PokeBerries, '/allBerryStats')