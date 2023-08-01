#Faça um programa que verifique se uma letra
#digitada é vogal ou consoante
letra = str(input("Insira uma letra do alfabeto: "))

if letra in 'aeiouAEIOU':
    print("A letra Inserida é uma vogal!")
else:
    print("A letra Inserida é uma consoante!")

