import entidades
import servicos 

def only_numbers_and_dot(input_str):
    for char in input_str:
        if not char.isdigit() and char != '.':
            return False
    return True

def ler_dados_disciplina():
    codigo = input("Digite o código da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    semestre = input("Digite o semestre da disciplina (yyyy.p): ")
    carga_horaria = input("Digite a carga horária da disciplina: ")
    while (not carga_horaria.isdigit()):
        carga_horaria = input("Digite um número inteiro: ")
    dias = input("Digite os dias (1..6) da semana que a disciplina ocorre (separados por vírgula): ")
    horarios = input("Digite os horários (1..6) da disciplina (separados por vírgula): ")
    disciplina = entidades.Disciplina(codigo, nome, semestre, carga_horaria, dias, horarios)
    return disciplina

def ler_dados_professor():
    codigo = input("Digite o código do professor: ")
    while (not codigo.isdigit()):
        codigo = input("Digite um número inteiro: ")
    nome = input("Digite o nome do professor: ")
    professor = entidades.Professor(codigo, nome)
    return professor

def ler_dados_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    return entidades.Aluno(matricula, nome, curso)

def ler_dados_nota(codigo_disciplina, matricula_aluno):
    valor = 0
    try: 
        valor = input('Digite o valor da nota: ')
        while (not only_numbers_and_dot(valor)):
            valor = (input("Digite um valor real: "))
        valor = float(valor)
    except Exception as ex:
        print(f'Entrada inválida! - {str(ex)}')
    nota = entidades.Nota(codigo_disciplina, matricula_aluno, valor)
    return nota

def mostrar_dados_disciplina(disciplina):
    print(f"Código: {disciplina.codigo}")
    print(f"Nome: {disciplina.nome}")
    print(f"Semestre: {disciplina.semestre}")
    print(f"Carga Horária: {disciplina.carga_horaria}")
    print(f"Dias: {disciplina.dias}")
    print(f"Horários: {disciplina.horarios}")
    print("Professores:")
    for professor in disciplina.professores:
        print(f"\t{professor}")
    print("Alunos:")
    for aluno in disciplina.alunos:
        print(f"\t{aluno}")

def mostrar_dados_professor(professor):
    print(f'{professor.codigo}, {professor.nome}')

def mostrar_dados_aluno(aluno):
    print(f'{aluno.matricula}, {aluno.nome}, {aluno.curso}')
    if len(aluno.get_notas()) > 0:
        for nota in aluno.get_notas():
            print(nota.valor)

def mostrar_disciplinas(disciplinas):
    for disciplina in disciplinas:
        mostrar_dados_disciplina(disciplina)

def mostrar_professores(professores):
    for professor in professores:
        mostrar_dados_professor(professor)

def mostrar_alunos(alunos):
    for aluno in alunos:
        mostrar_dados_aluno(aluno)

def mostrar_notas(notas, disciplinas, alunos):
    for nota in notas:
        nome_disciplina = servicos.pesquisar_por_codigo(nota.codigo_disciplina, disciplinas)
        nome_aluno = servicos.pesquisa_aluno_matricula(nota.matricula_aluno, alunos)
        print(f'{nome_disciplina}, {nome_aluno}, {nota.valor}')

def menu_principal():
    print('--- Menu Principal ---')
    print('1 - Disciplinas')
    print('2 - Professores e Alunos')
    print('3 - Salvar dados em arquivo')
    print('4 - Sair')
    opcao = input("Digite a opção desejada: ")
    while (not opcao.isdigit()):
        opcao = input("Digite um número válido: ")
        if opcao not in ['1','2','3','4']:
            print('Opção inválida!')
    return opcao

def menu_disciplinas():
    print('--- Disciplinas ---')
    print('1 - Lista discplinas')
    print('2 - Nova disciplina')
    print('3 - Associa professor a disciplina')
    print('4 - Matricula aluno em disciplina')
    print('5 - Cadastrar nota de aluno em disciplina')
    print('6 - Listar notas de alunos')
    print('7 - Voltar')
    opcao = input("Digite a opção desejada: ")
    while (not opcao.isdigit()):
        opcao = input("Digite um número válido: ")
        if opcao not in ['1','2','3','4','5','6','7']:
            print('Opção inválida!')
    return opcao

def menu_professores_alunos():
    print('--- Professores e Alunos ---')
    print('1 - Listar professores') 
    print('2 - Listar alunos')
    print('3 - Voltar')
    opcao = input("Digite a opção desejada: ")
    while (not opcao.isdigit()):
        opcao = input("Digite um número válido: ")
        if opcao not in ['1','2','3']:
            print('Opção inválida!')
    return opcao