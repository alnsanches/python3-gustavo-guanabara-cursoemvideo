#DESAFIO 051: Progressão Aritmética

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.


pa = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão: ')) #numero que quero pular
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(r, pa))
print(pa, end=' ')

for c in range(1, 10):
    pa += r
    print(pa, end=' ')
