# EXERCÍCIO 014: Conversor de Temperaturas

#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.


temperatura = float(input('Digite a temperatura em ºC:'))
f = (temperatura * (9 / 5)) + 32
print('{}ºC é igual a {}ºF' .format(temperatura, f))
