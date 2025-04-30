#DESAFIO 041: Classificando Atletas

#A Confederação Nacional de Natação precisa de um programa que leia o ano
#de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JUNIOR
#- Até 25 anos: SÊNIOR
#- Acima: MASTER

from datetime import date
atual = date.today().year
nas = int(input('Em que ano o atleta nasceu (ex: 1990)? '))

if nas <= 9:
    print('O atleta de {} anos vai ficar na categoria MIRIM!'.format(nas))
elif nas <= 14:
    print('O atleta de {} anos vai ficar na categoria INFANTIL!'.format(nas))
elif nas <= 19:
    print('O atleta de {} anos vai ficar na categoria JUNIOR!'.format(nas))
elif nas <= 25:
    print('O atleta de {} anos vai ficar na categoria SÊNIOR!'.format(nas))
elif nas > 25:
    print('O atleta de {} anos vai ficar na categoria MASTER!'.format(nas))
