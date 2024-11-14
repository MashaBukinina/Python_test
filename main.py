import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7de5c75865d1fc1f77d93abd67ba431a'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }


Body_Create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = Body_Create_pokemon)
print(response_create.text)

ID = response_create.json()['id']

Body_Rename_pokemon = {

    "pokemon_id": ID,
    "name": "generate",
    "photo_id": -1
}

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = Body_Rename_pokemon)
print(response_rename.text)

Body_Catch_pokemon = {

    "pokemon_id": ID

}

response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = Body_Catch_pokemon)
print(response_catch_pokemon.text)



