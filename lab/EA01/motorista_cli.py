from motorista_dao import MotoristaDAO
from passageiro import Passageiro
from motorista import Motorista
from corrida import Corrida


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO: MotoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        notas = 0
        n_corridas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('\tNota: '))
            distancia = float(input('\tDistancia: '))
            valor = float(input('\tValor: '))

            print('\tPassageiro')
            nome_passageiro = str(input('\t\tNome: '))
            documento_passageiro = str(input('\t\tDocumento: '))

            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Mais uma corrida? (S/N) ').lower() == 'n':
                break

        nota = int(notas / n_corridas)
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.create_motorista(motorista)

    def read_motorista(self):
        id = input("Id motorista: ")
        motorista = self.motoristaDAO.read_motorista_by_id(id)
        if motorista:
            print(f'Nota: {motorista["nota"]}')
            print('Corridas: ')
            for corrida in motorista["corridas"]:
                passageiro = corrida["passageiro"]

                print(f'\tNota: {corrida["nota"]}')
                print(f'\tDistancia: {corrida["distancia"]}')
                print(f'\tValor: {corrida["valor"]}')

                print('\tPassageiro: ')
                print(f'\t\tNome: {passageiro["nome"]}')
                print(f'\t\tDocumento: {passageiro["documento"]}')

    def update_motorista(self):
        id = input("Id motorista: ")

        corridas = []
        notas = 0
        n_corridas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('\tNota: '))
            distancia = float(input('\tDistancia: '))
            valor = float(input('\tValor: '))

            print('\tPassageiro')
            nome_passageiro = str(input('\t\tNome: '))
            documento_passageiro = str(input('\t\tDocumento: '))

            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Mais uma corrida? (S/N) ').lower == 'n':
                break

        nota = int(notas / n_corridas)
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Id motorista: ")
        self.motoristaDAO.delete_motorista(id)

    def run(self):
        print("Bem-vindo ao CLI do motorista!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()
