import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7de5c75865d1fc1f77d93abd67ba431a'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '7481'

def test_status_code():
    response_list_of_pokemons = requests.get(url = f'{URL}/trainers')
    assert response_list_of_pokemons.status_code == 200
 
 
def test_my_name():
    response_my_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_my_name.json()['data'][0]['trainer_name'] == 'TYawn'

 


    


