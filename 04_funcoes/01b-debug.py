# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manha") :
    mensagem = f"Bom {turno}, {nome}!"

saudacao("Ana")
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2
    return resultado

print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    global total
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n):
    if n <= 0:  
        return
    print(n)
    contagem(n - 1)

contagem(3)

# Erro 1: linha 8 o {} é so usado para os dicionarios o correto é usar os ().
# Erro 2: linha 12 não tinha um valor retornado.
# Erro 3: linha 18 não tinha a variavel global.
# Erro 4: linha 25 estava em um loop infinito.



