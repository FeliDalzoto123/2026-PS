# ===========================================
# SISTEMA DE APROVAÇÃO DE ALUNOS 
# ===========================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipo s e controle de Fluxo
# Autor      : Felipe Dalzoto
# Data       : 10/03/2026
# Repositorio: https://github.com/FeliDalzoto123/2026-PS
# ============================================
#
# DESCRIÇÃO:
# Desenvolver um programa que controla o estoque
# de uma loja de informática. Ele precisa saber quais
# produtos estão em quantidade critica, adequada, e excesso.
# =============================================


estoque = [
    {"nome": "Teclado", "quantidade": 30,"preço": 300},
    {"nome": "Mouse", "quantidade": 10, "preço": 250},
    {"nome": "Monitor", "quantidade": 20, "preço": 560},
    {"nome": "Mouse_Pad", "quantidade": 5, "preço": 50},
    {"nome": "Gabinete", "quantidade": 50, "preço": 700},
    {"nome": "Cabo_De_Rede", "quantidade": 2, "preço": 20}
]

print("==== CONTROLE DE ESTOQUE ====")

for produto in estoque:
    nome = produto["nome"]
    quantidade = produto["quantidade"]
    preço = produto["preço"]

    if quantidade < 5:
        situacao = "Quantidade critica"
    elif quantidade >= 20:
        situacao = "Quantidade adequada"
    else:
        situcao = "Excesso de estoque"


    print("-" * 30)
    print(f"Produto: {nome}")
    print(f"Quantidade em Estoque: {quantidade}")
    print(f"Preço: R$ {preço:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)



