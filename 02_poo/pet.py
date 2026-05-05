'''
==================================================================
# ARQUIVO    : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula       : Aula 20 - Por que POO?
# Autor      : Felipe Dalzoto
# Conceitos  : Classe, objeto, atributos, métodos, encapsulamento
# Atividade  : Classe Pet
===================================================================
'''

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
        print(f"Hospedagem: {'Sim' if self.hospedagem else 'Não'}")
        print(f"Vacinado: {self.vacinado}")
       
    
    def registrar_entrada(self):
        self.hospedagem = True
        print(f"{self.nome} entrou no hotel.")
        
    def registrar_saida(self):
        self.hospedagem = False
        print(f"{self.nome} saiu do hotel.")
    
    def calcular_diaria(self):
        if self.hospedagem:
           
            if self.idade <= 3:
                return 50.00
            elif 4 <= self.idade <= 10:
                return 60.00
            elif self.idade > 10:
                return 70.00
            
    def verificar_vacinação(self):
        if self.vacinado.lower() == "sim":
            return "Vacinado."
        else:
            return "Não vacinado."

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"Peso atualizado para {self.peso} kg.")
        
    def emitir_resumo(self, resumo):
        self.resumo = f"Pet: {self.nome}, Espécie: {self.especie}, Idade: {self.idade} anos, Vacinado: {self.vacinado}, Peso: {self.peso} kg,  Raça: {self.raca}, Hospedagem: "
        print(self.resumo)
    
    def exibir_raca(self):
        return self.raca 

    
    
pet1 = Pet("Rex", "Cachorro", 5, "sim", 20, "Pastor Alemão")
pet2 = Pet("Titica", "Galinha", 3, "não", 10, "garnizé")
pet3 = Pet("Thomas", "Gato", 5, "sim", 30, "Persa")

    
pet1.exibir_dados()
pet1.verificar_vacinação()
pet1.atualizar_peso(20)
pet1.exibir_raca()
pet1.emitir_resumo("Resumo do Pet")
print()

    
pet2.exibir_dados()
pet2.verificar_vacinação()
pet2.atualizar_peso(10)
pet2.exibir_raca()
pet2.emitir_resumo("Resumo do Pet")
print()

    
pet3.exibir_dados()
pet3.verificar_vacinação()
pet3.atualizar_peso(30)
pet3.exibir_raca()
pet3.emitir_resumo("Resumo do Pet")

