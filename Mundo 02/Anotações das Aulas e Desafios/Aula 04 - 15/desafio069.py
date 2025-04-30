#DESAFIO 069: Análise de Dados do Grupo

#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) Quantas pessoas têm mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres têm menos de 20 anos.

from time import sleep
maior = homem = mulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
        homem += 1
    elif sexo in 'F' and idade < 20:
        mulher += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    again = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if again in 'N':
        break
sleep(1)
print('=-'*10)
print('PROGRAMA ENCERRADO')
sleep(2)
print('Analisando dados...')
print('=-'*10)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos de idade')