#EXERCÍCIO 007: Média Aritmética
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
media = (n1 + n2) / 2
print('A média do aluno é {:.2f}'.format(media))
if media > 6:
    print('APROVADO')
elif media == 6:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
