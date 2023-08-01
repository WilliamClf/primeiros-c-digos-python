#Faça um Programa que peça as 4 notas bimestrais e
#mostre a média
nota1 = input("Digite a nota do 1º bimestre: ")
nota2 = input("Digite a nota do 2º bimestre: ")
nota3 = input("Digite a nota do 3º bimestre: ")
nota4 = input("Digite a nota do 4º bimestre: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

calculoMedia = (nota1 + nota2 + nota3 + nota4)/4
print(calculoMedia)
