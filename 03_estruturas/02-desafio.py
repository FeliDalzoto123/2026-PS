# ===========================================
# SISTEMA DE BIBLIOTECAS
# ===========================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Felipe Dalzoto
# Data       : 12/03/2026
# Repositorio: https://github.com/FeliDalzoto123/2026-PS
# ============================================
#
# DESCRIÇÃO:
# Criar um catalogo com livros diversos e tem que contem um cadastro de livros novos durante o uso,
# uma busca por autor, registrar empréstimos e devoluçõs
# e ao final do programa gerar um relatorio final. 
# =============================================


titulos = [
    {"titulo":"O Programador Pragmático", "autor": "Andrew Hunt e David Thomas"},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin"},
    {"titulo": "Entendendo Algoritimos", "autor": "Aditya Bhargava"},
]

# Acesso por indice (começa em 0, não em 1!)
print()
print("Primeiro Livro: ", titulos[0]["titulo"], "de", titulos[0]["autor"])
print("Último Livro  : ", titulos[-1]["titulo"], "de", titulos[-1]["autor"])    
print("Total de Livros: ", len(titulos))

# Cadastrar um novo livro
cadastro = input("Deseja cadastrar um novo livro? (s/n): ")

if cadastro.lower() == "n":
    print

if cadastro.lower() == "s":

    novo_livro = input("Digite o nome do livro: ")
    novo_autor = input("Digite o nome do autor: ")
    titulos.append(f"{novo_livro}, {novo_autor}")

    print("Seu cadastro foi concluido com sucesso!")
    mostra_o_catalogo = input("Deseja ver o catalogo atualizado? (s/n): ")

    if mostra_o_catalogo.lower() == "s":
        print(titulos)
    else:
        print("Obrigado por usar nosso sistema de bibliotecas!")

busca_por_autor = input("Digite o nome do autor para busca: ")
if busca_por_autor in titulos:
    print("O autor", busca_por_autor, "está no catalogo.")
else:
    print("O autor", busca_por_autor, "não encontrado no catalogo.")

# Registrar empréstimo
emprestimo = input("Deseja registrar um empréstimo? (s/n): ")
if emprestimo.lower() == "s":
    livro_emprestado = input("Digite o nome do livro para empréstimo: ")
    if livro_emprestado in titulos:
        print("O livro", livro_emprestado, "foi emprestado com sucesso!")
    else:
        print("O livro", livro_emprestado, "não foi encontrado no catalogo.")

# Registrar devolução
devoluçao = input("Deseja registrar uma devolução? (s/n): ")
if devoluçao.lower() == "n":
    print("Obrigado por usar nosso sistema de bibliotecas!")
elif devoluçao.lower() == "s":
    livro_devolvido = input("Digite o nome do livro para devolução: ")
    if livro_devolvido in titulos:
        print("O livro", livro_devolvido, "foi devolvido com sucesso!")
    
# Gerar relatório final
print("\nRelatório Final:")
print("Total de Livros no Catalogo:", len(titulos))
print("Livros Disponíveis:")
for livro in titulos:
    print("- ", livro)

