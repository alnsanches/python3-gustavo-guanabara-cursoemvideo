#DESAFIO 050: Soma dos Pares

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
#daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


soma = 0
cont = 0
for c in range(1, 7):
    numeros = int(input(f"Digite {c} valor:"))
    if numeros % 2 == 0:
        soma+=numeros
        cont += 1
print(f"Você digitou {cont} números PARES e a soma total deles foi {soma}")
