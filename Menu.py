def menu():
    print("----------Sistema Acadêmico----------")
    print(" ")
    print("Menu: ")
    print("Digite 1 para cadastrar o estudante.")
    print("Digite 2 para cadastrar as disciplinas.")
    print("Digite 3 para cadastrar as notas.")
    print("Digite 4 para situação da disciplina.")
    print("Digite 5 para situação do estudante.")
    print("Digite 0 para sair.")
    print(" ")
    opçao = int(input("Qual opção você deseja: "))
    print("-------------------------------------")
    if (opçao == 1):
        cadastrar_aluno()
    elif (opçao == 2):
        cadastrar_disciplina()
    elif (opçao == 3):
         cadastrar_nota()
    elif (opçao == 4):
         situaçao_disciplina()
    elif (opçao == 5):
         situaçao_estudante()   
    else:
         while():
              break
def cadastrar_aluno():
        print("----------Cadastrar Aluno----------")
        nome = str(input("Digite seu nome: "))
        while (len(nome) < 3):
             print("Nome Inválido")
             nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        while (idade < 3 or idade > 100):
             print("Idade Inválido")
             idade = int(input("Digite sua idade: "))
        CPF = str(input("Digite seu CPF: "))
        while (len(CPF) != 11):
             print("CPF Inválido")
             CPF = str(input("Digite seu CPF: "))
        telefone = str(input("Digite seu número de telefone: "))
        while (telefone != 11):
             print("Telefone Inválido")
             telefone = str(input("Digite seu número de telefone: "))
        nome_r = str(input("Digite o nome de um dos seus responsáveis: "))
        while (len(nome_r) < 3):
             print("Nome do Responsável Inválido")
             nome_r = str(input("Digite o nome de um dos seus responsáveis: "))
        menu()
menu()
"""def cadastrar_disciplina():
        print("----------Cadastrar Disciplina----------")
        l_disciplinas = []
        for i in range(5):
            disciplina = str(input("Digite a %d° discipplina: " %(i+1)))
            l_disciplinas.append(disciplina)
        print(l_disciplinas)
        menu()
def cadastrar_nota():
     print("----------Cadastrar Nota----------")
     import l_disciplinas
     l_notas = []
     for x in range(5):
          notas = float(input("Digite a sua nota em %s: " %(l_disciplinas[0])))
          l_notas.append(notas)
          l_disciplinas+= 1
     menu()
def situaçao_disciplina():
     import l_disciplinas
     import l_notas 
     for t in range (5):
          if ((l_notas in l_disciplinas[0] == 10) and (l_notas in l_disciplinas[0] < 11)):
               print("O aluno foi aprovado com distinção")
               print("Nota: "(l_notas[0]))
          elif ((l_notas in l_disciplinas[0] >= 6) and (l_notas in l_disciplinas[0] < 10)):
               print("O aluno foi aprovado")
               print("Nota: "(l_notas[0]))
          else:
               print("O aluno não foi aprovado")
               print("Nota: "(l_notas[0]))
     l_disciplinas+= 1
def situaçao_estudante():
     import l_notas
     if ((l_notas >= 6) and (l_notas < 11)):
          print("O aluno passou de ano direto")
          print("Notas: "(l_notas))
     elif((l_notas)):
menu()"""