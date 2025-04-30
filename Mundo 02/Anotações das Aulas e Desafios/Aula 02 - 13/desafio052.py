#DESAFIO 052: Números Primos

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
b = 0
for c in range(1, n+1):
    if n % c == 0:
        b += 1
if b == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')