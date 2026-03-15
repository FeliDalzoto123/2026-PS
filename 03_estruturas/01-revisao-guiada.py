# ===========================================
# SISTEMA DE BIBLIOTECAS
# ===========================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Felipe Dalzoto
# Data       : 11/03/2026
# Repositorio: https://github.com/FeliDalzoto123/2026-PS
# ============================================
#
# DESCRIÇÃO:
# Catálogo de livros que demosntra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# =============================================

# ---- LISTAS: CONCEITO BÁSICO ----

# Criando uma lista de titulos
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritimos",
]

# Acesso por indice (começa em 0, não em 1!)
print()
print("Primeiro Livro: ", titulos[0])
print("Último Livro  : ", titulos[-1])    # indice -1 = último elemento
print("Total de Livros: ", len(titulos))

# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append: ", titulos)
print()

#verifica se um item existe 
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')
else:
    print(f'"{busca}" não encontrado.')


# Ordenar a lista
titulos.sort()
print("Lista Ordenada: ", titulos)
print()

# Remover um item
titulos.remove("Entendendo Algoritimos")
print("Após remove: ", titulos)
print()


# ---- DICIONÁRIOS: CONCEITO BÁSICO ----

# Um dicionario representa um livro com seus atributos
livro = {
    "titulo":       "O Programador Pragmático",
    "autor":        "Andrew Hunt e David Thomas",
    "ano":          1999,           # int, não string
    "disponivel":   True,           #bool
}



# Acessando valores pelas chaves
print("Titulo :", livro["titulo"])
print("Autor  :", livro["autor"])
print("Ano    :", livro["ano"])
print("Status :", "Disponível" if livro["disponivel"] else "Emprestado")
print()


# ---- MODIFICANDO E CONSULTANDO ----

# Atualizando um valor existente
livro["disponivel"] = False  # livro foi emprestado
print("\nApós empréstimo: ", livro["disponivel"])


# Adicionando uma nova chave
livro["paginas"] = 352
print("Páginas: ", livro["paginas"])


# .get() - acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não Informada")
print("Editora: ", editora)  # não lança KeyError, retorna o padrão
print()


# ---- CATÁLOGO: LISTA DE DICIONÁRIOS ----

catalogo = [
    {"titulo":   "O Programador Pragmático", "autor":  "Andrew Hunt e David Thomas", "ano":  1999,
"disponivel": True},
    {"titulo":  "Código Limpo", "autor":  "Robert C. Martin", "ano":  2008,
"disponivel":  False},
    {"titulo":  "Entendendo Algoritimos", "autor":  "Aditya Bhargava", "ano":  2016,
"disponivel":  True},
]

print("=== Catálogo da Biblioteca ===")
print()

# Percorrendo cada livro com for
for livor in catalogo:
    status = "Disponivel" if livro["disponivel"] else "Emprestado"
    print(f'  {livro["titulo"]} ({livro["ano"]})')
    print(f'  Autor: {livro["autor"]} | {status}')
    print(" " + "-" * 40)



# ==== CONSULTAS E FILTROS ====

print("\n=== Livros Disponíveis ===")
for livro in catalogo:
    if livro["disponivel"]:         # filtra apenas os disponíveis
        print(f'  {livro["titulo"]}')

print("\n=== Busca por título ===")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro['titulo'].lower():        # .lower() ignora maiúsculas/minúsculas
        print(f' Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True
if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():        # .items() retorna pares (chave, valor)
    print(f"  {chave}: {valor}")
