#EXERCÍCIO 021: Tocando um MP3

#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3 (substitua pelo caminho do seu arquivo)
pygame.mixer.music.load('Mundo 01/Exercícios Corrigidos/gidle_queencard.mp3')

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando até a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


