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
# Este Programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variaveis, tipos de dados, operadores,
# estruturas de seleção e estrutura de repetição.
# =============================================

# ==== DADOS DA TURMA ====
# Uma lista de dicionários: cada dicionário representa um aluno

turma = [
    {"nome": "Ana",  "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},

]

print("=== Resultador da Turma ===")
print()

# o "for" percorre cada aluno de lista automaticamente
for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2

    if media >= 6.0:
        situacao = "✅ Aprovado"
    elif media >= 4.0:
        situacao = "⚠️ Recuperação"
    else:
        situacao = "❌ Reprovado"

    print(f"Aluno    : {nome}")
    print(f"Média    : {media:.2f}")
    print(f"Sittuação:{situacao}")
    print("-" * 30)
