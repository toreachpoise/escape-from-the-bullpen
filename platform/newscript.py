## bismillah

import pygame, sys, traceback, os, csv
from pygame.locals import *

try:
    clock = pygame.time.Clock()
    pygame.init()
    running = True
    print("here we goooo")

    ## variables
    pygame.display.set_caption("escape the bullpen")
    vec = pygame.math.Vector2 #2d babey
    window_size = (1260, 630) #scaled from display
    screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 700
    display_height = 350
    display = pygame.Surface((display_width, display_height))
    acceleration = 5
    jump_height = 7
    friction = 0.1
    true_scroll = [0,0]
    gravity = 1
    scroll = true_scroll.copy()
    font = pygame.font.SysFont("Verdana", 60)
    game_over = font.render("Game Over", True, (255,255,255))
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

    ## classes
    class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Background.png")
            self.rect = self.image.get_rect()

      def render(self):
            display.blit(self.image, (0,0))


#    class Ground(pygame.sprite.Sprite):
#        def __init__(self):
#            super().__init__()
#            self.image = pygame.image.load("ground.png")
#            self.rect = self.image.get_rect(topleft=(0, 325))
#            self.image.set_colorkey((255,255,255))
#
#        def render(self):

##            display.blit(self.image, (0-scroll[0],325-scroll[1]))
    class Tile(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
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
            self.touching_ground = False
            self.pos = vec((tilemap.start_x, tilemap.start_y))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.image = pygame.image.load("jack idle 1.png")
            self.rect = self.image.get_rect(topleft=self.pos)
            self.health = 1

        def collision_test(self, tilelist):
            if abs(self.vel.x) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        print("horizontal collision")
                        if self.x_direction == "LEFT":
                            #self.pos.x = tile.rect.right
                            #self.vel.x = acceleration
                            #self.acc.x = 0
                            print("left bump")
                        if self.x_direction == "RIGHT":
                            #self.pos.x = tile.rect.left
                            #self.vel.x = -acceleration
                            #self.acc.x = 0
                            print("right bump")
            if abs(self.vel.y) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        if 0 < self.vel.y < 10:
                            self.pos.y = tile.rect.y - 59
                            self.touching_ground = True
                            self.vel.y = 0
                            self.acc.y = 0
                        if self.vel.y > 0:
                            self.health = 0
                            self.kill()
                        if self.vel.y < 0:
                            self.acc.y = gravity
                            #self.pos.y = tile.rect.y + tilemap.tile_height
        def move(self):
            self.acc = vec(0,gravity) #downward acceleration aka gravity
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
            self.collision_test(tilelist)
            if pressed_keys[K_SPACE]:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        print("jump")
                        self.y_direction = "UP"
                        self.pos.y -= jump_height
                        self.vel.y = -(5 * jump_height)
                        self.touching_ground = False
            if self.vel.y > 0:
                self.y_direction = "DOWN"
            self.vel.y += self.acc.y + acceleration
            self.pos.y += self.vel.y
            self.collision_test(tilelist)

            self.rect.topleft = self.pos

        def render(self):
            if self.touching_ground:
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
                if self.x_direction == "RIGHT":
                    self.image = jump_ani_R[self.move_frame]
                elif self.x_direction == "LEFT":
                    self.image = jump_ani_L[self.move_frame]
            self.move_frame+= 1
            if self.move_frame > 7: # Return to base frame if at end of movement sequence
                self.move_frame = 0
                return

    print("you got a class system, bitch")

    background = Background()
#    ground = Ground()
#    ground_group = pygame.sprite.Group()
    tilemap = TileMap("level 1.csv")
    tilelist = []
#    ground_group.add(ground)
    jack = Player()
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
        if jack.health == 1:
            display.blit(jack.image, (jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1]))
        else:
            display.fill((255,0,0))
            display.blit(game_over, (display_width/3, display_height/3))
        screen.blit(pygame.transform.scale(display, window_size), (0,0)) #scaling display to fit the screen
        pygame.display.update()
        clock.tick(24) #number sets framerate in fps

except:
    print("you crashed bitch")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
