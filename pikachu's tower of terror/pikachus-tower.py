# init block
import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

#variables
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
HARD = 7

#setup
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pikachu's Tower of Terror")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (255,255,255))

background = pygame.image.load("background.png") ###
gameoverscreen = pygame.image.load("gameover.png") ###

#classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.surf = pygame.Surface((30, 30))
        #self.surf.fill((128,255,255))
        self.surf = pygame.image.load("pikachu-sprite-gif-6.gif") ###
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0,0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

class Coin(pygame.sprite.Sprite): ### new class
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()

        self.rect.topleft = pos

    def update(self):
        if self.rect.colliderect(P1.rect):
            P1.score += 5
            self.kill()

class platform(pygame.sprite.Sprite):
    def __init__(self, width = 0, height = 18): ### width and height are new
        super().__init__()
        #self.surf = pygame.Surface((random.randint(50,100), 12)) ##for plain platforms
        #self.surf.fill((0,255,0)) ##plain platforms
        if width == 0: width = random.randint(50, 120) ###
        self.image = pygame.image.load("platform.png") ###
        self.surf = pygame.transform.scale(self.image, (width, height)) ###
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
        self.speed = random.randint(-1, 1)
        self.moving = True
        self.point = True
        if (self.speed == 0): ###
            self.moving == False ###

    def move(self):
        hits = self.rect.colliderect(P1.rect)
        if self.moving == True:
            self.rect.move_ip(self.speed, 0)
            if hits:
                P1.pos += (self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH

    def generateCoin(self): ###
        if (self.speed == 0):
            coins.add(Coin((self.rect.centerx, self.rect.centery - 50)))

#functions
def check(platform, groupies): ## makes sure there's space between them
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False


def plat_gen(): ## makes new platforms
    while len(platforms) < 7 :
        width = random.randrange(50,100)
        p  = None ###
        C = True

        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                            random.randrange(-50, 0))
            C = check(p, platforms)
        p.generateCoin() ###
        platforms.add(p)
        all_sprites.add(p)


#sprites
PT1 = platform()
P1 = Player()

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
PT1.moving = False
PT1.point = False

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

coins = pygame.sprite.Group() ###

#level generation
for x in range(random.randint(5, 6)):
    C = True
    pl = platform()
    while C:
        pl = platform()
        C = check(pl, platforms)
    pl.generateCoin() ###
    platforms.add(pl)
    all_sprites.add(pl)

#gameloop
while True:
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()

    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            #displaysurface.fill((255,0,0))
            displaysurface.blit(gameoverscreen, (0,0)) ###
            displaysurface.blit(game_over, (30,200))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
        for coin in coins:
            coin.rect.y += abs(P1.vel.y)
            if coin.rect.top >= HEIGHT:
                coin.kill()
    plat_gen()
#    displaysurface.fill((0,0,0))
    displaysurface.blit(background, (0,0)) ###
    for coin in coins: ###
        displaysurface.blit(coin.image, coin.rect)
        coin.update()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    score  = font_small.render(str(P1.score), True, (153,225,255))
    displaysurface.blit(score, (WIDTH/2, 10))
    pygame.display.update()
    FramePerSec.tick(FPS)
