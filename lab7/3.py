import pygame

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('red ball')
color = pygame.Color('red')
x,y = 50, 50
radius = 25
dx = 20
dy = 20 
fps = 20
clock = pygame.time.Clock()
while True:
    screen.fill('white')
    pygame.draw.circle(screen,color,(x,y),radius)
    pygame.display.flip()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 50:
        y -= dy
    elif pressed[pygame.K_DOWN] and y <= 550:
        y += dy
    elif pressed[pygame.K_RIGHT] and x <= 550:
        x += dx
    elif pressed[pygame.K_LEFT] and x >= 50:
        x -= dx
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(fps)