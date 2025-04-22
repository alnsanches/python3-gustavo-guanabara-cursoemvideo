#EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


cidade = str(input('Em que cidade você nasceu? ')).strip().title()
print('Santo' in cidade)