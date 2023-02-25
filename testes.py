import entidades
import dao
import servicos

def popula_dados():
    disciplinas, professores, alunos, notas = [], [], [], []

    # Criando os professores
    professor1 = entidades.Professor('1', "João")
    professor2 = entidades.Professor('2', "Maria")
    professor3 = entidades.Professor('3', "Ana")
    # Criando os alunos
    aluno1 = entidades.Aluno('1', "Pedro", "Engenharia")
    aluno2 = entidades.Aluno('2', "Julia", "Administração")
    aluno3 = entidades.Aluno('3', "Lucas", "Medicina")
    aluno4 = entidades.Aluno('4', "Clara", "Engenharia")
    
    # Criando a disciplina
    disciplina = entidades.Disciplina('1', "Programação", "2022/1", 60, [1, 3, 5], [2, 4, 6], [professor1, professor2], [aluno1, aluno2, aluno3])
    disciplina2 = entidades.Disciplina('2', "Engenharia de Software", "2022/1", 90, [1, 3, 5], [3, 5], [professor3], [aluno1, aluno4])

    # Adicionando notas para cada aluno
    aluno1.add_nota(entidades.Nota(disciplina.codigo, aluno1.matricula, 7)) 
    aluno1.add_nota(entidades.Nota(disciplina.codigo, aluno1.matricula, 8))
    aluno1.add_nota(entidades.Nota(disciplina.codigo, aluno1.matricula, 9))
    aluno2.add_nota(entidades.Nota(disciplina.codigo, aluno2.matricula, 6))
    aluno2.add_nota(entidades.Nota(disciplina.codigo, aluno2.matricula, 7))
    aluno2.add_nota(entidades.Nota(disciplina.codigo, aluno2.matricula, 5))
    aluno3.add_nota(entidades.Nota(disciplina.codigo, aluno3.matricula, 10))
    aluno3.add_nota(entidades.Nota(disciplina.codigo, aluno3.matricula, 9))
    aluno3.add_nota(entidades.Nota(disciplina.codigo, aluno3.matricula, 8))

    aluno1.add_nota(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9)) 
    aluno1.add_nota(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9))
    aluno1.add_nota(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9))
    aluno4.add_nota(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))
    aluno4.add_nota(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))
    aluno4.add_nota(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))

    # Populando as listas de disciplinas, professores, alunos e notas
    disciplinas.append(disciplina)
    disciplinas.append(disciplina2)
    professores.append(professor1)
    professores.append(professor2)
    professores.append(professor3)
    alunos.append(aluno1)
    alunos.append(aluno2)
    alunos.append(aluno3)
    alunos.append(aluno4)
    notas.append(entidades.Nota(disciplina.codigo, aluno1.matricula, 7)) 
    notas.append(entidades.Nota(disciplina.codigo, aluno1.matricula, 8))
    notas.append(entidades.Nota(disciplina.codigo, aluno1.matricula, 9))
    notas.append(entidades.Nota(disciplina.codigo, aluno2.matricula, 6))
    notas.append(entidades.Nota(disciplina.codigo, aluno2.matricula, 7))
    notas.append(entidades.Nota(disciplina.codigo, aluno2.matricula, 5))
    notas.append(entidades.Nota(disciplina.codigo, aluno3.matricula, 10))
    notas.append(entidades.Nota(disciplina.codigo, aluno3.matricula, 9))
    notas.append(entidades.Nota(disciplina.codigo, aluno3.matricula, 8))

    notas.append(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9)) 
    notas.append(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9))
    notas.append(entidades.Nota(disciplina2.codigo, aluno1.matricula, 9))
    notas.append(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))
    notas.append(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))
    notas.append(entidades.Nota(disciplina2.codigo, aluno4.matricula, 10))

    return disciplinas, professores,alunos, notas

def teste_salvar_arquivo(disciplinas, professores, alunos, notas, arquivo):
    dao.salvar_dados_arquivo(disciplinas, professores, alunos, notas, arquivo)

def teste_recupera_dados_arquivo(arquivo):
    return dao.recuperar_dados_arquivo(arquivo)