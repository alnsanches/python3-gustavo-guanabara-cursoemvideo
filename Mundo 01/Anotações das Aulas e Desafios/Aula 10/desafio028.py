#DESAFIO 028: Jogo da Adivinhação v1.0

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
while True:
    print('-=-' * 10)
    print('JOGO DE ADIVINHAÇÃO!')
    print('-=-' * 10)

    num = random.randint(0, 5)
    tentativa = int(input('Adivinhe qual o número de 0 a 5: '))
    if tentativa == num:
        print('Parabéns você conseguiu acertar!')
    else:
        print('Infelizmente não foi dessa vez')
    print('Obrigado por jogar!')
    nova = str(input('Deseja jogar novamente? S/N: ')).strip().upper()
    if nova == 'S':
        continue
    else:
        break

