#DESAFIO 037: Conversor de Bases Numéricas

#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
#a base de conversão:

#- 1 para Binário
#- 2 para Octal
#- 3 para Hexadecimal


print('-='*20)
print('Conversor de binário, octal e hexadecimal:')
print('-='*20)
print('')
n = int(input('Digite um número inteiro: '))
print('')
print('''Escolha uma das bases de conversão:

[ 1 ]  Converter para BINÁRIO
[ 2 ]  Converter para OCTAL
[ 3 ]  Converter para HEXADECIMAL''')
print('')
e = int(input('Sua escolha: '))

if e == 1:
    print('{} convertido para binário é igual a: {}'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} convertido para octal é igual a: {}'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} convertido para hexadecimal é iual a: {}'.format(n, hex(n)[2:]))
else:
    print('Por favor digite uma opção válida!')

