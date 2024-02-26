
class Aula:
    def __init__(self, professor, assunto, alunos) -> None:
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno) -> None:
        self.alunos.append(aluno)

    def listar_presenca(self):
        s = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.nome}:'
        for aluno in self.alunos:
            s += f'\n{aluno.presenca()}'
