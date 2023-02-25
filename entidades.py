# Definicao das classes do programa

# Regras mais importantes: 
'''
Disciplina tem uma lista de professores
Disciplina tem uma lista de alunos
Nota é associada a disciplina e aluno
'''

class Disciplina:
    def __init__(self, codigo, nome, semestre, carga_horaria, dias, horarios, professores=None, alunos=None):
        self.codigo = codigo
        self.nome = nome
        self.semestre = semestre
        self.carga_horaria = carga_horaria
        self.dias = dias
        self.horarios = horarios
        if professores is not None: 
            self.professores = professores
        else:
            self.professores = list()
        if alunos is not None:
            self.alunos = alunos
        else:
            self.alunos = list()

    def get_professores(self):
        return self.professores

    def get_alunos(self):
      return self.alunos

    def set_professores(self, professores):
      self.professores = professores

    def set_alunos(self, alunos):
      self.alunos = alunos

    def add_professor(self, professor):
      self.professores.append(professor)

    def add_aluno(self, aluno):
      self.alunos.append(aluno)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Professor:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Aluno:
    notas=[]
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.notas = list()

    def add_nota(self,nota):
      self.notas.append(nota)

    def get_notas(self):
      return self.notas

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

class Nota:
    def __init__(self, codigo_disciplina, matricula_aluno, valor):
        self.codigo_disciplina = codigo_disciplina
        self.matricula_aluno = matricula_aluno
        self.valor = valor