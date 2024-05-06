# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# Tarefa 03 Python
# 5)Crie um programa que pergunte ao usuário a quantidade de dias, horas, minutos e segundos, e calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos"))

total_segundos = segundos + (minutos*60) + (horas*3600) + (dias*86400)

print("O total em segundos é: ", total_segundos)