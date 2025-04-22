#EXERCÍCIO 005: Antecessor e Sucessor

#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.


number = int(input(' Digite um número: '))
print ('Seu antecessor é {} e sucessor {}' .format(number-1, number+1))