from database import Database


class GameDatabase:
    def __init__(self, database: Database):
        self._db = database
        self._players_id = self._get_players_id()
        self._matches_id = self._get_matches_id()

    def _generate_id(self, id_list):
        return len(id_list)

    def _get_players_id(self):
        query = "MATCH (p:Player) RETURN p.id AS players_id"
        results = self._db.execute_query(query)
        return [result["players_id"] for result in results]

    def _get_matches_id(self):
        query = "MATCH (m:Match) RETURN m.id AS matches_id"
        results = self._db.execute_query(query)
        return [result["matches_id"] for result in results]

    def create_player(self, name):
        id = self._generate_id(self._players_id)

        query = "CREATE (:Player {id: $id, name: $name})"
        parameters = {"id": id, "name": name}

        self._db.execute_query(query, parameters)
        self._players_id.append(id)

    def update_player(self, id, new_name):
        query = "MATCH (p:Player {id: $id}) SET p.name = $new_name"
        parameters = {"id": id, "new_name": new_name}
        self._db.execute_query(query, parameters)

    def delete_player(self, id):
        query = "MATCH (p:Player {id: $id}) DETACH DELETE p"
        parameters = {"id": id}
        self._db.execute_query(query, parameters)

    def create_match(self, players: list[tuple[str, int]]):
        id = self._generate_id(self._matches_id)

        query = "CREATE (:Match {id: $id})"
        parameters = {"id": id}

        self._db.execute_query(query, parameters)
        self._matches_id.append(id)

        winner = ""
        winner_score = 0
        for player_name, player_score in players:
            query = "MATCH (p:Player {name: $name}), (m:Match {id: $id}) CREATE (p)-[:PLAYED {score: $score}]->(m)"
            parameters = {
                "name": player_name,
                "id": id,
                "score": player_score
            }
            self._db.execute_query(query, parameters)

            if winner_score < player_score:
                winner_score = player_score
                winner = player_name

        self.update_match_winner(id, winner)

    def update_match_winner(self, id, winner):
        query = "MATCH (m:Match {id: $id}) SET m.winner = $winner"
        parameters = {"id": id, "winner": winner}
        self._db.execute_query(query, parameters)

    def delete_player(self, id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        parameters = {"id": id}
        self._db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self._db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self, id):
        query = "MATCH (m:Match {id: $id}) RETURN m.winner AS winner"
        parameters = {"id": id}
        winner = self._db.execute_query(query, parameters)

        query = "MATCH (m:Match {id: $id})<-[P:PLAYED]-(p:Player) RETURN p.name AS player, P.score AS score;"
        results = self._db.execute_query(query, parameters)

        match = {
            "id": id,
            "winner": winner[0]['winner'],
            "players_score": [
                {
                    result['player']: result["score"]
                } for result in results
            ]
        }

        return match

    def get_player_hist(self, player_id):
        query = "MATCH (p:Player {id: $id})-[P:PLAYED]->(m:Match) RETURN m.id AS match_ID, m.winner = p.name AS winner, P.score AS score"
        parameters = {"id": player_id}
        results = self._db.execute_query(query, parameters)

        history = [
            {
                'match_ID': result['match_ID'],
                'winner': result['winner'],
                'score': result['score']
            } for result in results
        ]
        return history
