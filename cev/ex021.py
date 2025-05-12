#import winsound
#winsound.PlaySound('Chop-Suey.wav', winsound.SND_FILENAME)

import pygame
pygame.init()
pygame.mixer.music.load('chop-suey.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()