#EXERCÍCIO 029: Radar Eletrônico

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
#mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

from random import randint
vel = int(input('Digite a sua velocidade (entre 10km/h e 180Km/h): '))
lim = randint(0, 180)
if lim < vel:
    print('Multado exedeu o limite sua velocidade é {}Km/h e o limite é {}Km/h'.format(vel, lim))
else:
    print('Velocidade normal {}Km/h é abaixo do limite que é {}Km/h'.format(vel, lim))
