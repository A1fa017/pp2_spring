import pygame
pygame.init()

WHITE = ('white')
BLACK = ('black')
RED = ('red')
RED_DARK = ('darkred')
GREEN = ('darkgreen')
BLUE = ('blue')

size = WIDTH,HEIGHT = (800, 600)
pygame.display.set_caption('Paint')
img = pygame.image.load("eraser.png")
eraser = pygame.transform.scale(img, (50,50))
SCREEN = pygame.display.set_mode(size)
clock = pygame.time.Clock()

dir, mouse = None, None
SCREEN.fill(WHITE)
color = BLACK
pen = 1
done = True 
shape = False
check = 0
save_screen = None
points = []

while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      dir = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      mouse = pygame.mouse.get_pos()
      if dir:
        pygame.draw.line(SCREEN, color, dir, mouse, pen)
        dir = mouse

    if event.type == pygame.MOUSEBUTTONUP:
      dir = None
      points = []
      done = True  

    if event.type == pygame.MOUSEBUTTONDOWN:
      if 40<=mouse[0]<=90 and 40<=mouse[1]<=90:
        color = RED

      elif 40<=mouse[0]<=90 and 100<=mouse[1]<=150:
        color = BLUE

      elif 40<=mouse[0]<=90 and 160<=mouse[1]<=210:
        color = GREEN

      elif 40<=mouse[0]<=90 and 380<=mouse[1]<=430:
        color = WHITE  
        check = 0 

      elif 41<=mouse[0]<=86 and 250<=mouse[1]<=295:
        check = 1
        shape = False
        
      elif 60<=mouse[0]<=90 and 325<=mouse[1]<=350:
        check = 1
        shape = True
      
      if check != 0 and color == WHITE:
        color = BLACK

      if check == 1:
        done = False
        x1,y1 = event.pos
        save_screen = SCREEN.copy()

    if event.type == pygame.MOUSEMOTION and (0,0) < event.pos < size and pygame.mouse.get_pressed()[0]:
      if not done:
          x2,y2 = event.pos
          width, height = abs(x1-x2), abs(y1-y2)
          SCREEN.blit(save_screen, (0,0))
          if shape:
              pygame.draw.ellipse(SCREEN, color, (x1 - width*(x2<x1),y1 - height*(y2<y1),width, height),pen) 
          else:
              pygame.draw.rect(SCREEN, color, (x1 - width*(x2<x1),y1 - height*(y2<y1),width, height),pen) 
     
    pygame.mouse.get_pos()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        pen+=1
      elif event.key == pygame.K_DOWN:
        pen-=1
        if pen <= 0:
          pen = 1

    pygame.draw.rect(SCREEN, WHITE, (2,2,120,598)) 
    pygame.draw.line(SCREEN, (0,0,0), (122,0),(122,600), 10)
    pygame.draw.rect(SCREEN, (0,0,0), (0,0,800,600), 10)
    pygame.draw.circle(SCREEN, RED, (60,60),30)
    pygame.draw.circle(SCREEN, BLUE, (60,130),30)
    pygame.draw.circle(SCREEN, GREEN, (60,200),30)
    pygame.draw.rect(SCREEN, (0,0,0), (40,250,45,45), 2)
    pygame.draw.circle(SCREEN, (0,0,0), (63,330), 23, 2)
   
  SCREEN.blit(eraser,(40,380))
  pygame.display.flip()
