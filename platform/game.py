## bismillah

import pygame, sys, traceback, os, csv, random # scipy.interpolate
from pygame.locals import *
from tkinter import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    FPS = 60
    animationspeed = 5 #fps of the animation will be 'FPS' divided by this number
    window_size = (1260, 630) #scaled from display
    screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 700
    display_height = 350
    display = pygame.Surface((display_width, display_height))
    acceleration = 5
    jump_height = FPS / (animationspeed)
    friction = 0.1
    topspeed = 10
    true_scroll = [0,0]
    gravity = 1
    falltodeath = 3 * jump_height
    scroll = true_scroll.copy()

    ## text onscreen
    font = pygame.font.SysFont("Verdana", 60)
    fontsmall = pygame.font.SysFont("Verdana", 32)
    congratulations = font.render("congratulations", False, (255,255,255))
    completed1 = fontsmall.render("you have finished the demo", False, (0,0,0))
    completed2 = fontsmall.render("of Escape the Bullpen", False, (0,0,0))
    completed3 = fontsmall.render("full game coming soon", False, (200,0,50))
    gameover = pygame.image.load("game over screen.png").convert_alpha()
    restart = fontsmall.render("press R to restart ...", False, (0,0,0))
    print("variables defined")

    ##animations & music
    idle_ani_R = [pygame.image.load("jack idle 1.png").convert_alpha(), pygame.image.load("jack idle 1.png").convert_alpha(),
                pygame.image.load("jack idle 2.png").convert_alpha(), pygame.image.load("jack idle 2.png").convert_alpha(),
                pygame.image.load("jack idle 3.png").convert_alpha(), pygame.image.load("jack idle 3.png").convert_alpha(),
                pygame.image.load("jack idle 4.png").convert_alpha(), pygame.image.load("jack idle 4.png").convert_alpha()]
    idle_ani_L = [pygame.image.load("jack idle L1.png").convert_alpha(), pygame.image.load("jack idle L1.png").convert_alpha(),
                pygame.image.load("jack idle L2.png").convert_alpha(), pygame.image.load("jack idle L2.png").convert_alpha(),
                pygame.image.load("jack idle L3.png").convert_alpha(), pygame.image.load("jack idle L3.png").convert_alpha(),
                pygame.image.load("jack idle L4.png").convert_alpha(), pygame.image.load("jack idle L4.png").convert_alpha()]

    run_start_ani_R = [pygame.image.load("jack run start 1.png").convert_alpha(), pygame.image.load("jack run start 2.png").convert_alpha(),
                pygame.image.load("jack run start 3.png").convert_alpha(), pygame.image.load("jack run start 4.png").convert_alpha(),
                pygame.image.load("jack run start 5.png").convert_alpha(), pygame.image.load("jack run start 6.png").convert_alpha(),
                pygame.image.load("jack run start 7.png"), pygame.image.load("jack run start 8.png")]
    run_start_ani_L = [pygame.image.load("jack run start L1.png").convert_alpha(), pygame.image.load("jack run start L2.png").convert_alpha(),
                pygame.image.load("jack run start L3.png").convert_alpha(), pygame.image.load("jack run start L4.png").convert_alpha(),
                pygame.image.load("jack run start L5.png").convert_alpha(), pygame.image.load("jack run start L6.png").convert_alpha(),
                pygame.image.load("jack run start L7.png").convert_alpha(), pygame.image.load("jack run start L8.png").convert_alpha()]

    run_ani_R = [pygame.image.load("jack run 1.png").convert_alpha(), pygame.image.load("jack run 2.png").convert_alpha(),
                pygame.image.load("jack run 3.png").convert_alpha(), pygame.image.load("jack run 4.png").convert_alpha(),
                pygame.image.load("jack run 5.png").convert_alpha(), pygame.image.load("jack run 6.png").convert_alpha(),
                pygame.image.load("jack run 7.png").convert_alpha(), pygame.image.load("jack run 8.png").convert_alpha()]
    run_ani_L = [pygame.image.load("jack run L1.png").convert_alpha(), pygame.image.load("jack run L2.png").convert_alpha(),
                pygame.image.load("jack run L3.png").convert_alpha(), pygame.image.load("jack run L4.png").convert_alpha(),
                pygame.image.load("jack run L5.png").convert_alpha(), pygame.image.load("jack run L6.png").convert_alpha(),
                pygame.image.load("jack run L7.png").convert_alpha(), pygame.image.load("jack run L8.png").convert_alpha()]

    attack_ani_R = [pygame.image.load("jack attack 1.png").convert_alpha(), pygame.image.load("jack attack 2.png").convert_alpha(),
                pygame.image.load("jack attack 3.png").convert_alpha(), pygame.image.load("jack attack 4.png").convert_alpha(),
                pygame.image.load("jack attack 5.png").convert_alpha(), pygame.image.load("jack attack 6.png").convert_alpha(),
                pygame.image.load("jack attack 7.png").convert_alpha(), pygame.image.load("jack attack 8.png").convert_alpha()]
    attack_ani_L = [pygame.image.load("jack attack L1.png").convert_alpha(), pygame.image.load("jack attack L2.png").convert_alpha(),
                pygame.image.load("jack attack L3.png").convert_alpha(), pygame.image.load("jack attack L4.png").convert_alpha(),
                pygame.image.load("jack attack L5.png").convert_alpha(), pygame.image.load("jack attack L6.png").convert_alpha(),
                pygame.image.load("jack attack L7.png").convert_alpha(), pygame.image.load("jack attack L8.png").convert_alpha()]

    jump_ani_R = [pygame.image.load("jack jump 1.png").convert_alpha(), pygame.image.load("jack jump 2.png").convert_alpha(),
                pygame.image.load("jack jump 3.png").convert_alpha(), pygame.image.load("jack jump 4.png").convert_alpha(),
                pygame.image.load("jack jump 5.png").convert_alpha(), pygame.image.load("jack jump 6.png").convert_alpha(),
                pygame.image.load("jack jump 7.png").convert_alpha(), pygame.image.load("jack jump 8.png").convert_alpha()]
    jump_ani_L = [pygame.image.load("jack jump L1.png").convert_alpha(), pygame.image.load("jack jump L2.png").convert_alpha(),
                pygame.image.load("jack jump L3.png").convert_alpha(), pygame.image.load("jack jump L4.png").convert_alpha(),
                pygame.image.load("jack jump L5.png").convert_alpha(), pygame.image.load("jack jump L6.png").convert_alpha(),
                pygame.image.load("jack jump L7.png").convert_alpha(), pygame.image.load("jack jump L8.png").convert_alpha()]

    elevator_ani = [pygame.image.load("elevator 1.png").convert_alpha(), pygame.image.load("elevator 2.png").convert_alpha(),
                pygame.image.load("elevator 3.png").convert_alpha(), pygame.image.load("elevator 4.png").convert_alpha(),
                pygame.image.load("elevator 5.png").convert_alpha(), pygame.image.load("elevator 6.png").convert_alpha(),
                pygame.image.load("elevator 7.png").convert_alpha(), pygame.image.load("elevator 7.png").convert_alpha(), pygame.image.load("elevator 6.png").convert_alpha(),
                pygame.image.load("elevator 5.png").convert_alpha(), pygame.image.load("elevator 4.png").convert_alpha(),
                pygame.image.load("elevator 3.png").convert_alpha(), pygame.image.load("elevator 2.png").convert_alpha(),
                pygame.image.load("elevator 1.png").convert_alpha()]

    cow_attack_R = [pygame.image.load("jack cow attack (1).png").convert_alpha(), pygame.image.load("jack cow attack (2).png").convert_alpha(),
                pygame.image.load("jack cow attack (3).png").convert_alpha(), pygame.image.load("jack cow attack (4).png").convert_alpha(),
                pygame.image.load("jack cow attack (5).png").convert_alpha(), pygame.image.load("jack cow attack (6).png").convert_alpha(),
                pygame.image.load("jack cow attack (7).png").convert_alpha(), pygame.image.load("jack cow attack (8).png").convert_alpha()]
    cow_attack_L = [pygame.image.load("jack cow attack L(1).png").convert_alpha(), pygame.image.load("jack cow attack L(2).png").convert_alpha(),
                pygame.image.load("jack cow attack L(3).png").convert_alpha(), pygame.image.load("jack cow attack L(4).png").convert_alpha(),
                pygame.image.load("jack cow attack L(5).png").convert_alpha(), pygame.image.load("jack cow attack L(6).png").convert_alpha(),
                pygame.image.load("jack cow attack L(7).png").convert_alpha(), pygame.image.load("jack cow attack L(8).png").convert_alpha()]

    cow_idle_R = [pygame.image.load("jack cow idle (1).png").convert_alpha(), pygame.image.load("jack cow idle (1).png").convert_alpha(),
                pygame.image.load("jack cow idle (2).png").convert_alpha(), pygame.image.load("jack cow idle (2).png").convert_alpha(),
                pygame.image.load("jack cow idle (3).png").convert_alpha(), pygame.image.load("jack cow idle (3).png").convert_alpha(),
                pygame.image.load("jack cow idle (4).png").convert_alpha(), pygame.image.load("jack cow idle (4).png").convert_alpha()]
    cow_idle_L = [pygame.image.load("jack cow idle L(1).png").convert_alpha(), pygame.image.load("jack cow idle L(1).png").convert_alpha(),
                pygame.image.load("jack cow idle L(2).png").convert_alpha(), pygame.image.load("jack cow idle L(2).png").convert_alpha(),
                pygame.image.load("jack cow idle L(3).png").convert_alpha(), pygame.image.load("jack cow idle L(3).png").convert_alpha(),
                pygame.image.load("jack cow idle L(4).png").convert_alpha(), pygame.image.load("jack cow idle L(4).png").convert_alpha()]

    cow_jump_R = [pygame.image.load("jack cow jump (1).png").convert_alpha(), pygame.image.load("jack cow jump (2).png").convert_alpha(),
                pygame.image.load("jack cow jump (3).png").convert_alpha(), pygame.image.load("jack cow jump (4).png").convert_alpha(),
                pygame.image.load("jack cow jump (5).png").convert_alpha(), pygame.image.load("jack cow jump (6).png").convert_alpha(),
                pygame.image.load("jack cow jump (7).png").convert_alpha(), pygame.image.load("jack cow jump (8).png").convert_alpha()]
    cow_jump_L = [pygame.image.load("jack cow jump L(1).png").convert_alpha(), pygame.image.load("jack cow jump L(2).png").convert_alpha(),
                pygame.image.load("jack cow jump L(3).png").convert_alpha(), pygame.image.load("jack cow jump L(4).png").convert_alpha(),
                pygame.image.load("jack cow jump L(5).png").convert_alpha(), pygame.image.load("jack cow jump L(6).png").convert_alpha(),
                pygame.image.load("jack cow jump L(7).png").convert_alpha(), pygame.image.load("jack cow jump L(8).png").convert_alpha()]

    cow_run_R = [pygame.image.load("jack cow run (1).png").convert_alpha(), pygame.image.load("jack cow run (2).png").convert_alpha(),
                pygame.image.load("jack cow run (3).png").convert_alpha(), pygame.image.load("jack cow run (4).png").convert_alpha(),
                pygame.image.load("jack cow run (5).png").convert_alpha(), pygame.image.load("jack cow run (6).png").convert_alpha(),
                pygame.image.load("jack cow run (7).png").convert_alpha(), pygame.image.load("jack cow run (8).png").convert_alpha()]
    cow_run_L = [pygame.image.load("jack cow run L(1).png").convert_alpha(), pygame.image.load("jack cow run L(2).png").convert_alpha(),
                pygame.image.load("jack cow run L(3).png").convert_alpha(), pygame.image.load("jack cow run L(4).png").convert_alpha(),
                pygame.image.load("jack cow run L(5).png").convert_alpha(), pygame.image.load("jack cow run L(6).png").convert_alpha(),
                pygame.image.load("jack cow run L(7).png").convert_alpha(), pygame.image.load("jack cow run L(8).png").convert_alpha()]

    cow_run_start_R = [pygame.image.load("jack cow run start (1).png").convert_alpha(), pygame.image.load("jack cow run start (2).png").convert_alpha(),
                pygame.image.load("jack cow run start (3).png").convert_alpha(), pygame.image.load("jack cow run start (4).png").convert_alpha(),
                pygame.image.load("jack cow run start (5).png").convert_alpha(), pygame.image.load("jack cow run start (6).png").convert_alpha(),
                pygame.image.load("jack cow run start (7).png").convert_alpha(), pygame.image.load("jack cow run start (8).png").convert_alpha()]
    cow_run_start_L = [pygame.image.load("jack cow run start L(1).png").convert_alpha(), pygame.image.load("jack cow run start L(2).png").convert_alpha(),
                pygame.image.load("jack cow run start L(3).png").convert_alpha(), pygame.image.load("jack cow run start L(4).png").convert_alpha(),
                pygame.image.load("jack cow run start L(5).png").convert_alpha(), pygame.image.load("jack cow run start L(6).png").convert_alpha(),
                pygame.image.load("jack cow run start L(7).png").convert_alpha(), pygame.image.load("jack cow run start L(8).png").convert_alpha()]

    ## classes
    class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Background.png").convert_alpha()
            self.rect = self.image.get_rect()

      def render(self):
            display.blit(self.image, (0,0))

    class Handler():
        def __init__(self):
            self.level = "1"
            self.stage_chosen = False

        def status_update(self):
            status_message = fontsmall.render(str(int(clock.get_fps())), False, (255,0,0))
            display.blit(status_message, (0,0))

        def choose_stage(self):
            if self.stage_chosen == False:
                self.root = Tk()
                self.root.geometry('200x330')
                button1 = Button(self.root, text = "Level 1", width = 18, height = 2, command = self.level1)
                button2 = Button(self.root, text = "Level 2", width = 18, height = 2, command = self.level2)
                button3a = Button(self.root, text = "Level 3a", width = 18, height = 2, command = self.level3a)
                button3br = Button(self.root, text = "Level 3b with rakesh", width = 18, height = 2, command = self.level3br)
                button3bn = Button(self.root, text = "Level 3b no rakesh", width = 18, height = 2, command = self.level3bn)
                button4 = Button(self.root, text = "Level 4", width = 18, height = 2, command = self.level4)
                button1.place(x = 40, y = 15)
                button2.place(x = 40, y = 65)
                button3a.place(x = 40, y = 115)
                button3br.place(x = 40, y = 165)
                button3bn.place(x = 40, y = 215)
                button4.place(x = 40, y = 265)
                self.root.mainloop()

        def level1(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "1"
            tilemap.tiles = tilemap.load_tiles("level 1.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("neonsigns.wav")
            pygame.mixer.music.play(-1)
            pass
        def level2(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "2"
            tilemap.tiles = tilemap.load_tiles("level 2.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("taurus.wav")
            pygame.mixer.music.play(-1)
            pass
        def level3a(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3a"
            tilemap.tiles = tilemap.load_tiles("level 3a.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("extracutscenestuff.wav")
            pygame.mixer.music.play(-1)
            pass
        def level3br(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3br"
            tilemap.tiles = tilemap.load_tiles("level 3b with rakesh.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("song3.wav")
            pygame.mixer.music.play(-1)
            pass
        def level3bn(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3bn"
            tilemap.tiles = tilemap.load_tiles("level 3b no rakesh.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("doctors.wav")
            pygame.mixer.music.play(-1)
            pass
        def level4(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "4"
            tilemap.tiles = tilemap.load_tiles("level 4.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pygame.mixer.music.unload()
            pygame.mixer.music.load("theescape.wav")
            pygame.mixer.music.play(-1)
            pass

        def game_over(self):
            if jack.died:
                print("game over")
                display.fill((204,51,0))
                display.blit(gameover, (0,0))
                display.blit(restart, (display_width/10, display_height/1.2))
                pressed_keys = pygame.key.get_pressed() # Returns the current key presses
                if pressed_keys[K_r]:
                    handler.restart()

        def restart(self):
            jack.died = False
            jack.fallcount = 0
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            jack.vel = vec(0,0)

        def quit(self):
            self.root.destroy()
            running = False
            pygame.quit()
            sys.exit()

        def stageend(self, tile, player):
            if player.rect.right >= tile.rect.x + scroll[0] and player.rect.bottom >= tile.rect.top - scroll[1]:
                    print("stage complete")
                    jack.kill()
                    jack.vel = vec(0,0)
                    self.stage_chosen = False
    handler = Handler()

    class Tile(pygame.sprite.Sprite):
        def __init__(self, image, x, y, tiletype):
            pygame.sprite.Sprite.__init__(self)
            if isinstance(self, Elevator):
                self.image = image
            else:
                self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
            self.tiletype = tiletype

        def move(self):
            if self.direction == 0:
                print("bull moving right")
                self.rect.x += self.vel.x
            if self.direction == 1:
                print("bull moving left")
                self.rect.x -= self.vel.x
            for tile in tilemap.tiles:
                if isinstance(tile, Bull):
                    pass
                else:
                    if self.rect.colliderect(tile.rect) == 1:
                        if self.direction == 0:
                            print("bull hit right")
                            self.direction = 1
                            self.rect.right = tile.rect.left
                        if self.direction == 1:
                            print("bull hit left")
                            self.direction = 0
                            self.rect.x = tile.rect.x + 64
            if handler.level == "3bn":
                pass
            else:
                if self.rect.colliderect(jack.rect) == 1:
                    if jack.attacking == True:
                        print("gottem")
                        self.alive = False
                        self.kill()
                    else:
                        jack.died = True

        def render(self, surface):
            if isinstance(self, Bull):
                if self.alive == True:
                    self.move()
                    #pygame.draw.rect(display, (0,0,255), [self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height], 0)
                    display.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))
                else:
                    self.kill()
                    try:
                        print("removed")
                        tilelist.remove(self)
                    except:
                        print("bull removal fail")
                        pass
            else:
                display.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

    class TileMap():
        def __init__(self, filename):
            self.tile_width = 64
            self.tile_height = 32
            self.start_x, self.start_y = 0, 0
            self.filename = "level 1.csv"
            if handler.level == "1":
                self.filename = "level 1.csv"
            elif handler.level == "2":
                self.filename = "level 2.csv"
            elif handler.level == "3a":
                self.filename = "level 3a.csv"
            elif handler.level == "3br":
                self.filename = "level 3b with rakesh.csv"
            elif handler.level == "3bn":
                self.filename = "level 3b no rakesh.csv"
            elif handler.level == "4":
                self.filename = "level 4.csv"
            self.tiles = self.load_tiles(self.filename)
            self.map_surface = pygame.Surface((self.map_w, self.map_h))
            self.map_surface.set_colorkey((0,0,0))
            self.elevator_pos_x, self.elevator_pos_y = 300, 0

        def load_tiles(self, filename):
            tilelist = []
            map = self.read_csv(filename)
            y = 0
            for row in map:
                x = 0
                for tile in row:
                    if tile == '5': ##jack tile
                        print("resetting jack position")
                        self.start_x, self.start_y = x * self.tile_width, y * self.tile_height
                    elif tile == '0': ##cement bottom
                        tilelist.append(Tile('cement bottom.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "cement"))
                    elif tile == '1': ##cement top
                        tilelist.append(Tile('cement top.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "cement"))
                    elif tile == '2': ##interior
                        tilelist.append(Tile('interior.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "interior"))
                    elif tile == '3': ##scaffold
                        tilelist.append(Tile('scaffold.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "scaffold"))
                    elif tile == '4': ##bull
                        tilelist.append(Bull('branch.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "bull"))
                    elif tile == '6': ##Elevator
                        tilelist.append(Elevator(elevator_ani, x * self.tile_width-scroll[0], y * self.tile_height-scroll[1], "elevator"))
                        self.elevator_pos_x, self.elevator_pos_y = x * self.tile_width-scroll[0], (y * self.tile_height-scroll[1])
                    x += 1
                y += 1 #move to next row
            self.map_w, self.map_h = x * self.tile_height, y * self.tile_width
            return tilelist

        def render(self, filename):
            for tile in self.tiles:
                if -self.tile_width < tile.rect.x-scroll[0] < display_width:
                    if -self.tile_height < tile.rect.y-scroll[1] < display_height:
                        tile.render(self.map_surface)
            display.blit(self.map_surface, (0,0))

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
            self.start_position = self.pos
            self.vel = vec(0,0)
            self.acc = vec(0,gravity)
            self.image = pygame.image.load("jack idle 1.png").convert_alpha()
            self.rect = self.image.get_rect(topleft = self.pos)
            self.on_the_ground = False
            self.fallcount = 0
            self.attacking = False
            self.attack_frame = 0
            self.died = False
            self.framecount = 0
            self.collidelist = 0

        def collision_test(self, tilelist):
            if abs(self.vel.x) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1 and tile.tiletype != "bull":
                        ## tiletype check is my lazy solution to bull tile rects not disappearing when killed =_=
                        if self.pos.y + 30 >= tile.rect.y:
                            self.pos.y = tile.rect.bottom + self.rect.height
                            #print("horizontal collision")
                            if self.x_direction == "LEFT":
                                self.pos.x = tile.rect.right + 5
                                self.vel.x = 2 * acceleration
                                self.acc.x = 0
                                #print("left bump")
                            if self.x_direction == "RIGHT":
                                self.pos.x = tile.rect.left - self.rect.width
                                self.vel.x = -2 * acceleration
                                self.acc.x = 0
                                #print("right bump")
            if abs(self.vel.y) > 0:
                self.collidelist = 0
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1 and tile.tiletype != "bull":
                        if self.vel.y > 0 and tile.rect.y >= self.rect.y - self.rect.height:
                            self.collidelist += 1
                            self.pos.y = tile.rect.y - (self.rect.height - 1)
                            self.on_the_ground = True
                            self.fallcount = 0
                            self.vel.y = 0
                            self.acc.y = 0
                        if self.vel.y < 0 and tile.rect.top <= self.rect.top:
                            if tile.tiletype != "scaffold":
                                print("hit head")
                                self.pos.y = tile.rect.bottom + self.rect.height
                                self.vel.y = 0
                                self.acc.y = gravity
                if self.collidelist == 0:
                    print("floating")
                    self.on_the_ground = False

        def move(self):
            pressed_keys = pygame.key.get_pressed() # Returns the current key presses
            if pressed_keys[K_RETURN]:
                if self.attacking == False:
                    self.attacking = True
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
                if self.fallcount <= 2:
                    print("jump")
                    self.y_direction = "UP"
                    self.on_the_ground == False
                    self.vel.y = -(4 * jump_height)
            if self.vel.y > 0:
                self.y_direction = "DOWN"
            self.vel.y += self.acc.y + acceleration
            self.pos.y += self.vel.y
            self.collision_test(tilelist)
            if self.on_the_ground == False:
                self.fallcount += 1
            if self.fallcount >= falltodeath and handler.level != "4":
                self.died = True
                self.vel = vec(0,0)
            self.rect.topleft = self.pos

        def render(self):
            if self.attacking: ##attack ani
                if self.attack_frame < 9:
                    if self.x_direction == "RIGHT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_attack_R[self.move_frame]
                        else:
                            self.image = attack_ani_R[self.move_frame]
                    elif self.x_direction == "LEFT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_attack_L[self.move_frame]
                        else:
                            self.image = attack_ani_L[self.move_frame]
                    self.attack_frame += 1
                else:
                    self.attack_frame = 0
                    self.attacking = False
            else:
                if self.vel == (0,0): ## idle ani
                    if self.x_direction == "RIGHT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_idle_R[self.move_frame]
                        else:
                            self.image = idle_ani_R[self.move_frame]
                    elif self.x_direction == "LEFT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_idle_L[self.move_frame]
                        else:
                            self.image = idle_ani_L[self.move_frame]
                if self.fallcount < 2:
                    if self.vel.x > 0.3: ## run
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_run_R[self.move_frame]
                        else:
                            self.image = run_ani_R[self.move_frame]
                        self.x_direction = "RIGHT"
                    if self.vel.x < -0.3:
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_run_L[self.move_frame]
                        else:
                            self.image = run_ani_L[self.move_frame]
                        self.x_direction = "LEFT"
                    if 0 < abs(self.vel.x) < 2: ##run start
                        if self.x_direction == "RIGHT":
                            if handler.level == "3bn" or handler.level == "4":
                                self.image = cow_run_start_R[self.move_frame]
                            else:
                                self.image = run_start_ani_R[self.move_frame]
                        if self.x_direction == "LEFT":
                            if handler.level == "3bn" or handler.level == "4":
                                self.image = cow_run_start_L[self.move_frame]
                            else:
                                self.image = run_start_ani_L[self.move_frame]
                else: ##jump
                    # now that there's fallcount I can implement jump start and end animations
                    if self.x_direction == "RIGHT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_jump_R[self.move_frame]
                        else:
                            self.image = jump_ani_R[self.move_frame]
                    elif self.x_direction == "LEFT":
                        if handler.level == "3bn" or handler.level == "4":
                            self.image = cow_jump_L[self.move_frame]
                        else:
                            self.image = jump_ani_L[self.move_frame]
            self.animate()

        def animate(self):
            self.framecount += 1
            if self.framecount == animationspeed:
                self.framecount = 0
                self.move_frame += 1
            if self.move_frame > 7: # Return to base frame if at end of movement sequence
                self.move_frame = 0
            if handler.level == "3bn" or handler.level == "4":
                display.blit(jack.image, (jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1] + 5))
            else:
                display.blit(jack.image, (jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1]))

    class Bull(Tile):
        def __init__(self, image, x, y, tiletype):
            super().__init__(image, x, y, tiletype)
            self.tiletype = tiletype
            self.image = pygame.image.load(image).convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.pos = vec(x,y)
            self.vel = vec(0,0)
            self.rect = self.mask.get_rect(midbottom=self.pos)
            self.direction = random.randint(0,1)
            self.vel.x = random.randint(2,6)/2
            self.alive = True

    class Elevator(Tile):
        def __init__(self, image, x, y, tiletype):
            self.tiletype = tiletype
            self.move_frame = 0
            self.image = image[self.move_frame]
            self.image.set_colorkey((0,153,51))
            self.rect = self.image.get_rect()
            self.pos = (x, y)

        def render(self, map_surface):
            self.pos = tilemap.elevator_pos_x - scroll[0], (tilemap.elevator_pos_y - 22) - scroll[1]
            self.rect.topleft = self.pos
            self.move_frame += 1
            if self.move_frame > 13: # Return to base frame if at end of movement sequence
                self.move_frame = 0
            #pygame.draw.rect(display, (255,0,0), self.rect, 0)
            display.blit(self.image, self.pos)

    print("you got a class system, bitch")


    background = Background()
    tilemap = TileMap("level 1.csv") ## change to change levels
    tilelist = []
    jack = Player()
    elevator = Elevator(elevator_ani, tilemap.elevator_pos_x, tilemap.elevator_pos_y, "elevator")
    #handler = Handler()
    print("sprites sprouted")
    print("running ...")

    while running:

        true_scroll[0] += (jack.rect.x-true_scroll[0]-350)/10
        true_scroll[1] += (jack.rect.y-true_scroll[1]-100)/10
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        background.render()
        #ground.render()
        tilemap.render("level 1.csv")
        jack.move()
        for event in pygame.event.get():
            if event.type == QUIT:
                handler.quit()
        #pygame.draw.rect(display, (0,0,255), [jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1], jack.rect.width, jack.rect.height], 0) ##representation of jack rect
        elevator.render(display)
        jack.render()
        handler.stageend(elevator, jack)
        handler.game_over()
        #handler.status_update() ##turn on to check fps
        handler.choose_stage()
        screen.blit(pygame.transform.scale(display, window_size), (0,0)) #scaling display to fit the screen
        pygame.display.update()
        clock.tick(FPS)

except:
    print("you crashed bitch")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
