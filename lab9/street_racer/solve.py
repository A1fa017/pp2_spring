import random
import sys
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 10


SCORE  = 0
COINS = 0
clock = pygame.time.Clock()


score_font = pygame.font.SysFont("Verdana", 20)
coins_font = pygame.font.SysFont('Verdana',20)
font_end = pygame.font.SysFont('Verdana',70)
font_start = pygame.font.SysFont('Verdana',70)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load("C:\pp2\lab8\street_racer\images\AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\pp2\lab8\street_racer\images\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 550), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\pp2\lab8\street_racer\images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
        
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -STEP)
            
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, STEP)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:\pp2\lab8\street_racer\images\Coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(60,550), random.randint(60,350)

    def draw(self,surface):
        surface.blit(self.image,self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
done = True

while True:

    while done:
        render_start = font_start.render('TAP TO START',True,'Navy')
        render_start_rect = render_start.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
        SURF.blit(bg,(0,0))
        SURF.blit(render_start,render_start_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = False
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()

    #collision of a player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        while True:
            render_end = font_end.render('GAME OVER',True,'DarkRed')
            render_end_rect = render_end.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
            SURF.blit(render_end,render_end_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    #collision of a player and coin
    if pygame.sprite.spritecollideany(P1,coins):
        x,y = random.randrange(40,50),random.randrange(40,50)
        C1.image = pygame.transform.scale(C1.image,(x,y))
        C1.rect = C1.image.get_rect(center=(random.randrange(60,550),random.randrange(60,550)))
        

        COINS += 1
        if COINS%4 == 0:
            ENEMTY_STEP += 1

    SURF.blit(bg, (0, 0))

    #drawing coin,enemy,player
    C1.draw(SURF)
    E1.draw(SURF)
    P1.draw(SURF)

    score_img = score_font.render(f'SCORE:{SCORE}', True, 'white')
    SURF.blit(score_img, (10, 10))

    coins_img = coins_font.render(f'COINS:{COINS}',True,'yellow')
    SURF.blit(coins_img, (10,40))

    pygame.display.update()
    clock.tick(FPS)
    
