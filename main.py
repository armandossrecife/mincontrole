import telas
import servicos
import dao
import testes

def sanity_testes():
    # Popula dados de testes
    print('Popula dados de testes')
    disciplinas, professores, alunos, notas = testes.popula_dados()
    print('Salva dados de teste no arquivo mini-ca.dat')
    testes.teste_salvar_arquivo(disciplinas, professores, alunos, notas, 'mini-ca.dat')
    print('Dados salvos com sucesso no arquivo : mini-ca.dat')
    print('Recuper dados de teste do arquivo mini-ca.dat')
    disciplinas, professores, alunos, notas = testes.teste_recupera_dados_arquivo('mini-ca.dat')
    print('Dados recuperados com sucesso do arquivo : mini-ca.dat')
    # Mostra dados de uma disciplina
    print('Mostra dados de uma disciplina')
    for each in disciplinas:
        telas.mostrar_dados_disciplina(each)

def menu_principal(disciplinas, professores, alunos, notas):
  while True:
    opcao = telas.menu_principal()
    if opcao == "1":
        # Chama o sub-menu disciplinas
        menu_disciplinas(disciplinas, professores, alunos, notas)
    elif opcao == "2":
        # Chama o sub-menu professores e alunos
        menu_professores_alunos(professores, alunos)
    elif opcao == "3":
        # Salva os dados em arquivo
        dao.salvar_dados_arquivo(disciplinas, professores, alunos, notas, 'mini-ca.dat')
        print('Dados salvos com sucesso no arquivo mini-ca.dat')
    elif opcao == "4":
        # Encerra o programa
        break
    else:
        print("Opção inválida.")

def menu_disciplinas(disciplinas, professores, alunos, notas):
    while True:
        opcao = telas.menu_disciplinas()
        if opcao == "1":
            print('--- Listar disciplinas ---')
            telas.mostrar_disciplinas(disciplinas)
        elif opcao == "2":
            print('--- Cadastra disciplina ---')
            disciplina = telas.ler_dados_disciplina()
            if servicos.pesquisar_por_codigo(disciplina.codigo, disciplinas) is None:
                disciplinas.append(disciplina)
                print('Disciplina cadastrada com sucesso!')
            else:
                print('A disciplina já existe!')
        elif opcao == "3":
            print('--- Cadastra professor em disciplina ---')
            codigo_professor = input('Código do professor: ')
            codigo_disciplina = input('Código da disciplina: ')
            professor = servicos.pesquisar_professor_por_codigo(codigo_professor, professores)
            disciplina = servicos.pesquisar_por_codigo(codigo_disciplina, disciplinas)
            if (disciplina is not None) and (professor is not None):
                if servicos.cadastrar_professor_disciplina(professor, disciplina):
                    print(f'Professor {professor.nome} associado a disciplina {disciplina.nome} com sucesso!')
                else:
                    print(f'Professor {professor.nome} já está associado a disciplina {disciplina.nome}')
            else:
                print(f'Código de disciplina ou professor inválido!')
        elif opcao == "4":
            print('--- Matricular aluno em disciplina ---')
            matricula_aluno = input('Matrícula do aluno: ')
            codigo_disciplina = input('Código da disciplina: ')
            aluno = servicos.pesquisa_aluno_matricula(matricula_aluno, alunos)
            disciplina = servicos.pesquisar_por_codigo(codigo_disciplina, disciplinas)
            if (disciplina is not None) and (aluno is not None):
                if servicos.matricular_aluno(disciplina, aluno):
                    print(f'Aluno {aluno.nome} matriculado com sucesso na disciplina {disciplina.nome}!')
                else:
                    print(f'O aluno {aluno.nome} já está matriculado na disciplina {disciplina.nome}.')
            else:
                print(f'Código de disciplina ou aluno inválido!')
        elif opcao == "5":
            print('--- Cadastra nota ---')
            codigo_disciplina = input('Código da disciplina: ')
            matricula_aluno = input('Matrícula do aluno: ')
            disciplina = servicos.pesquisar_por_codigo(codigo_disciplina, disciplinas)
            aluno = servicos.pesquisa_aluno_matricula(matricula_aluno, alunos)
            if (disciplina is not None) and (aluno is not None):
                nota = telas.ler_dados_nota(codigo_disciplina, matricula_aluno)
                aluno.add_nota(nota)
                notas.append(nota)
            else:
                print('Disciplina ou matrícula inválida!')    
        elif opcao == "6": 
            print('--- Listar notas ---')
            telas.mostrar_notas(notas, disciplinas, alunos)
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")

def menu_professores_alunos(professores, alunos):
    while True:
        opcao = telas.menu_professores_alunos()
        if opcao == "1":
            print('--- Listar professores ---')
            telas.mostrar_professores(professores)
        elif opcao == "2":
            print('--- Listar alunos ---')
            telas.mostrar_alunos(alunos)
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

# popula dados de exemplo
#sanity_testes()
disciplinas, professores, alunos, notas = dao.recuperar_dados_arquivo('mini-ca.dat')
menu_principal(disciplinas, professores, alunos, notas)