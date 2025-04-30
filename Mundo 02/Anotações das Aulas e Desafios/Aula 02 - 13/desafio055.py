#DESAFIO 055: Maior e Menor da Sequência

#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.


lista= []
for c in range (1,6):
    lista.append(float(input ('Qual o peso da {}ª pessoa? ' .format (c))))
print ('O maior peso é', max(lista))
print ('O menor peso é', min(lista))
