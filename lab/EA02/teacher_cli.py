from teacher_crud import TeacherCRUD


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print(f'Commands: {[cmd for cmd in self.commands.keys()].append('quit')}')
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD: TeacherCRUD):
        super().__init__()
        self._teacherCRUD = teacherCRUD
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input('Nome do professor: ')
        ano_nasc = input('Ano de nascimento: ')
        cpf = input('Cpf: ')

        self._teacherCRUD.create(name, ano_nasc, cpf)

        print('Professor criado!')

    def read_teacher(self):
        name = input('Nome do professor: ')

        teacher = self._teacherCRUD.read(name)

        if teacher:
            print('Professor encontrado:')
            for key, value in teacher.items():
                print(f'\t- {key}: {value}')
        else:
            print('Professor não encontrado!')

    def update_teacher(self):
        name = input('Nome do professor: ')
        newCpf = input('Novo CPF: ')

        teacher = self._teacherCRUD.update(name, newCpf)

        if teacher:
            print('Professor atualizado:')
            for key, value in teacher.items():
                print(f'\t- {key}: {value}')
        else:
            print('Professor não encontrado!')

    def delete_teacher(self):
        nome = input("Nome do professor: ")
        self._teacherCRUD.delete(nome)

        print('Professor deletado')

    def run(self):
        print("Bem-vindo ao CLI do professor!")
        super().run()
