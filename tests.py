import pytest
from api import get_berries_count
from api import get_berries_data
from api import get_berries_names
from api import get_growth_time_freq
from api import get_growth_time_list
from api import abort_if_status_code_is_not_200
from api import PokeBerries
from api import app
from flask import Response


@pytest.fixture(autouse=True)
def berries_data():
    """Data from sixteen berries"""
    return [{'firmness': {'name': 'soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/2/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 3, 'id': 1, 'item': {'name': 'cheri-berry', 'url': 'https://pokeapi.co/api/v2/item/126/'}, 'max_harvest': 5, 'name': 'cheri', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'fire', 'url': 'https://pokeapi.co/api/v2/type/10/'}, 'size': 20, 'smoothness': 25, 'soil_dryness': 15}, {'firmness': {'name': 'super-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/5/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 3, 'id': 2, 'item': {'name': 'chesto-berry', 'url': 'https://pokeapi.co/api/v2/item/127/'}, 'max_harvest': 5, 'name': 'chesto', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'water', 'url': 'https://pokeapi.co/api/v2/type/11/'}, 'size': 80, 'smoothness': 25, 'soil_dryness': 15}, {'firmness': {'name': 'very-soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/1/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 10}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 3, 'id': 3, 'item': {'name': 'pecha-berry', 'url': 'https://pokeapi.co/api/v2/item/128/'}, 'max_harvest': 5, 'name': 'pecha', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'electric', 'url': 'https://pokeapi.co/api/v2/type/13/'}, 'size': 40, 'smoothness': 25, 'soil_dryness': 15}, {'firmness': {'name': 'hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/3/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 10}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 3, 'id': 4, 'item': {'name': 'rawst-berry', 'url': 'https://pokeapi.co/api/v2/item/129/'}, 'max_harvest': 5, 'name': 'rawst', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'grass', 'url': 'https://pokeapi.co/api/v2/type/12/'}, 'size': 32, 'smoothness': 25, 'soil_dryness': 15}, {'firmness': {'name': 'super-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/5/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 10}], 'growth_time': 3, 'id': 5, 'item': {'name': 'aspear-berry', 'url': 'https://pokeapi.co/api/v2/item/130/'}, 'max_harvest': 5, 'name': 'aspear', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'ice', 'url': 'https://pokeapi.co/api/v2/type/15/'}, 'size': 50, 'smoothness': 25, 'soil_dryness': 15}, {'firmness': {'name': 'very-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/4/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 10}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 10}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 10}], 'growth_time': 4, 'id': 6, 'item': {'name': 'leppa-berry', 'url': 'https://pokeapi.co/api/v2/item/131/'}, 'max_harvest': 5, 'name': 'leppa', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'fighting', 'url': 'https://pokeapi.co/api/v2/type/2/'}, 'size': 28, 'smoothness': 20, 'soil_dryness': 15}, {'firmness': {'name': 'super-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/5/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 10}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 10}], 'growth_time': 4, 'id': 7, 'item': {'name': 'oran-berry', 'url': 'https://pokeapi.co/api/v2/item/132/'}, 'max_harvest': 5, 'name': 'oran', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'poison', 'url': 'https://pokeapi.co/api/v2/type/4/'}, 'size': 35, 'smoothness': 20, 'soil_dryness': 15}, {'firmness': {'name': 'hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/3/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 10}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 10}], 'growth_time': 4, 'id': 8, 'item': {'name': 'persim-berry', 'url': 'https://pokeapi.co/api/v2/item/133/'}, 'max_harvest': 5, 'name': 'persim', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'ground', 'url': 'https://pokeapi.co/api/v2/type/5/'}, 'size': 47, 'smoothness': 20, 'soil_dryness': 15}, {'firmness': {'name': 'super-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/5/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 10}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 10}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 12, 'id': 9, 'item': {'name': 'lum-berry', 'url': 'https://pokeapi.co/api/v2/item/134/'}, 'max_harvest': 5, 'name': 'lum', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'flying', 'url': 'https://pokeapi.co/api/v2/type/3/'}, 'size': 34, 'smoothness': 20, 'soil_dryness': 8}, {'firmness': {'name': 'very-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/4/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 10}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 10}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 10}], 'growth_time': 8, 'id': 10, 'item': {'name': 'sitrus-berry', 'url': 'https://pokeapi.co/api/v2/item/135/'}, 'max_harvest': 5, 'name': 'sitrus', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'psychic', 'url': 'https://pokeapi.co/api/v2/type/14/'}, 'size': 95, 'smoothness': 20, 'soil_dryness': 7}, {'firmness': {'name': 'soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/2/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 15}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 5, 'id': 11, 'item': {'name': 'figy-berry', 'url': 'https://pokeapi.co/api/v2/item/136/'}, 'max_harvest': 5, 'name': 'figy', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'bug', 'url': 'https://pokeapi.co/api/v2/type/7/'}, 'size': 100, 'smoothness': 25, 'soil_dryness': 10}, {'firmness': {'name': 'hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/3/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 15}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 5, 'id': 12, 'item': {'name': 'wiki-berry', 'url': 'https://pokeapi.co/api/v2/item/137/'}, 'max_harvest': 5, 'name': 'wiki', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'rock', 'url': 'https://pokeapi.co/api/v2/type/6/'}, 'size': 115, 'smoothness': 25, 'soil_dryness': 10}, {'firmness': {'name': 'hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/3/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 15}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 5, 'id': 13, 'item': {'name': 'mago-berry', 'url': 'https://pokeapi.co/api/v2/item/138/'}, 'max_harvest': 5, 'name': 'mago', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'ghost', 'url': 'https://pokeapi.co/api/v2/type/8/'}, 'size': 126, 'smoothness': 25, 'soil_dryness': 10}, {'firmness': {'name': 'super-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/5/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 15}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 5, 'id': 14, 'item': {'name': 'aguav-berry', 'url': 'https://pokeapi.co/api/v2/item/139/'}, 'max_harvest': 5, 'name': 'aguav', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'dragon', 'url': 'https://pokeapi.co/api/v2/type/16/'}, 'size': 64, 'smoothness': 25, 'soil_dryness': 10}, {'firmness': {'name': 'soft', 'url': 'https://pokeapi.co/api/v2/berry-firmness/2/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 0}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 0}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 15}], 'growth_time': 5, 'id': 15, 'item': {'name': 'iapapa-berry', 'url': 'https://pokeapi.co/api/v2/item/140/'}, 'max_harvest': 5, 'name': 'iapapa', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'dark', 'url': 'https://pokeapi.co/api/v2/type/17/'}, 'size': 223, 'smoothness': 25, 'soil_dryness': 10}, {'firmness': {'name': 'very-hard', 'url': 'https://pokeapi.co/api/v2/berry-firmness/4/'}, 'flavors': [{'flavor': {'name': 'spicy', 'url': 'https://pokeapi.co/api/v2/berry-flavor/1/'}, 'potency': 10}, {'flavor': {'name': 'dry', 'url': 'https://pokeapi.co/api/v2/berry-flavor/2/'}, 'potency': 10}, {'flavor': {'name': 'sweet', 'url': 'https://pokeapi.co/api/v2/berry-flavor/3/'}, 'potency': 0}, {'flavor': {'name': 'bitter', 'url': 'https://pokeapi.co/api/v2/berry-flavor/4/'}, 'potency': 0}, {'flavor': {'name': 'sour', 'url': 'https://pokeapi.co/api/v2/berry-flavor/5/'}, 'potency': 0}], 'growth_time': 2, 'id': 16, 'item': {'name': 'razz-berry', 'url': 'https://pokeapi.co/api/v2/item/141/'}, 'max_harvest': 10, 'name': 'razz', 'natural_gift_power': 60, 'natural_gift_type': {'name': 'steel', 'url': 'https://pokeapi.co/api/v2/type/9/'}, 'size': 120, 'smoothness': 20, 'soil_dryness': 35}]

@pytest.fixture(autouse=True)
def growth_time_coll():
    """Growth time data collection"""
    return [3, 3, 3, 3, 3, 4, 4, 4, 12, 8, 5, 5, 5, 5, 5, 2]

@pytest.fixture(autouse=True)
def mocked_response():
    """Final response"""
    return {
        "berries_names": [
            "cheri", "chesto", "pecha", "rawst", "aspear", "leppa", "oran", "persim", 
            "lum", "sitrus", "figy", "wiki", "mago", "aguav", "iapapa", "razz", 
            "bluk", "nanab", "wepear", "pinap", "pomeg", "kelpsy", "qualot", "hondew", 
            "grepa", "tamato", "cornn", "magost", "rabuta", "nomel", "spelon", "pamtre", 
            "watmel", "durin", "belue", "occa", "passho", "wacan", "rindo", "yache", 
            "chople", "kebia", "shuca", "coba", "payapa", "tanga", "charti", "kasib", 
            "haban", "colbur", "babiri", "chilan", "liechi", "ganlon", "salac", "petaya", 
            "apicot", "lansat", "starf", "enigma", "micle", "custap", "jaboca", "rowap"
        ], 
        "min_growth_time": 2, 
        "median_growth_time": 15.0, 
        "max_growth_time": 24, 
        "variance_growth_time": 62.47197420634921, 
        "mean_growth_time": 12.859375, 
        "frequency_growth_time": {
            "2": 5, 
            "3": 5, 
            "4": 3, 
            "5": 5, 
            "6": 4, 
            "8": 7, 
            "12": 1, 
            "15": 5, 
            "18": 17, 
            "24": 12
        }
    }

@pytest.fixture(autouse=True)
def poke_berries_instance():
    """Resource instance to handle the get method"""
    poke_berrie = PokeBerries()
    return poke_berrie


def test_abort_if_status_code_is_not_200_passes():
    """Test the 200[OK] status code"""
    assert abort_if_status_code_is_not_200(status_code=200, res_url='https://www.fakedata.com') == None

def test_abort_if_status_code_is_not_200_fails():
    """Test the 403[Forbidden] status code"""
    with pytest.raises(Exception):
        abort_if_status_code_is_not_200(status_code=403, res_url='https://www.fakedata.com')

def test_get_berries_count_passes():
    """Test that there are 64 berries available"""
    assert get_berries_count(res_url='https://pokeapi.co/api/v2/berry/') == 64

def test_get_berries_count_not_found():
    """Raise an exception because of the wrong url"""
    with pytest.raises(Exception):
        get_berries_count(res_url='https://pokeapi.co/api/v2/berr/')

def test_get_berries_data_passes():
    """Test that the final object is a list with 3 elements"""
    berries_data = get_berries_data(count=3, res_url="https://pokeapi.co/api/v2/berry/")
    assert isinstance(berries_data, list)
    assert len(berries_data) == 3

def test_get_berries_data_fails():
    """Raise an exception because of the wrong url and a missing count"""
    with pytest.raises(Exception):
        berries_data = get_berries_data(count=3, res_url="https://pokeapi.co/api/v2/ber/")
        assert len(berries_data) == 2

def test_get_growth_time_list_passes(berries_data):
    """Test final object is a list containing 16 elements"""
    growth_time_list = get_growth_time_list(collection=berries_data)
    assert isinstance(growth_time_list, list) == True
    assert len(growth_time_list) == 16

def test_get_growth_time_list_fails(berries_data):
    """Test final object is not a dictionary and it does not have 64 elements"""
    growth_time_list = get_growth_time_list(collection=berries_data)
    assert isinstance(growth_time_list, dict) == False
    assert len(growth_time_list) != 64

def test_get_berries_names_passes(berries_data):
    """Test the final object is a list containing 16 elements and checks the last name on it"""
    berries_names = get_berries_names(berries_data)
    assert isinstance(berries_names, list) == True
    assert len(berries_names) == 16
    assert berries_names[-1] == 'razz'

def test_get_berries_names_fails(berries_data):
    """Test the final object is not a tuple containing 32 elements and checks the that first name is wrong"""
    berries_names = get_berries_names(berries_data)
    assert isinstance(berries_names, tuple) == False
    assert len(berries_names) != 32
    assert berries_names[0] != 'cherio'

def test_get_growth_time_freq_passes(growth_time_coll):
    """Test the final object is a dictionary and the value of the key 2"""
    frequency = get_growth_time_freq(growth_time_coll)
    assert isinstance(frequency, dict) == True
    assert frequency.get(2) == 1

def test_get_growth_time_freq_fails(growth_time_coll):
    """Test the final object is not a string and the value of the key 4 is not 4"""
    frequency = get_growth_time_freq(growth_time_coll)
    assert isinstance(frequency, str) == False
    assert frequency.get(4) != 4

def test_get_poke_berries_passes(poke_berries_instance):
    """Test the final response object is an instance of the Response class"""
    with app.app_context():
        response = poke_berries_instance.get(url='https://pokeapi.co/api/v2/berry/')
        assert isinstance(response, Response) == True

def test_get_poke_berries_fails(poke_berries_instance):
    """Raise an exception because of the incomplete url"""
    with pytest.raises(Exception):
        poke_berries_instance.get(url='https://pokeapi.co/api/v2/be')
    