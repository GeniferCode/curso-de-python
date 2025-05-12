from emoji import emojize
import pygame
pygame.init()
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('\033[32mAPROVADO! 😎')
    pygame.mixer_music.load('sucesso.mp3')
    pygame.mixer.music.play()
    input()
elif 5<=media<7:
    print(emojize('\033[33mRECUPERAÇÃO! :hot_face:', variant='emoji_type'))
    pygame.mixer.music.load('mais-ou-menos.mp3')
    pygame.mixer.music.play()
    input()
else:
    print(emojize('\033[31mREPROVADO! :pensive_face:', variant='emoji_type'))
    pygame.mixer.music.load('fail.mp3')
    pygame.mixer.music.play()
    input()
pygame.event.wait()
