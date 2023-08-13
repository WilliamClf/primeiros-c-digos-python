#Faça um programa que leia três números e mostre o
#maior e o menor deles

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

maior = menor = num1

if num2 > maior:
 maior = num2

if num3 > maior:
 maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'O maior número é: ',maior)
print(f'O menor número é: ',menor)
