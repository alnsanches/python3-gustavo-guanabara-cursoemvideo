#DESAFIO 033: Maior e Menor Valores

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))
