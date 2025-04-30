#DESAFIO 044: Gerenciador de Pagamentos

#Elabore um programa que calcule o valor a ser pago de um produto,
#considerando o seu preço normal, e condição de pagamento:

#- À vista no dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

print('-'*20)
print('| LOJINHA DA ESQUINA |')
print('-'*20)
v = float(input('Digite o valor do produto: R$'))
print('''Escolha um método de pagamento abaixo:

[ 1 ] A vista no dinheiro ou nocheque com 10% de desconto.
[ 2 ] A vista no cartão com 5% de desconto. 
[ 3 ] Parcelado 2x no cartão (sem desconto)
[ 4 ] Parcelado 3x ou mais no cartão com 20% de juros''')
p = int(input('Sua escolha: '))

if p == 1:
    total = v-(v*10/100)
elif p == 2:
    total = v-(v*5/100)
elif p == 3:
    total = v
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif p == 4:
    total = v+(v*20/100)
    tpd = int(input('Digite quantas vezes deseja parcelar: '))
    print('')
    parcela = total/tpd
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% de juros'.format(tpd, parcela))
else:
    total = 0
    print('Ocorreu um erro, verifique o que você digitou e tente novamente!')
    print('')
print('O produto de R${:.2f} vai custar R${:.2f} no total!'.format(v, total))
