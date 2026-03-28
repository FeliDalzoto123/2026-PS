# ===============================================
# SISTEMA DE CADASTRO DE UM CLUBE, TIME OU EVENTO
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 12 - criação do projeto.
# Autor      : Felipe Dalzoto e Fabricio Candido
# Data       : 28/03/2026
# Repositorio: https://github.com/FeliDalzoto123/2026-PS
# ================================================
#
# DESCRIÇÃO:
# Criar um sistema para cadastrar um clube, time 
# ou evento para gerenciamento de campeonato.
# =================================================

ARQUIVO = "teste.txt"

# Vai criar uma pasta se não existir
def criar_arquivo():
    try:
        with open(ARQUIVO, "x") as f:
            pass
    except FileExistsError:
        pass
    
# Cadastro Dos Clubes, Times ou Eventos
def cadastro():
    usuario = input("Novo usuário: ")
    senha = input("Nova senha: ")
    print()

    with open(ARQUIVO, "a") as f:
        f.write(f"{usuario};{senha}\n")

    print("Usuário cadastrado com sucesso!")

# Listar usuários
def listar_usuarios():
    with open(ARQUIVO, "r") as f:
        print("\nUsuários cadastrados:")
        for linha in f:
            usuario, senha = linha.strip().split(";")
            print(f"- {usuario}")

# Login
def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    print()

    with open(ARQUIVO, "r") as f:
        for linha in f:
            u, s = linha.strip().split(";")
            if usuario == u and senha == s:
                print("Login realizado com sucesso!")
                return

    print("Usuário ou senha inválidos!")

# Menu Principal
def menu():
    criar_arquivo()

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Login")
        print("4 - Sair")
        print()

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            login()
        elif opcao == "4":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida!")

# Executar sistema
menu()