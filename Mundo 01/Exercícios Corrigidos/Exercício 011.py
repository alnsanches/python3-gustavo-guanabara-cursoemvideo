#EXERCÍCIO 011: Pintando Parede

#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2 m².



a = float(input('Digite a altura da parede (m^2): '))
l = float(input('Digite a largura da parede (m^2): '))

area = a*l
tinta = area/2

print(f'A area total é de {area}, e a quantidade de tinta a uma area de 2m^2 é {tinta}litros de tinta')


# OUTRA MANEIRA DE FAZER: 

#larg = float(input('Largura da parede: '))
#alt = float(input('Altura da parede: '))
#area = larg * alt
#tinta = area / 2
#print('Sua parede tem as dimensões de {} x {} e sua área é de {} m².'.format(larg, alt, area))
#print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))
