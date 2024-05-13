from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

cloud_config= {
  'secure_connect_bundle': 'secure-connect-dbiot.zip'
}

with open("dbiot-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace("ksiot")

carro = input("CAR: ")
query = f"SELECT nome, estante, quantidade FROM peca WHERE carro = '{carro}' ALLOW FILTERING;"
print(query)
result = session.execute(query)

for r in result:
    print(r)
