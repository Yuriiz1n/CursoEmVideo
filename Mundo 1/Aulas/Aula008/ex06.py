import pygame
import time

pygame.init()
pygame.mixer.music.load('DEVILS NEVER CRY (スタッフロール).mp3')
pygame.mixer.music.play()
pygame.event.wait()

print("Tocando música... (Aperte 'p' para pausar, 'r' para retomar, 'e' para sair)")

while True:
    query = input(" ")

    if query == 'p':
        pygame.mixer.music.pause()
        print("Música pausada.")

    elif query == 'r':
        pygame.mixer.music.unpause()
        print("Música retomada.")

    elif query == 'e':
        pygame.mixer.music.stop()
        print("Música parada.")
        break
