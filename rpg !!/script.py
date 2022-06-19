## following along from https://coderslegacy.com/python/pygame-rpg-game-tutorial/

import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *

pygame.init()  # Begin pygame

## variables
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 12
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

##display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

## animations (rn run and attacks are the same for left and right lol)
idle_ani_R = [pygame.image.load("jack idle 1.png"), pygame.image.load("jack idle 2.png"),
            pygame.image.load("jack idle 3.png"), pygame.image.load("jack idle 4.png"),
            pygame.image.load("jack idle 5.png"), pygame.image.load("jack idle 6.png"),
            pygame.image.load("jack idle 7.png"), pygame.image.load("jack idle 8.png")]
idle_ani_L = [pygame.image.load("jack idle L1.png"), pygame.image.load("jack idle L2.png"),
            pygame.image.load("jack idle L3.png"), pygame.image.load("jack idle L4.png"),
            pygame.image.load("jack idle L5.png"), pygame.image.load("jack idle L6.png"),
            pygame.image.load("jack idle L7.png"), pygame.image.load("jack idle L8.png")]

run_start_ani_R = [pygame.image.load("jack run start 1.png"), pygame.image.load("jack run start 2.png"),
            pygame.image.load("jack run start 3.png"), pygame.image.load("jack run start 4.png"),
            pygame.image.load("jack run start 5.png"), pygame.image.load("jack run start 6.png"),
            pygame.image.load("jack run start 7.png"), pygame.image.load("jack run start 8.png")]
run_start_ani_L = [pygame.image.load("jack run start L1.png"), pygame.image.load("jack run start L2.png"),
            pygame.image.load("jack run start L3.png"), pygame.image.load("jack run start L4.png"),
            pygame.image.load("jack run start L5.png"), pygame.image.load("jack run start L6.png"),
            pygame.image.load("jack run start L7.png"), pygame.image.load("jack run start L8.png")]

run_ani_R = [pygame.image.load("jack run 1.png"), pygame.image.load("jack run 2.png"),
            pygame.image.load("jack run 3.png"), pygame.image.load("jack run 4.png"),
            pygame.image.load("jack run 5.png"), pygame.image.load("jack run 6.png"),
            pygame.image.load("jack run 7.png"), pygame.image.load("jack run 8.png")]
run_ani_L = [pygame.image.load("jack run L1.png"), pygame.image.load("jack run L2.png"),
            pygame.image.load("jack run L3.png"), pygame.image.load("jack run L4.png"),
            pygame.image.load("jack run L5.png"), pygame.image.load("jack run L6.png"),
            pygame.image.load("jack run L7.png"), pygame.image.load("jack run L8.png")]

jump_ani_R = [pygame.image.load("jack jump 1.png"), pygame.image.load("jack jump 2.png"),
            pygame.image.load("jack jump 3.png"), pygame.image.load("jack jump 4.png"),
            pygame.image.load("jack jump 5.png"), pygame.image.load("jack jump 6.png"),
            pygame.image.load("jack jump 7.png"), pygame.image.load("jack jump 8.png")]
jump_ani_L = [pygame.image.load("jack jump L1.png"), pygame.image.load("jack jump L2.png"),
            pygame.image.load("jack jump L3.png"), pygame.image.load("jack jump L4.png"),
            pygame.image.load("jack jump L5.png"), pygame.image.load("jack jump L6.png"),
            pygame.image.load("jack jump L7.png"), pygame.image.load("jack jump L8.png")]

draw_ani_R = [pygame.image.load("jack draw 1.png"), pygame.image.load("jack draw 1.png"),
            pygame.image.load("jack draw 2.png"), pygame.image.load("jack draw 2.png"),
            pygame.image.load("jack draw 3.png"), pygame.image.load("jack draw 3.png"),
            pygame.image.load("jack draw 4.png"), pygame.image.load("jack draw 4.png")]
draw_ani_L = [pygame.image.load("jack draw L1.png"), pygame.image.load("jack draw L1.png"),
            pygame.image.load("jack draw L2.png"), pygame.image.load("jack draw L2.png"),
            pygame.image.load("jack draw L3.png"), pygame.image.load("jack draw L3.png"),
            pygame.image.load("jack draw L4.png"), pygame.image.load("jack draw L4.png")]

attack_ani_R = [pygame.image.load("jack attack 1.png"), pygame.image.load("jack attack 2.png"),
            pygame.image.load("jack attack 3.png"), pygame.image.load("jack attack 4.png"),
            pygame.image.load("jack attack 5.png"), pygame.image.load("jack attack 6.png"),
            pygame.image.load("jack attack 7.png"), pygame.image.load("jack attack 8.png")]
attack_ani_L = [pygame.image.load("jack attack L1.png"), pygame.image.load("jack attack L2.png"),
            pygame.image.load("jack attack L3.png"), pygame.image.load("jack attack L4.png"),
            pygame.image.load("jack attack L5.png"), pygame.image.load("jack attack L6.png"),
            pygame.image.load("jack attack L7.png"), pygame.image.load("jack attack L8.png")]

sheath_ani_R = [pygame.image.load("jack draw 5.png"), pygame.image.load("jack draw 5.png"),
            pygame.image.load("jack draw 6.png"), pygame.image.load("jack draw 6.png"),
            pygame.image.load("jack draw 7.png"), pygame.image.load("jack draw 7.png"),
            pygame.image.load("jack draw 8.png"), pygame.image.load("jack draw 8.png")]
sheath_ani_L = [pygame.image.load("jack draw L5.png"), pygame.image.load("jack draw L5.png"),
            pygame.image.load("jack draw L6.png"), pygame.image.load("jack draw L6.png"),
            pygame.image.load("jack draw L7.png"), pygame.image.load("jack draw L7.png"),
            pygame.image.load("jack draw L8.png"), pygame.image.load("jack draw L8.png")]

## classes
class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Background.png")
            self.rectBGimg = self.bgimage.get_rect()
            self.bgY = 0
            self.bgX = 0

      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center = (350, 350))
        self.bgX1 = 0
        self.bgY1 = 285

    def render(self):
        displaysurface.blit(self.image, (self.bgX1, self.bgY1))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jack idle 1.png")
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

        # Movement
        self.jumping = False
        self.running = False
        self.move_frame = 0
        self.attacking = False
        self.cooldown = False ###
        self.attack_frame = 0


    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        self.acc = vec(0,0.5)

        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

        # This causes character warping from one point of the screen to the other
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos  # Update rect with new pos

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player ,ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False


    def update(self):
        # Return to base frame if at end of movement sequence
        if self.move_frame > 7:
            self.move_frame = 0
            return
        # idle animation setup
        if self.running == False:
            if self.direction == "RIGHT":
                self.image = idle_ani_R[self.move_frame]
            else:
                self.image = idle_ani_L[self.move_frame]
            self.move_frame += 1
        # Move the character to the next frame if conditions are met
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1
        if self.jumping == True:
            if self.vel.x > 0:
                self.image = jump_ani_R[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = jump_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

          # Returns to base frame if standing still and incorrect frame is showing
    #      if abs(self.vel.x) < 0.2 and self.move_frame != 0:
    #            self.move_frame = 0
                #if self.direction == "RIGHT":
                #      self.image = run_ani_R[self.move_frame]
                #elif self.direction == "LEFT":
                #      self.image = run_ani_L[self.move_frame]

    def attack(self):
      # If attack frame has reached end of sequence, return to base frame
      if self.attack_frame > 7:
            self.attack_frame = 0
            self.attacking = False

      # Check direction for correct animation to display
      if self.direction == "RIGHT":
            self.image = attack_ani_R[self.attack_frame]
      elif self.direction == "LEFT":
            self.correction()
            self.image = attack_ani_L[self.attack_frame]

      # Update the current attack frame
      self.attack_frame += 1

    def correction(self):
      # Function is used to correct an error with character position on left attack frames
      if self.attack_frame == 1:
            self.pos.x -= 20
      if self.attack_frame == 10:
            self.pos.x += 20

    def jump(self):
        self.rect.x += 1

        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        self.rect.x -= 1

        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def player_hit(self): ###
        if self.cooldown == False:
            self.cooldown = True
            pygame.time.set_timer(hit_cooldown, 1000) #may be inaccurate b/c our framerate is different than the tutorial
            print("hit")
            pygame.display.update()

class Enemy(pygame.sprite.Sprite): ### all new baybey
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Branch.png")
        self.rect = self.image.get_rect()
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.direction = random.randint(0,1) #0 for right, 1 for left
        self.vel.x = random.randint(2,6) / 2

        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 235

    def move(self):
        if self.pos.x >= (WIDTH-15): #stops them going offscreen
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0
        if self.direction == 0: #directional movement
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x

        self.rect.center = self.pos #changes rect for collisions

    def render(self):
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

    def update(self):
        hits = pygame.sprite.spritecollide(self, Playergroup, False)
        if hits and player.attacking == True:
            self.kill()
        elif hits and player.attacking == False:
            player.hit()

##sprites
player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player) ###

background = Background()

ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

enemy = Enemy()

hit_cooldown = pygame.USEREVENT + 1 ###

##gameloop
while True:
    player.gravity_check()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True
        if event.type == hit_cooldown: ###
            player.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

    # sprite related functions
    player.update()
    if player.attacking == True:
        player.attack()
    player.move()
#    enemy.update()
#    enemy.move()

    # Display and Background related functions
    background.render()
    ground.render()

    # Rendering characters
    displaysurface.blit(player.image, player.rect)
#    enemy.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
