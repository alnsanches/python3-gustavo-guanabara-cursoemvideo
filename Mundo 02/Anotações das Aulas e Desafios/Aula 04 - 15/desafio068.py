#DESAFIO 068: Jogo do Par ou Ímpar

#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
#jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint
cont = 0
while True:
    valorjogador = int(input('Digite um número entre 0 a 10: '))
    computador = randint(0, 10)
    total = valorjogador + computador
    escolha = ' ' #abrindo uma string vazia para inserir o que o usuario digitar
    while escolha not in 'PI':
        escolha  = str(input('Par ou ímpar?: ')).strip().upper()[0] #pega só a 1° letra
    print(f'Você jogou {valorjogador} e o computador {computador}. Total: {total}.')
    if escolha in 'P':       
        if total % 2 == 0:
            print(f'O número {total} é PAR, e como você escolheu PAR, PARABÉNS, você ganhou do computador!')
            cont += 1
        else:
            print(f'O número {total} é ÍMPAR, e como você escolheu PAR, VOCÊ PERDEU!')
            break
    elif escolha in 'I':
        if total & 2 != 0:
            print(f'O número {total} é ÍMPAR, e como você escolheu ÍMPAR, VOCÊ GANHOU!')
            cont += 1
        else:
            print(f'O número {total} é PAR, e já que você escolheu ÍMPAR, O COMPUTADOR GANHOU!')
            break     
print(f'Você venceu {cont} vezes seguidas! Obrigado e até a próxima vez!')
