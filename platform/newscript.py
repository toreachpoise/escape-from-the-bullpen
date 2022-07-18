## bismillah

import pygame, sys, traceback, os, csv
from pygame.locals import *

try:
    clock = pygame.time.Clock()
    pygame.init()
    print("here we goooo")

    ## variables
    pygame.display.set_caption("escape the bullpen")
    vec = pygame.math.Vector2 #2d babey
    window_size = (1050, 525) #scaled from display
    screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 700
    display_height = 350
    display = pygame.Surface((display_width, display_height))
    acceleration = 5
    jump_height = 5
    friction = 0.1
    true_scroll = [0,0]
    scroll = true_scroll.copy()
    print("variables defined")

    class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Background.png")
            self.rect = self.image.get_rect()

      def render(self):
            display.blit(self.image, (0,0))

    class Ground(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("ground.png")
            self.rect = self.image.get_rect(topleft=(0, 325))
            self.image.set_colorkey((255,255,255))

        def render(self):
            display.blit(self.image, (0-scroll[0],325-scroll[1]))

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
            tilelist = pygame.sprite.Group()
            tiles = []
            map = self.read_csv(filename)
            y = 0
            for row in map:
                x = 0
                for tile in row:
                    if tile == '5': ##jack tile
                        self.start_x, self.start_y = x * self.tile_width, y * self.tile_height
                    elif tile == '0': ##cement bottom
                        tiles.append(Tile('cement bottom.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '1': ##cement top
                        tiles.append(Tile('cement top.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '2': ##interior
                        tiles.append(Tile('interior.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '3': ##scaffold
                        tiles.append(Tile('scaffold.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    ##bull tile ID is 4
                    x += 1
                y += 1 #move to next row
            for tile in tiles:
                tilelist.add(tile)
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
            self.pos = vec((tilemap.start_x, tilemap.start_y))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.image = pygame.image.load("jack idle 1.png")
            self.rect = self.image.get_rect(topleft=self.pos)

        def collision_test(self, tilelist):
            if abs(self.vel.x) > 0:
                print("moving horizontally")
                hits = pygame.sprite.spritecollide(self, tilelist, False)
                if hits:
                    print("horizontal collision")
                    if self.vel.x > 0:
                        #self.pos.x = hits[0].rect.left
                        #self.vel.x = 0
                        #self.acc.x = 0
                        print("right bump")
                    if self.vel.x < 0:
                        #self.pos.x = hits[0].rect.right
                        #self.vel.x = 0
                        #self.acc.x = 0
                        print("left bump")
            if abs(self.vel.y) > 0:
                print("moving vertically")
                hits = pygame.sprite.spritecollide(self, tilelist, False)
                if hits:
                    print("vertical collision")
                    if self.vel.y > 0:
                        self.pos.y = hits[0].rect.y - 59
                        self.vel.y = 0
                        self.acc.y = 0
                        print("bottom bump")
                    if self.vel.y < 0:
                        self.acc.y = 0.5
                        self.rect.top = hits[0].rect.bottom
                        print("top bump")

        def move(self):
            self.acc = vec(0,0.5) #downward acceleration aka gravity
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
                hits = pygame.sprite.spritecollide(self, tilelist, False)
                if hits:
                    print("jump")
                    self.y_direction = "UP"
                    self.pos.y -= jump_height
                    self.vel.y = -(5 * jump_height)
            if self.vel.y > 0:
                self.y_direction = "DOWN"
            self.vel.y += self.acc.y + acceleration
            self.pos.y += self.vel.y
            self.collision_test(tilelist)

            self.rect.topleft = self.pos

        def render(self):
            self.image = pygame.image.load("jack idle 1.png")
            display.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

    print("you got a class system, bitch")

    background = Background()
    ground = Ground()
    ground_group = pygame.sprite.Group()
    tilemap = TileMap("level 1.csv")
    tilelist = pygame.sprite.Group()
    ground_group.add(ground)
    jack = Player()
    print("sprites sprouted")


    while True:
        display.fill((146,244,255))

        true_scroll[0] += (jack.rect.x-true_scroll[0]-350)/20
        true_scroll[1] += (jack.rect.y-true_scroll[1]-175)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        background.render()
        ground.render()
        tilemap.load_map("level 1.csv")
        tilemap.render()
        jack.move()
        jack.render()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(pygame.transform.scale(display, window_size), (0,0)) #scaling display to fit the screen
        pygame.display.update()
        clock.tick(12) #number sets framerate in fps

except:
    print("you crashed bitch")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
