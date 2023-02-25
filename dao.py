import entidades

def salvar_dados_arquivo(disciplinas, professores, alunos, notas, arquivo):
    try:
        with open(arquivo, 'w') as f:
            for disciplina in disciplinas:
                f.write(f"DISCIPLINA:{disciplina.codigo},{disciplina.nome},{disciplina.semestre},{disciplina.carga_horaria}#{''.join(str(disciplina.dias))};{''.join(str(disciplina.horarios))}\n")
                for professor in disciplina.get_professores():
                    f.write(f"DISCIPLINA-PROFESSOR:{professor.codigo},{professor.nome},{disciplina.codigo}\n")
                for aluno in disciplina.get_alunos():
                    f.write(f"DISCIPLINA-ALUNO:{aluno.matricula},{aluno.nome},{aluno.curso},{disciplina.codigo}\n")
            for professor in professores:
                f.write(f"PROFESSOR:{professor.codigo},{professor.nome}\n")
            for aluno in alunos:
                f.write(f"ALUNO:{aluno.matricula},{aluno.nome},{aluno.curso}\n")
            for nota in notas:
                f.write(f"NOTA:{nota.codigo_disciplina},{nota.matricula_aluno},{nota.valor}\n")
    except FileExistsError:
        print(f"Arquivo {arquivo} não encontrado")        

def recuperar_dados_arquivo(arquivo):
    disciplinas = []
    professores = []
    alunos = []
    notas = []
    try:
        with open(arquivo, "r") as f:
            linhas = f.readlines()
            for linha in linhas:
                tipo, dados = linha.split(":")
                dados = dados.strip()
                if tipo == "DISCIPLINA":
                    dados1, dados2 = dados.split("#")
                    codigo, nome, semestre, carga_horaria = dados1.split(",")
                    dias, horarios = dados2.split(";")
                    # Converte string para list
                    dias = dias.strip('][').split(', ')
                    horarios = horarios.strip('][').split(', ')
                    disciplina = entidades.Disciplina(codigo, nome, semestre, carga_horaria, dias, horarios)
                    disciplinas.append(disciplina)
                elif tipo == "DISCIPLINA-PROFESSOR":
                    codigo_professor, nome_professor, codigo_disciplina = dados.split(',')
                    professor = entidades.Professor(codigo_professor, nome_professor)
                    disciplinas[-1].add_professor(professor)
                elif tipo == "DISCIPLINA-ALUNO":
                    codigo_aluno, nome_aluno, curso, codigo_disciplina = dados.split(',')
                    aluno = entidades.Aluno(codigo_aluno, nome_aluno, curso)
                    disciplinas[-1].add_aluno(aluno)
                elif tipo == "PROFESSOR":
                    codigo, nome = dados.split(",")
                    professor = entidades.Professor(codigo, nome)
                    professores.append(professor)
                elif tipo == "ALUNO":
                    matricula, nome, curso = dados.split(",")
                    aluno = entidades.Aluno(matricula, nome, curso)
                    alunos.append(aluno)
                elif tipo == "NOTA":
                    codigo_disciplina, matricula_aluno, valor = dados.split(",")
                    nota = entidades.Nota(codigo_disciplina, matricula_aluno, float(valor))
                    notas.append(nota)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")

    return disciplinas, professores, alunos, notas