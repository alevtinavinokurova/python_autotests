import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6ac54c97b191f334b1b108e7f7e382d0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '29710'


def test_ststus_code():
    response = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code ==200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['trainer_id'] == TRAINER_ID 