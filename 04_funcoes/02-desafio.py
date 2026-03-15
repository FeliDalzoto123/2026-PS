# ===========================================
# SISTEMA DE APROVAÇÃO DE ALUNOS 
# ===========================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipo s e controle de Fluxo
# Autor      : Felipe Dalzoto
# Data       : 14/03/2026
# Repositorio: https://github.com/FeliDalzoto123/2026-PS
# ============================================
#
# DESCRIÇÃO:
# Este Programa processa as notas de uma turma e vai determinar
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado) organizados
# em modulos e funções para melhorar a organização
# do código.
# =============================================

# ==== DADOS DO ALUNO ====
nome = input("Digite o nome do Aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

# ==== Calcular a média ====
media = (nota1 + nota2) / 2
if media >= 6.0:
    situacao = "✅ Aprovado"
elif media >= 4.0:
    situacao = "⚠️ Recuperação"
else:
    situacao = "❌ Reprovado"

# === exibe o resultado formatado de forma clara ===
print('=' * 40)
print("=== Relatório Final do Aluno ====")
print(f"Aluno: {nome}")
print(f"Média do Aluno: {media:.2f}")
print(f"Situação do Aluno: {situacao}")
print('=' * 40)
