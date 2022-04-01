import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('sound')
sounds = [f'sounds/{file}' for file in os.listdir('sounds')]
music = pygame.mixer.music
music.load(sounds[0])
music.play()
fps = 1000
clock = pygame.time.Clock()
cnt = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                cnt += 1
                if cnt%2 == 0:
                    music.unpause()
                else:
                    music.pause()
            elif pressed[pygame.K_RIGHT]:
                sounds = sounds[1:]+sounds[:1]
                music.load(sounds[0])
                music.play()
            elif pressed[pygame.K_LEFT]:
                sounds = sounds[-1:]+sounds[:-1]
                music.load(sounds[0])
                music.play()    
    clock.tick(fps)
    pygame.display.flip()    