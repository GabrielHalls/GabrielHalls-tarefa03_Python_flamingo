# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# Tarefa 03 Python
# 3) Faça um programa que pergunte ao usuário o valor do produto e o percentual de desconto, e retorne o valor final após o desconto.

valorProd = float(input("Digite o valor do produto: "))
percetualDesconto = float(input("Digite o percentual de desconto (%): "))

desconto = valorProd * (percetualDesconto/100)

valorFinal = valorProd - desconto

print("O valor final do produto após o desconto é: ", valorFinal)