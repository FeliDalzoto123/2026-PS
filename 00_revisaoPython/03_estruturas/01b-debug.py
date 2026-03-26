# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo",  "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"])

print("\nLivros Disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:
         print(f'{livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de Livros: {total}")

for chave, valor in catalogo[0].items():
    print(f" {chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)

# Erro 1: linha 10 O catalogo estava procurando o terceiro livro, sendo que não tem nenhum os livros começam 0 a 2.
# Erro 2: linha 14 Ele estava verificando quais livros estavam com false, sendo que o correto é verificar quais livros são true.
# Erro 3: linha 20 O loop tenta desempacotar chave e valor diretamente do dicionário.
# Erro 4: linha 23 A palavra Autor estava com letra maiuscula, sendo que dentro do dicionario esta com letra minuscula
