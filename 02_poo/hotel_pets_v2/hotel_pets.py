'''
==================================================================
# ARQUIVO    : pet_v2.py
# Disciplina : Programação de Sistemas (2026-PS)
# Aula       : Aula 23 - Por que POO?
# Autor      : Felipe Dalzoto
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento
# Atividade  : Classe Pet
===================================================================
'''
import pickle

class Pet:
    def __init__(self, nome, especie, idade, vacinado, raca, peso): 

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.hospedagem = False
        self.raca = raca
        self.peso = peso
        self.vacinado = vacinado
        
    def exibir_dados(self):
        print("\n=== Dados do Pet ===")
        self.registrar_entrada()
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Raça: {self.raca}")
        print(f"Hospedagem: {'Sim' if self.hospedagem else 'Não'}")
        print(f"Vacinado: {self.vacinado}") 
    
    def registrar_entrada(self):
        self.hospedagem = True
        print(f"{self.nome} entrou no hotel.")
        
    def registrar_saida(self):
        self.hospedagem = False
        print(f"{self.nome} saiu do hotel.")
    
    def calcular_diaria(self):
        if not self.hospedagem:
            return 0
           
        if 1 <= self.idade <= 3:
            return 50.00
        elif 4 <= self.idade <= 10:
            return 60.00
        elif self.idade > 10:
            return 70.00
            
    def verificar_vacinacao(self):
        if self.vacinado.lower() == "sim":
            return "Vacinado."
        else:
            return "Não vacinado."

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"Peso atualizado para {self.peso} kg.")

        
    def emitir_resumo(self):
        self.resumo = (
            f"\n===== RESUMO DO PET =====\n"
            f"Nome: {self.nome}\n"
            f"Espécie: {self.especie}\n"
            f"Idade: {self.idade} anos\n"
            f"Raça: {self.raca}\n"
            f"Peso: {self.peso} kg\n"
            f"Vacinação: {self.verificar_vacinacao()}\n"
            f"Hospedagem: {'Sim' if self.hospedagem else 'Não'}\n"
            )
        print(self.resumo)
    
    def exibir_raca(self):
        return self.raca
    
# -----------------------------------
# ARQUIVOS
# -----------------------------------

ARQUIVO_TXT = "pets.txt"
ARQUIVO_BINARIO = "pets.dat"
    
def salvar_em_binario(pets):
    try:
        with open(ARQUIVO_BINARIO, "wb") as arquivo:
            pickle.dump(pets, arquivo)
    except Exception as e:
        print(f"Erro ao salvar dados binários: {e}")
        print("Dados binários carregados com sucesso!")
        return pets
    except FileNotFoundError:
        print("Arquivo binário não encontrado.")
    return []

def carregar_binario():
    try:
        with open(ARQUIVO_BINARIO, "rb") as arquivo:
            pets = pickle.load(arquivo)
        print("Dados binários carregados com sucesso!")
        return pets
    except FileNotFoundError:
        print("Arquivo binário não encontrado.")
        return []

def salvar_em_txt(pets):
    try:
        with open(ARQUIVO_TXT, "w") as arquivo:
            for pet in pets:
                arquivo.write(f"{pet.nome}, {pet.especie}, {pet.idade}, {pet.vacinado}, {pet.raca}, {pet.peso}\n")
    except Exception as e:
        print(f"Erro ao salvar dados em texto: {e}")
        print("Dados em texto salvos com sucesso!")

def listar_pets(lista_pets):
    if not lista_pets:
        print("Nenhum pet cadastrado.")
        return
    for pet in lista_pets:
        pet.exibir_dados()
        
def relatorio_hospedados(lista_pets):
    total = 0
    print("\n===== PETS HOSPEDADOS =====")
    encontrou = False
    for pet in lista_pets:
        if pet.hospedagem:
            encontrou = True
            diaria = pet.calcular_diaria()
            print(f"\nNome: {pet.nome}")
            print(f"Diária: R$ {diaria:.2f}")
            total += diaria
    if not encontrou:
        print("\nNenhum pet hospedado.")
    print(f"\nTOTAL DAS DIÁRIAS: R$ {total:.2f}")
    
def escolher_pet(lista_pets):
    if len(lista_pets) == 0:
        print("\nNenhum pet cadastrado.")
        return None
    print("\n===== PETS CADASTRADOS =====")

    for i, pet in enumerate(lista_pets):
        print(f"[{i}] {pet.nome}")
    try:
        indice = int(input("\nEscolha o número do pet: "))
        if 0 <= indice < len(lista_pets):
            return lista_pets[indice]
        else:
            print("Índice inválido.")
            return None
    except ValueError:
        print("Digite um número válido.")
        return None

def Menu():
    lista_pets = carregar_binario()
    while True:

        print("\n========= HOTEL PET =========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Buscar pet por nome")
        print("4 - Atualizar peso")
        print("5 - Resumo do pet")
        print("6 - Relatório de hospedagem")
        print("7 - Salvar em TXT")
        print("8 - Salvar em BINÁRIO")
        print("9 - Apagar Pet")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n===== CADASTRO =====")
            nome = input("Nome: ")
            especie = input("Espécie: ")
            idade = int(input("Idade: "))
            vacinado = input("Vacinado (sim/não): ")
            raca = input("Raça: ")
            peso = float(input("Peso: "))

            novo_pet = Pet(nome, especie, idade, vacinado, raca, peso)

            lista_pets.append(novo_pet)
            print(f"\n{nome} cadastrado com sucesso!")

        elif opcao == "2":
            listar_pets(lista_pets)
            
        elif opcao == "3":
            nome_busca = input("\nDigite o nome do pet para buscar: ")
            pet_encontrado = None
            for pet in lista_pets:
                if pet.nome.lower() == nome_busca.lower():
                    pet_encontrado = pet
                    break
            if pet_encontrado:
                pet_encontrado.exibir_dados()
            else:
                print("Pet não encontrado.")

        elif opcao == "4":
            pet = escolher_pet(lista_pets)
            if pet:
                novo_peso = float(input("Novo peso: "))
                pet.atualizar_peso(novo_peso)

        elif opcao == "5":
            pet = escolher_pet(lista_pets)
            if pet:
                pet.emitir_resumo()
            
        elif opcao == "6":
            relatorio_hospedados(lista_pets)

        elif opcao == "7":
            salvar_em_txt(lista_pets)

        elif opcao == "8":
            salvar_em_binario(lista_pets)

        elif opcao == "9":
            pet = escolher_pet(lista_pets)
            if pet:
                lista_pets.remove(pet)
                print(f"{pet.nome} removido com sucesso!")
        elif opcao == "0":
            salvar_em_binario(lista_pets)
            print("\nPrograma encerrado!")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    Menu()
