# EXERCÍCIO 008: Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#obs:Lembrando que conversão de Metros para:
#dm(Decímetro) é igual a:  valor*10
#cm(Centrímetro) é igual a:  valor*100
#mm(Milímetro) é igual a:  valor*1000
#dam(Decâmetro) é igual a:  valor/10
#hm(Hectômetro) é igual a: valor/100
#km(Quilômetro) é igual a: valor/1000

#obs²: pode acrescentar o limite de casas decimais colocando:
#:.0f (nenhuma casa decimal)
#:.1f(somente uma casa decimal)
#:.2f(somente duas casas decimais)
#:.3f(somente três casas decimais)
#print(f'a medida de {a} metros é igual a {a/10:.1f} decâmetros')

a = float(input('Digite um valor em metro: '))
print(f'a medida de {a} metros é igual a {a*10} decímetros')
print(f'a medida de {a} metros é igual a {a*100} centímetros')
print(f'a medida de {a} metros é igual a {a*1000} milímetros')
print(f'a medida de {a} metros é igual a {a/10} decâmetros')
print(f'a medida de {a} metros é igual a {a/100} hectômetros')
print(f'a medida de {a} metros é igual a {a/1000} quilômetros')


