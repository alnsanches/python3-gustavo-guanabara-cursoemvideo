#DESAFIO 007: Média Aritmética

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A primeira nota foi {}, a segunda nota foi {} e a média entre elas é {}.'.format(nota1, nota2, media))
