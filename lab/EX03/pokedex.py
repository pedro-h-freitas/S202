from database import Database
from write_a_json import write_a_json


class Pokedex:
    def __init__(self, database: Database):
        self._database = database

    def get_pokemon_by_name(self, name: str):
        query = self._database.collection.find({'name': name})
        write_a_json(query, "pokemon_by_name")

    def get_pokemons_by_types(self, types: list):
        query = self._database.collection.find({"type": {"$in": types}})
        write_a_json(query, "pokemons_by_types")

    def get_pokemons_weak_againt(self, weakness: list):
        query = self._database.collection.find(
            {"weakness": {"$all": weakness}})
        write_a_json(query, "pokemons_weak_againt")

    def get_pokemons_with_one_weakness(self):
        query = self._database.collection.find({"weaknesses": {"$size": 1}})
        write_a_json(query, "pokemons_with_one_weakness")

    def get_pokemons_with_no_evolutions(self):
        query = self._database.collection.find(
            {"next_evolution": {"$exists": False}})
        write_a_json(query, "pokemons_with_no_evolutions")
