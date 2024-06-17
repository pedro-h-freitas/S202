import redis 

redis_conn = redis.Redis(
    host="...", 
    port=19861,
    username="default", # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="...", # use your Redis password
    decode_responses=True
)

# redis_conn.hset("product:2", mapping={
#     "nome": "Macbook",
#     "preco": 12999.99,
#     "marca": "Apple",
#     "descricao": "Um notebbok simples de entrada"
# })

# redis_conn.lpush("estoque", "poduct:1","product:2")

redis_conn.lrem("estoque", 1,"poduct:1" )
# redis_conn.lpush("estoque", "product:1")

tamanho_estoque = redis_conn.llen("estoque")

estoque = redis_conn.lrange("estoque", 0, tamanho_estoque-1)
print(estoque)
for produto in estoque:
    print(redis_conn.hget(produto, "nome"))
    print(redis_conn.hget(produto, "preco"))
    print()