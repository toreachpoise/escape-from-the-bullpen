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
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

##display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

## animations (rn run and attacks are the same for left and right lol)
run_ani_R = [pygame.image.load("run_1.png"), pygame.image.load("run_2.png"),
            pygame.image.load("run_3.png"), pygame.image.load("run_4.png"),
            pygame.image.load("run_5.png"), pygame.image.load("run_6.png"),
            pygame.image.load("run_7.png"), pygame.image.load("run_8.png")]
run_ani_L = [pygame.image.load("run_1.png"), pygame.image.load("run_2.png"),
            pygame.image.load("run_3.png"), pygame.image.load("run_4.png"),
            pygame.image.load("run_5.png"), pygame.image.load("run_6.png"),
            pygame.image.load("run_7.png"), pygame.image.load("run_8.png")]

jump_ani_R = [pygame.image.load("jack-r.png"), pygame.image.load("jack-r-jump-1.png"),
            pygame.image.load("jack-r-jump-2.png"), pygame.image.load("jack-r-jump-3.png"),
            pygame.image.load("jack-r-jump-4.png"), pygame.image.load("jack-r-jump-5.png"),
            pygame.image.load("jack-r-jump-4.png"), pygame.image.load("jack-r-jump-3.png"),
            pygame.image.load("jack-r-jump-2.png"), pygame.image.load("jack-r-jump-1.png")]
jump_ani_L = [pygame.image.load("jack-l.png"), pygame.image.load("jack-l-jump-1.png"),
            pygame.image.load("jack-l-jump-2.png"), pygame.image.load("jack-l-jump-3.png"),
            pygame.image.load("jack-l-jump-4.png"), pygame.image.load("jack-l-jump-5.png"),
            pygame.image.load("jack-l-jump-4.png"), pygame.image.load("jack-l-jump-3.png"),
            pygame.image.load("jack-l-jump-2.png"), pygame.image.load("jack-l-jump-1.png")]

attack_ani_R = [pygame.image.load("atk_1.png"), pygame.image.load("atk_2.png"),
            pygame.image.load("atk_3.png"), pygame.image.load("atk_4.png"),
            pygame.image.load("atk_5.png"), pygame.image.load("atk_6.png"),
            pygame.image.load("atk_7.png"), pygame.image.load("atk_8.png")]
attack_ani_L = [pygame.image.load("atk_1.png"), pygame.image.load("atk_2.png"),
            pygame.image.load("atk_3.png"), pygame.image.load("atk_4.png"),
            pygame.image.load("atk_5.png"), pygame.image.load("atk_6.png"),
            pygame.image.load("atk_7.png"), pygame.image.load("atk_8.png")]

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
        self.image = pygame.image.load("jack-r.png")
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
          if self.move_frame > 6:
                self.move_frame = 0
                return

          # Move the character to the next frame if conditions are met
          if self.jumping == False and self.running == True:
                if self.vel.x > 0:
                      self.image = run_ani_R[self.move_frame]
                      self.direction = "RIGHT"
                else:
                      self.image = run_ani_L[self.move_frame]
                      self.direction = "LEFT"
                self.move_frame += 1
          if self.jumping == True: ###
              if self.vel.x > 0:
                  self.image = jump_ani_R[self.move_frame]
                  self.direction = "RIGHT"
              else:
                  self.image = jump_ani_L[self.move_frame]
                  self.direction = "LEFT"
              self.move_frame += 1

          # Returns to base frame if standing still and incorrect frame is showing
          if abs(self.vel.x) < 0.2 and self.move_frame != 0:
                self.move_frame = 0
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


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()



##sprites
player = Player()
Playergroup = pygame.sprite.Group()

background = Background()

ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

##gameloop
while True:
    player.gravity_check()

    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass


        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True

    # Player related functions
    player.update()
    if player.attacking == True:
        player.attack()
    player.move()

    # Display and Background related functions
    background.render()
    ground.render()

    # Rendering Player
    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
