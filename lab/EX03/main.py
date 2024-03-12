from pokedex import Pokedex
from database import Database
from write_a_json import write_a_json

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

name = "Bulbasaur"
pokedex.get_pokemon_by_name(name)

types = ["Water", "Poison"]
pokedex.get_pokemons_by_types(types)

weakness = ["Electric", "Ground", "Psychic"]
pokedex.get_pokemons_weak_againt(weakness)

pokedex.get_pokemons_with_one_weakness()

pokedex.get_pokemons_with_no_evolutions()
