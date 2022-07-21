import pygame, sys, traceback, os, csv
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (600,400) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
font = pygame.font.SysFont("Verdana", 60)
endgame = False
time_count = 0
waiting = font.render("Waiting", True, (0,0,0))
game_over = font.render("Game Over", True, (255,255,255))
display_width = 700
display_height = 350
display = pygame.Surface((display_width, display_height))

def wait():
    time_count += 1
    if time_count > 10:
        endgame = True

while True:
    wait()
    if endgame == False:
        print("waiting")
        display.fill((0,0,255))
        display.blit(waiting, (display_width/3, display_height/3))

    else:
        print("game over")
        display.fill((255,0,0))
        display.blit(game_over, (display_width/3, display_height/3))
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(1)
