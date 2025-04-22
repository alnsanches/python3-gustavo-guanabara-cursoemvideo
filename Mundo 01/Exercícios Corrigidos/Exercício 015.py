# EXERCÍCIO 015: Aluguel de Carros

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. 


diaria = float(input('Qual o valor da diária do carro? '))
valorporkm = float(input('Qual o valor por km rodado? '))
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

pago = (dias * diaria) + (km * valorporkm)
print('O total a pagar é de R$ {:.2f}!'.format(pago))
