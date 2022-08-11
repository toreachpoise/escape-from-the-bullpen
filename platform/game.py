## bismillah

import pygame, sys, traceback, os, csv, random
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
    window_size = (1260, 630) #scaled from display
    screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 700
    display_height = 350
    display = pygame.Surface((display_width, display_height))
    acceleration = 5
    jump_height = 10
    friction = 0.1
    topspeed = 10
    true_scroll = [0,0]
    gravity = 1
    falltodeath = 25
    scroll = true_scroll.copy()
    font = pygame.font.SysFont("Verdana", 60)
    fontsmall = pygame.font.SysFont("Verdana", 32)
    congratulations = font.render("congratulations", False, (255,255,255))
    completed1 = fontsmall.render("you have finished the demo", False, (0,0,0))
    completed2 = fontsmall.render("of Escape the Bullpen", False, (0,0,0))
    completed3 = fontsmall.render("full game coming soon", False, (200,0,50))
    gameover = pygame.image.load("game over screen.png").convert_alpha()
    restart = fontsmall.render("press R to restart ...", False, (0,0,0))
    print("variables defined")

    ##animations
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
                self.root.geometry('200x283')
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
            pass
        def level2(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "2"
            tilemap.tiles = tilemap.load_tiles("level 2.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pass
        def level3a(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3a"
            tilemap.tiles = tilemap.load_tiles("level 3a.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pass
        def level3br(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3br"
            tilemap.tiles = tilemap.load_tiles("level 3b with rakesh.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pass
        def level3bn(self):
            self.root.destroy()
            self.stage_chosen = True
            self.level = "3bn"
            tilemap.tiles = tilemap.load_tiles("level 3b no rakesh.csv")
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
            pass
        def level4(self):
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
            #self.root.destroy()
            jack.died = False
            jack.fallcount = 0
            jack.pos = vec(tilemap.start_x, tilemap.start_y)
        def quit(self):
            #self.root.destroy()
            running = False
            pygame.quit()
            sys.exit()
        def stageend(self, tilelist, player):
            for tile in tilelist:
                if isinstance(tile, Elevator) and tile.rect.colliderect(player.rect):
                        print("stage completed")
                        jack.kill()
                        display.fill((0,0,255))
                        display.blit(congratulations, (display_width/5, display_height/3))
                        display.blit(completed1, (display_width/10, display_height/2))
                        display.blit(completed2, (display_width/10, display_height/1.7))
                        display.blit(completed3, (display_width/10, display_height/1.4))
                        stage_chosen = False
    handler = Handler()

    class Tile(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            if isinstance(self, Elevator):
                self.image = image
            else:
                self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y

        def move(self):
            if self.direction == 0:
                self.rect.x += self.vel.x
            if self.direction == 1:
                self.rect.x -= self.vel.x
            for tile in tilemap.tiles:
                if isinstance(tile, Bull):
                    pass
                else:
                    if self.rect.colliderect(tile.rect) == 1:
                        if tile.rect.y + 15 >= self.rect.y:
                            if self.direction == 0:
                                self.rect.x = tile.rect.x - 32
                                self.direction = 1
                            if self.direction == 1:
                                self.rect.x = tile.rect.x + 64
                                self.direction = 0

        def render(self, surface):
            if isinstance(self, Bull):
                self.move()
            display.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

    class TileMap():
        def __init__(self, filename):
            self.tile_width = 64
            self.tile_height = 32
            self.start_x, self.start_y = 0, 0
            self.filename = filename
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
                        self.start_x, self.start_y = x * self.tile_width, y * self.tile_height
                    elif tile == '0': ##cement bottom
                        tilelist.append(Tile('cement bottom.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '1': ##cement top
                        tilelist.append(Tile('cement top.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '2': ##interior
                        tilelist.append(Tile('interior.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '3': ##scaffold
                        tilelist.append(Tile('scaffold.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '4': ##bull
                        tilelist.append(Bull('branch.png', x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
                    elif tile == '6': ##Elevator
                        tilelist.append(Elevator(elevator_ani, x * self.tile_width-scroll[0], y * self.tile_height-scroll[1]))
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
            display.blit(self.map_surface, (0-scroll[0],0-scroll[1]))

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
            self.acc = vec(0,0)
            self.image = pygame.image.load("jack idle 1.png").convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.mask.get_rect(topleft = self.pos)
            self.on_the_ground = False
            self.fallcount = 0
            self.died = False
            self.framecount = 0

        def collision_test(self, tilelist):
            if abs(self.vel.x) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        if self.pos.y + 50 >= tile.rect.y:
                            self.pos.y = tile.rect.bottom + 60
                            print("horizontal collision")
                            if self.x_direction == "LEFT":
                                self.pos.x = tile.rect.right + 5
                                self.vel.x = 2 * acceleration
                                self.acc.x = 0
                                print("left bump")
                            if self.x_direction == "RIGHT":
                                self.pos.x = tile.rect.left - 65
                                self.vel.x = -2 * acceleration
                                self.acc.x = 0
                                print("right bump")
            if abs(self.vel.y) > 0:
                for tile in tilemap.tiles:
                    if self.rect.colliderect(tile.rect) == 1:
                        if self.vel.y > 0 and tile.rect.y >= self.rect.y - self.rect.height:
                            self.pos.y = tile.rect.y - 59
                            self.on_the_ground = True
                            self.fallcount = 0
                            self.vel.y = 0
                            self.acc.y = 0
                        if self.vel.y < 0 and abs(self.vel.x) < acceleration:
                            self.acc.y = gravity
                            self.vel.y = 0
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
                if self.fallcount <= 2:
                    print("jump")
                    self.y_direction = "UP"
                    self.pos.y -= jump_height
                    self.on_the_ground == False
                    self.vel.y = -(4 * jump_height)
            if self.vel.y > 0:
                self.y_direction = "DOWN"
            self.vel.y += self.acc.y + acceleration
            self.pos.y += self.vel.y
            self.collision_test(tilelist)
            if self.on_the_ground == False:
                self.fallcount += 1
            if self.fallcount >= falltodeath:
                self.died = True
                self.vel = vec(0,0)
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
            self.framecount += 1
            if self.framecount == 5:
                self.framecount = 0
                self.move_frame+= 1
            if self.move_frame > 7: # Return to base frame if at end of movement sequence
                self.move_frame = 0
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.mask.get_rect(topleft = self.pos)

    class Bull(Tile):
        def __init__(self, image, x, y):
            self.image = pygame.image.load(image).convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.pos = vec(x,y)
            self.vel = vec(0,0)
            self.rect = self.mask.get_rect(midtop=self.pos)
            self.direction = random.randint(0,1)
            self.vel.x = random.randint(2,6)/2


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
            self.move_frame += 1
            if self.move_frame > 13: # Return to base frame if at end of movement sequence
                self.move_frame = 0
            pygame.draw.rect(display, (255,0,0), self.rect, 0)
            display.blit(self.image, self.pos)


#    def Loadify(imgname):
#        return pygame.image.load(imgname).convert_alpha()

    print("you got a class system, bitch")


    background = Background()
    tilemap = TileMap("level 2.csv") ## change to change levels
    tilelist = []
    jack = Player()
    elevator = Elevator(elevator_ani, tilemap.elevator_pos_x, tilemap.elevator_pos_y)
    #handler = Handler()
    print("sprites sprouted")


    while running:

        true_scroll[0] += (jack.rect.x-true_scroll[0]-350)/10
        true_scroll[1] += (jack.rect.y-true_scroll[1]-100)/10
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        background.render()
        #ground.render()
        tilemap.render("level 3b with rakesh.csv")
        jack.move()
        jack.render()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.draw.rect(display, (0,0,255), [jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1], jack.rect.height, jack.rect.width], 0) ##representation of jack rect
        display.blit(jack.image, (jack.pos.x - true_scroll[0], jack.pos.y - true_scroll[1]))
        elevator.render(display)
        handler.stageend(tilelist, jack)
        handler.game_over()
        handler.status_update()
        handler.choose_stage()
        screen.blit(pygame.transform.scale(display, window_size), (0,0)) #scaling display to fit the screen
        pygame.display.update()
        clock.tick(FPS)

except:
    print("you crashed bitch")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
