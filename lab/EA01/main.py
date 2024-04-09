from motorista_cli import MotoristaCLI
from motorista_dao import MotoristaDAO

if __name__ == '__main__':
    motoristaDAO = MotoristaDAO('EA01', 'Motoristas')
    cli = MotoristaCLI(motoristaDAO)
    cli.run()
