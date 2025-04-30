#DESAFIO 049: Tabuada v2.0

#Refaça o DESAFIO 009, mostrando a tabuada de um número que
#o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))
for p in range(1, 11):
    print('{} x {} = {}'.format(num, p, num * p))