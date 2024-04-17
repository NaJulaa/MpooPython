class Aluno:
    def __init__(self, nome, matricula, data_nascimento, endereco):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Endereço: {self.endereco}"

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return f"Curso: {self.nome}, Código: {self.codigo}"

class Endereco:
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"Endereço: {self.rua}, {self.numero}, {self.cidade}, {self.estado}, CEP: {self.cep}"

class Disciplina:
    def __init__(self, nome, codigo, professor, sala):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor
        self.sala = sala

    def __str__(self):
        return f"Disciplina: {self.nome}, Código: {self.codigo}, Professor: {self.professor}, Sala: {self.sala}"

class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Professor: {self.nome}, Matrícula: {self.matricula}"

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def __str__(self):
        return f"Sala: {self.numero}, Capacidade: {self.capacidade}"

endereco1 = Endereco("Rua ABC", "123", "Cidade A", "Estado X", "12345-678")
curso1 = Curso("Ciência da Computação", "CC001")
professor1 = Professor("João Silva", "P001")
sala1 = Sala("101", 50)

aluno1 = Aluno("Maria Souza", "2000-01-01", curso1, endereco1)
disciplina1 = Disciplina("Introdução à Programação", "IP001", professor1, sala1)

print(aluno1)
print(disciplina1)