#Faça um programa que peça um valor e mostre na
#tela se o valor é positivo ou negativo
num = float(input('Insira um número: '))

if num > 0:
    print("O número Inserido é positivo!")
elif num < 0:
    print("O número Inserido é negativo!")
else:
    print("O número Inserido é igual a 0!")