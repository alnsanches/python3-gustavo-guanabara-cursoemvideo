#DESAFIO 010: Conversor de Moedas

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere U$ 1,00 = R$ 5,92 e Euro 5,36


real = float(input('Quanto de dinheiro a pessoal você tem na carteira? R$'))
dolar = real / 5.92
euro = real / 5.36
print('Com R${:.2f} você pode comprar U$${:.2f} e pode comprar €{:.2f}'.format(real, dolar, euro))