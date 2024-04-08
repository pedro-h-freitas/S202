from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable


def get_pets(tx):
    query = """
        MATCH (n:Pet) RETURN n.nome AS pets;
    """
    try:
        result = tx.run(query)
        return [row['pets'] for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise


def get_childs(tx, parent):
    query = """
        MATCH ({nome: $parent})-[:PAI_DE]->(n) RETURN n.nome AS child;
    """
    try:
        result = tx.run(query, parent=parent)
        return [row['child'] for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise


def get_relationship_time(tx, person):
    query = """
        MATCH ({nome: $person})-[r:NAMORADO_DE]->() RETURN r.tempo AS relationship_time;

    """
    try:
        result = tx.run(query, person=person)
        return [row['relationship_time'] for row in result]

    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise


def main():
    uri = "neo4j+s://866c64e8.databases.neo4j.io"
    user = "neo4j"
    password = "bFpcJvndreeqWEjuf-SmmqCxDNj9GprFlQNVna7bdxU"

    driver = GraphDatabase.driver(uri, auth=(user, password))

    while True:
        print('Cliente de Consulta')
        print('0 - Sair')
        print('1 - Quem são os Pets?')
        print('2 - Filhos de ...?')
        print('3 - ... namora a quanto tempo?')

        op = input('Opção: ')
        print()

        if op == '0':
            driver.close()
            break

        elif op == '1':
            with driver.session() as session:
                result = session.execute_read(get_pets)
            print('Os pets são: ')
            for pet in result:
                print(f'    {pet}')
            print()

        elif op == '2':
            parent = input('Filhos de: ')

            with driver.session() as session:
                result = session.execute_read(get_childs, parent)

            if len(result) == 0:
                print(f'{parent} não tem filhos\n')

            else:
                for child in result:
                    print(f'    {child}')
                print()

        elif op == '3':
            person = input('Pessoa: ')

            with driver.session() as session:
                result = session.execute_read(get_relationship_time, person)

            if len(result) == 0:
                print(f'{person} não namora\n')

            else:
                print(f'{person} namora há {result[0]} anos\n')

        else:
            print('Opção Inválida!')

        input('[ENTER] para continuar')
        print()


if __name__ == '__main__':
    main()
