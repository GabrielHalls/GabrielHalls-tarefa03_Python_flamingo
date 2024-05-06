# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# Tarefa 03 Python
# 4- Faça um programa que receba três notas de um aluno e calcule sua média.

aluno = input("Digite nome do Aluno \n")
nota1 = float(input("Digite a nota da AV1: "))
nota2 = float(input("Digite a nota da AV2: "))
nota3 = float(input("Digite a nota da CONCLUSIVA: "))

media = (nota1+nota2+nota3)/3

print("A media do", aluno, "é", media)
