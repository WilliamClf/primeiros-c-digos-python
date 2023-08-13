#Faça um programa que peça as 4 notas bimestrais e
#mostre uma média indicando uma mensagem de
#reprovação caso a nota seja menor que 7

nota1 = float(input('Insira a nota da sua primeira prova: '))
nota2 = float(input('Insira a nota da sua segunda prova: '))
nota3 = float(input('Insira a nota da sua terceira prova: '))
nota4 = float(input('Insira a nota da sua quarta prova: '))

calculoMedia = (nota1 + nota2 + nota3 + nota4)/4

if calculoMedia < 7:
    print('Reprovado! Sua média é:',calculoMedia)
elif calculoMedia >= 7:
    print('Aprovado! Sua média é:',calculoMedia)
