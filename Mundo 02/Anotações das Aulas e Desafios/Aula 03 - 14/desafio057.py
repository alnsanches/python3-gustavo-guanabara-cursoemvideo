#DESAFIO 057: Validação de Dados

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.


gender = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while gender != 'M' and gender != 'F':
    print('Valor inválido! Digite M para sexo MASCULINO ou F para sexo FEMININO.')
    gender = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
if gender == 'M':
    print('Você do sexo MASCULINO!')
elif gender == 'F':
    print('Você é do sexo FEMININO!')
