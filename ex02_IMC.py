# Curso básico de Python
# Nome do desenvolvedor: Gabriel Vinicius
# Versão 1.0
# Exercicicos de logica de programação
# com logica de programação em python
# Tarefa 03 Python
# 2 -Crie um programa que solicite ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).


print("Vamos fazer o calculo do seu IMC?")
# Aqui estou solicitando que o usuario insira seu peso e altura
peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))
#Vamos calcular o IMC
imc = peso / (altura**2)
#Aqui vamos imprimir o seu IMC
print("Seu IMC é : ", imc)

#Aqui vamos classificar o IMC

if imc <18.5: print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25: print("Você está normal")
elif imc >= 25 and imc <30: print("Você está com sobrepeso")
else: print("Você está obeso.")

