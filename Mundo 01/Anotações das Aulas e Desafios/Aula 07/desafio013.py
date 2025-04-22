#DESAFIO 013: Reajuste Salarial

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário R$: '))
aumento = float(input('Digite aumento %: '))
percentual = (aumento/100)
acrescimo = percentual*salario
novo_salario = salario+acrescimo

print (f'Salário atual R$:{salario:.2f}, novo salario R$:{novo_salario:.2f}')
