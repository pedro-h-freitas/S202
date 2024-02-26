
class Professor:
    def __init__(self, nome) -> None:
        self.nome = nome

    def ministrar_aula(self, assunto) -> str:
        return f'O professor {self.nome} está ministrando uma aula sobro o assunto {assunto}'
