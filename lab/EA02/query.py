from database import Database

db = Database(
    'neo4j+s://866c64e8.databases.neo4j.io',
    'neo4j',
    'bFpcJvndreeqWEjuf-SmmqCxDNj9GprFlQNVna7bdxU'
)
db.reset_db()


query = 'MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf;'
parameters = {"name": "Renzo"}

resutls = db.execute_query(query, parameters)

ano_nasc, cpf = resutls[0]['ano_nasc'], resutls[0]['cpf']

print('Questão 01\n')
print("\na - Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.")
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
print(f'\t- ano_nasc: {ano_nasc}')
print(f'\t- cpf: {cpf}')
print('-' * 50)


query = 'MATCH (t:Teacher) WHERE t.name STARTS WITH "M" RETURN t.name AS name, t.cpf AS cpf;'

results = [
    {
        'name': row['name'],
        'cpf': row['cpf']
    }
    for row in db.execute_query(query)
]

print('\nb - Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.')
print(f'\t- query')
print(f'\t\t{query}')

for row in results:
    print('-' * 50)
    for key, value in row.items():
        print(f'\t- {key}: {value}')
print('-' * 50)

query = 'MATCH (c:City) RETURN c.name AS name;'

results = [r['name'] for r in db.execute_query(query)]

print('\nc - Busque pelos nomes de todas as cidades “City” e retorne-os.')
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
for i in results:
    print(f'\t- {i}')
print('-' * 50)

query = 'MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address;'

results = [
    {
        'name': row['name'],
        'address': row['address']
    }
    for row in db.execute_query(query)
]

print('\nd - Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.')
print(f'\t- query')
print(f'\t\t{query}')
for row in results:
    print('-' * 50)
    for key, value in row.items():
        print(f'\t- {key}: {value}')
print('-' * 50)

query = 'MATCH (t:Teacher) RETURN min(t.ano_nasc) AS velho_ano_nasc, max(t.ano_nasc) AS novo_ano_nasc;'

velho_ano_nasc, novo_ano_nasc = db.execute_query(
    query)[0]['velho_ano_nasc'], db.execute_query(query)[0]['novo_ano_nasc']

print('\n\nQuestão 02')
print('\na - Encontre o ano de nascimento do professor mais jovem e do professor mais velho.')
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
print(f'\t- Mais jovem: {"novo_ano_nasc"}')
print(f'\t- Mais velho: {"velho_ano_nasc"}')
print('-' * 50)

query = 'MATCH (c:City) RETURN avg(c.population) as media_pop;'
result = db.execute_query(query)[0]['media_pop']

print('\nb - Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.')
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
print(f'\t- Média: {result}')
print('-' * 50)

query = 'MATCH (c:City {cep: "37540-000"}) RETURN replace(c.name, "a", "A") AS name_replaced;'
result = db.execute_query(query)[0]['name_replaced']

print('\nc - Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A”.')
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
print(f'\t- {result}')
print('-' * 50)

query = 'MATCH (n:Teacher) RETURN substring(n.name, 3, 1) AS letra_3;'
results = [result['letra_3'] for result in db.execute_query(query)]

print('\nd - Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.')
print(f'\t- query')
print(f'\t\t{query}')
print('-' * 50)
for result in results:
    print(f'\t- {result}')
print('-' * 50)
