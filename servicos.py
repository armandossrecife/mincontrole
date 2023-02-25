# Dado um codigo retorna a disciplina
def pesquisar_por_codigo(codigo_disciplina, disciplinas):
    disciplina = None
    # percorre a lista de disciplinas para procurar o codigo correspondente
    for d in disciplinas:
        if codigo_disciplina == d.codigo:
            return d
    return disciplina

def pesquisar_professor_por_codigo(codigo_professor, professores):
    professor = None
    for p in professores:
        if codigo_professor == p.codigo:
            return p
    return professor

def pesquisa_aluno_matricula(matricula_aluno, alunos):
    aluno = None
    for a in alunos:
        if matricula_aluno == a.matricula:
            return a
    return aluno

def cadastrar_professor_disciplina(professor, disciplina):
    pode_cadastrar = True
    for p in disciplina.get_professores():
        if p.codigo == professor.codigo:
            pode_cadastrar = False
    if pode_cadastrar:
        disciplina.add_professor(professor)
    return pode_cadastrar

def matricular_aluno(disciplina, aluno):
    pode_matricular = True
    # Pesquisa se aluno jah esta na disciplina
    for a in disciplina.get_alunos():
        if aluno.matricula == a.matricula:
            pode_matricular = False
    if pode_matricular: 
        # pode matricular aluno
        disciplina.add_aluno(aluno)
    return pode_matricular

    