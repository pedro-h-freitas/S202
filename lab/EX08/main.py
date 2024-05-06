from database import Database
from game_database import GameDatabase

db = Database(
    'neo4j+s://866c64e8.databases.neo4j.io',
    'neo4j',
    'bFpcJvndreeqWEjuf-SmmqCxDNj9GprFlQNVna7bdxU'
)
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("Pedro")
game_db.create_player("Yasmin")

game_db.create_match([("Pedro", 100), ("Yasmin", 200)])
game_db.create_match([("Pedro", 200), ("Yasmin", 100)])
game_db.create_match([("Pedro", 300), ("Yasmin", 250)])
game_db.create_match([("Pedro", 150), ("Yasmin", 200)])
game_db.create_match([("Pedro", 190), ("Yasmin", 270)])

print(game_db.get_players())
print(game_db.get_match(2))
print(game_db.get_player_hist(0))
