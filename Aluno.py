
class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome

    def presenca(self) -> str:
        return f'O aluno {self.nome} está presente'
