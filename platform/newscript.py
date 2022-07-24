## bismillah

import pygame, sys, traceback, os, csv
from pygame.locals import *
from tkinter import *

try:
    clock = pygame.time.Clock()
    pygame.init()
    running = True
    print("here we goooo")

    ## variables
    pygame.display.set_caption("escape the bullpen")
    bullimg = pygame.image.load("branch.png")
    pygame.display.set_icon(bullimg)
    vec = pygame.math.Vector2 #2d babey
    window_size = (1260, 630) #scaled from display
    screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 700
    display_height = 350
    display = pygame.Surface((display_width, display_height))
    acceleration = 5
    jump_height = 7
    friction = 0.1
    topspeed = 20
    true_scroll = [0,0]
    gravity = 1
    falltodeath = 15
    scroll = true_scroll.copy()
    font = pygame.font.SysFont("Verdana", 60)
    fontsmall = pygame.font.SysFont("Verdana", 32)
    congratulations = font.render("congratulations", False, (255,255,255))
    completed1 = fontsmall.render("you have finished the demo", False, (0,0,0))
    completed2 = fontsmall.render("of Escape the Bullpen", False, (0,0,0))
    completed3 = fontsmall.render("full game coming soon", False, (200,0,50))
    gameover = pygame.image.load("game over screen.png")
    restart = fontsmall.render("press R to restart ...", False, (0,0,0))
    gameover.convert()
    print("variables defined")

    ##animations
    idle_ani_R = [pygame.image.load("jack idle 1.png"), pygame.image.load("jack idle 1.png"),
                pygame.image.load("jack idle 2.png"), pygame.image.load("jack idle 2.png"),
                pygame.image.load("jack idle 3.png"), pygame.image.load("jack idle 3.png"),
                pygame.image.load("jack idle 4.png"), pygame.image.load("jack idle 4.png")]
    idle_ani_L = [pygame.image.load("jack idle L1.png"), pygame.image.load("jack idle L1.png"),
                pygame.image.load("jack idle L2.png"), pygame.image.load("jack idle L2.png"),
                pygame.image.load("jack idle L3.png"), pygame.image.load("jack idle L3.png"),
                pygame.image.load("jack idle L4.png"), pygame.image.load("jack idle L4.png")]

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

    elevator_ani = [pygame.image.load("elevator 1.png"), pygame.image.load("elevator 2.png"),
                pygame.image.load("elevator 3.png"), pygame.image.load("elevator 4.png"),
                pygame.image.load("elevator 5.png"), pygame.image.load("elevator 6.png"),
                pygame.image.load("elevator 7.png"), pygame.image.load("elevator 7.png"), pygame.image.load("elevator 6.png"),
                pygame.image.load("elevator 5.png"), pygame.image.load("elevator 4.png"),
                pygame.image.load("elevator 3.png"), pygame.image.load("elevator 2.png"),
                pygame.image.load("elevator 1.png")]

    ## classes
    class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Background.png")
            self.rect = self.image.get_rect()

      def render(self):
            display.blit(self.image, (0,0))

    class Tile(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            if isinstance(self, Elevator):
                self.image = image
            else:
                self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
        def render(self, surface):
            display.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

    class TileMap():
        def __init__(self, filename):
            self.tile_width = 64
            self.tile_height = 32
            self.start_x, self.start_y = 0, 0
            self.tiles = self.load_tiles(filename)
            self.map_surface = pygame.Surface((self.map_w, self.map_h))
            self.map_surface.set_colorkey((0,0,0))
            self.elevator_pos_x, self.elevator_pos_y = 0, 0

        def load_tiles(self, filename):
            tilelist = []
            map = self.read_csv(filename)
            y = 0
            for row in map:
                x = 0
                for tile in row:
                    if tile == '5': ##jack tile
                        self.start_x, self.start_y = x * self.tile_width, y * self.tile_height
                    elif tile == '0': ##cement bottom
                        tilelist.append(Tile('cement bottom.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '1': ##cement top
                        tilelist.append(Tile('cement top.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '2': ##interior
                        tilelist.append(Tile('interior.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '3': ##scaffold
                        tilelist.append(Tile('scaffold.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    ##bull tile ID is 4
                    elif tile == '6': ##Elevator
                        tilelist.append(Elevator(elevator_ani, x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                        self.elevator_pos_x, self.elevator_pos_y = x * self.tile_width-scroll[0], (y * self.tile_height-scroll[1]) - 32
                    x += 1
                y += 1 #move to next row
            self.map_w, self.map_h = x * self.tile_height, y * self.tile_width
            return tilelist

        def render(self):
            display.blit(self.map_surface, (0-scroll[0],0-scroll[1]))

        def load_map(self, filename):
            self.load_tiles(filename)
            for tile in self.tiles:
                tile.render(self.map_surface)

        def read_csv(self, filename):
            map = []
            with open(os.path.join(filename)) as data:
                data = csv.reader(data, delimiter=',')
                for row in data:
                    map.append(list(row))
            return map

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.x_direction = "RIGHT"
            self.y_direction = "DOWN"
            self.move_frame = 0
            self.pos = vec((tilemap.start_x, tilemap.start_y))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.image = pygame.image.load("jack idle 1.png")
            self.rect = self.image.get_rect(topleft=self.pos)
            self.on_the_ground = False
            self.fallcount = 0
            self.died = False

        def collision_test(self, tilelist):
            if abs(self.vel.x) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        if self.pos.y + 50 >= tile.rect.y:
                            self.pos.y = tile.rect.bottom + 60
                            print("horizontal collision")
                            if self.x_direction == "LEFT":
                                self.pos.x = tile.rect.right
                                self.vel.x = 2 * acceleration
                                self.acc.x = 0
                                print("left bump")
                            if self.x_direction == "RIGHT":
                                self.pos.x = tile.rect.left - 60
                                self.vel.x = -2 * acceleration
                                self.acc.x = 0
                                print("right bump")
            if abs(self.vel.y) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        if self.vel.y > 0:
                            self.pos.y = tile.rect.y - 59
                            self.on_the_ground = True
                            self.fallcount = 0
                            self.vel.y = 0
                            self.acc.y = 0
                        if self.vel.y < 0:
                            self.acc.y = gravity
                            #self.pos.y = tile.rect.y + tilemap.tile_height

        def move(self):
            self.acc = vec(0,gravity) #downward acceleration aka gravity
            self.on_the_ground = False
            pressed_keys = pygame.key.get_pressed() # Returns the current key presses
            if pressed_keys[K_LEFT]: # Accelerates the player in the direction of the key press
                self.x_direction = "LEFT"
                self.acc.x = -acceleration
            if pressed_keys[K_RIGHT]:
                self.x_direction = "RIGHT"
                self.acc.x = acceleration
            self.vel.x += self.acc.x
            self.pos.x += self.vel.x
            if self.acc.x > 0:
                self.acc.x -= friction
            if self.acc.x < 0:
                self.acc.x += friction
            if abs(self.acc.x) < 0.1:
                self.acc.x = 0
                self.vel.x = 0
            if abs(self.vel.x) > topspeed:
                self.acc.x = 0
                if self.vel.x > 0:
                    self.vel.x = topspeed
                else:
                    self.vel.x = -topspeed
            self.collision_test(tilelist)
            if pressed_keys[K_SPACE]:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        print("jump")
                        self.y_direction = "UP"
                        self.pos.y -= jump_height
                        self.on_the_ground == False
                        self.vel.y = -(5 * jump_height)
            if self.vel.y > 0:
                self.y_direction = "DOWN"
            self.vel.y += self.acc.y + acceleration
            self.pos.y += self.vel.y
            self.collision_test(tilelist)
            if self.on_the_ground == False:
                self.fallcount += 1
            if self.fallcount >= falltodeath:
                self.died = True
            self.rect.topleft = self.pos


        def render(self):
            if self.fallcount == 0:
                if self.vel == (0,0):
                    if self.x_direction == "RIGHT":
                        self.image = idle_ani_R[self.move_frame]
                    elif self.x_direction == "LEFT":
                        self.image = idle_ani_L[self.move_frame]
                if self.vel.x > 0.3:
                    self.image = run_ani_R[self.move_frame]
                    self.x_direction = "RIGHT"
                if self.vel.x < -0.3:
                    self.image = run_ani_L[self.move_frame]
                    self.x_direction = "LEFT"
                if 0 < abs(self.vel.x) < 2:
                    if self.x_direction == "RIGHT":
                        self.image = run_start_ani_R[self.move_frame]
                    if self.x_direction == "LEFT":
                        self.image = run_start_ani_L[self.move_frame]
            else:
                # now that there's fallcount I can implement jump start and end animations
                if self.x_direction == "RIGHT":
                    self.image = jump_ani_R[self.move_frame]
                elif self.x_direction == "LEFT":
                    self.image = jump_ani_L[self.move_frame]
            self.move_frame+= 1
            if self.move_frame > 7: # Return to base frame if at end of movement sequence
                self.move_frame = 0
                return


    class Elevator(Tile):
        def __init__(self, image, x, y):
            self.move_frame = 0
            self.image = image[self.move_frame]
            self.image.set_colorkey((0,153,51))
            self.rect = self.image.get_rect()
            self.pos = (x, y)

        def render(self, map_surface):
            self.pos = tilemap.elevator_pos_x, tilemap.elevator_pos_y
            self.rect.topleft = self.pos
            self.move_frame+= 1
            if self.move_frame > 13: # Return to base frame if at end of movement sequence
                self.move_frame = 0
            pygame.draw.rect(display, (255,0,0), self.rect, 0)
            display.blit(self.image, self.pos)

        def stageend(self, player):
            if self.rect.left < (player.rect.right - true_scroll[0]):
                if self.rect.top <= player.rect.top: # + true_scroll[1]:
                    print("stage completed")
                    jack.kill()
                    display.fill((0,0,255))
                    display.blit(congratulations, (display_width/5, display_height/3))
                    display.blit(completed1, (display_width/10, display_height/2))
                    display.blit(completed2, (display_width/10, display_height/1.7))
                    display.blit(completed3, (display_width/10, display_height/1.4))

    class Handler():
        def init(self):
            self.level = 1

        def game_over(self):
            if jack.died:
                print("game over")
                display.fill((255,0,0))
                #self.root = Tk()
                #self.root.geometry('170x200')
                #button1 = Button(self.root, text="continue", width = 18, height = 5, command = self.restart)
                #button2 = Button(self.root, text="quit", width = 18, height = 5, command = self.quit)
                #button1.pack()
                #button2.pack()
                #self.root.mainloop()
                display.blit(gameover, (0,0))
                display.blit(restart, (display_width/10, display_height/1.2))
                pressed_keys = pygame.key.get_pressed() # Returns the current key presses
                if pressed_keys[K_r]:
                    handler.restart()
        def restart(self):
            #self.root.destroy()
            jack.died = False
            jack.fallcount = 0
            jack.pos.x = tilemap.start_x
            jack.pos.y = tilemap.start_y
        def quit(self):
            #self.root.destroy()
            running = False
            pygame.quit()
            sys.exit()

    print("you got a class system, bitch")


    background = Background()
    tilemap = TileMap("level 1.csv")
    tilelist = []
    jack = Player()
    elevator = Elevator(elevator_ani, tilemap.elevator_pos_x, tilemap.elevator_pos_y)
    handler = Handler()
    print("sprites sprouted")


    while running:

        true_scroll[0] += (jack.rect.x-true_scroll[0]-350)/20
        true_scroll[1] += (jack.rect.y-true_scroll[1]-100)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        background.render()
        #ground.render()
        tilemap.load_map("level 1.csv")
        tilemap.render()
        jack.move()
        jack.render()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

        display.blit(jack.image, (jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1]))
        elevator.render(tilemap.map_surface)
        #pygame.draw.rect(display, (0,0,255), [jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1], 60, 60], 0) ##representation of jack rect
        elevator.stageend(jack)
        handler.game_over()
        screen.blit(pygame.transform.scale(display, window_size), (0,0)) #scaling display to fit the screen
        pygame.display.update()
        clock.tick(24) #number sets framerate in fps

except:
    print("you crashed bitch")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
