init python:
    import pygame
    FPS = 60
    animationspeed = 3  #fps of the animation will be 'FPS' divided by this number
    #screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 1920
    display_height = 960
    display = renpy.Render(display_width, display_height)
    acceleration = 5
    jump_height = FPS / (animationspeed)
    friction = 0.1
    topspeed = 20
    true_scroll = [0,0]
    scroll = true_scroll.copy()
    gravity = 1
    falltodeath = 3 * jump_height
    jack_width = 30
    jack_height = 60

    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
        ##math operations for our vectors
        def __add__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x + other.x, self.y + other.y)
            return Vector(self.x + other, self.y + other)

        def __sub__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x - other.x, self.y - other.y)
            return Vector(self.x - other, self.y - other)

        def __mul__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x * other.x, self.y * other.y)
            return Vector(self.x * other, self.y * other)

        def __rmul__(self, other):
            return self.__mul__(other)

        def __truediv__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x / other.x, self.y / other.y)
            return Vector(self.x / other, self.y / other)

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.x == other.x and self.y == other.y
            return self.x == other and self.y == other

        def __neg__(self):
            return Vector(-self.x, -self.y)

        def make_int_tuple(self):
            return int(self.x), int(self.y)

        def set(self, vec):
            self.x = vec.x
            self.y = vec.y

    class Sprite():
        def __init__(self, width, height, x, y):
            self.width = width
            self.height = height
            self.position = Vector(x,y)

        def render(self, render, st, at):
            display = renpy.render(self.image, self.width, self.height, st, at)
            if isinstance(self, Tile):
                render.blit(display, (int(self.position.x-scroll[0]), int(self.position.y-scroll[1])))
            else:
                render.blit(display, (int(self.position.x), int(self.position.y)))

        def is_colliding(self,other):
            return(
                self.position.x <= other.position.x + other.width and
                self.position.x + self.width >= other.position.x and
                self.position.y <= other.position.y + other.height and
                self.position.y + self.height >= other.position.y
            )

    class Background(Sprite):
        def __init__(self, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.image = Image('/images/Minigame/background BIGGER.png')

    class Player(Sprite):
        def __init__(self, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.x_direction = "RIGHT"
            self.y_direction = "DOWN"
            self.move_frame = 0
            self.start_position = Vector(x, y)
            self.position = self.start_position
            self.width, self.height = width, height
            self.vel = Vector(0,0)
            self.acc = Vector(0, gravity)
            self.image = Image("/images/Minigame/jack idle 1.png")
            self.jumping = False
            self.attacking = False
            self.died = False
            self.on_the_ground = False

            self.run_right_ani = []
            self.run_left_ani = []
            self.run_start_right_ani = []
            self.run_start_left_ani = []
            self.idle_right_ani = []
            self.idle_left_ani = []
            self.jump_right_ani = []
            self.jump_left_ani = []
            self.attack_right_ani = []
            self.attack_left_ani = []

            self.cow_run_right_ani = []
            self.cow_run_left_ani = []
            self.cow_run_start_right_ani = []
            self.cow_run_start_left_ani = []
            self.cow_idle_right_ani = []
            self.cow_idle_left_ani = []
            self.cow_jump_right_ani = []
            self.cow_jump_left_ani = []
            self.cow_attack_right_ani = []
            self.cow_attack_left_ani = []

            self.run_right_ani.append(Image("/images/Minigame/jack run 1.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 2.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 3.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 4.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 5.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 6.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 7.png"))
            self.run_right_ani.append(Image("/images/Minigame/jack run 8.png"))
            for sprite in self.run_right_ani:
                self.run_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 1.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 2.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 3.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 4.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 5.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 6.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 7.png"))
            self.run_start_right_ani.append(Image("/images/Minigame/jack run start 8.png"))
            for sprite in self.run_start_right_ani:
                self.run_start_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.jump_right_ani.append(Image("/images/Minigame/jack jump 1.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 2.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 3.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 4.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 5.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 6.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 7.png"))
            self.jump_right_ani.append(Image("/images/Minigame/jack jump 8.png"))
            for sprite in self.jump_right_ani:
                self.jump_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.attack_right_ani.append(Image("/images/Minigame/jack attack 1.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 2.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 3.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 4.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 5.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 6.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 7.png"))
            self.attack_right_ani.append(Image("/images/Minigame/jack attack 8.png"))
            for sprite in self.attack_right_ani:
                self.attack_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.idle_right_ani.append(Image("/images/Minigame/jack idle 1.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 2.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 3.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 4.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 1.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 2.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 3.png"))
            self.idle_right_ani.append(Image("/images/Minigame/jack idle 4.png"))
            for sprite in self.idle_right_ani:
                self.idle_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (1).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (2).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (3).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (4).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (5).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (6).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (7).png"))
            self.cow_run_right_ani.append(Image("/images/Minigame/jack cow run (8).png"))
            for sprite in self.cow_run_right_ani:
                self.cow_run_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (1).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (2).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (3).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (4).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (5).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (6).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (7).png"))
            self.cow_run_start_right_ani.append(Image("/images/Minigame/jack cow run start (8).png"))
            for sprite in self.cow_run_start_right_ani:
                self.cow_run_start_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (1).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (2).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (3).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (4).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (5).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (6).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (7).png"))
            self.cow_jump_right_ani.append(Image("/images/Minigame/jack cow jump (8).png"))
            for sprite in self.cow_jump_right_ani:
                self.cow_jump_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (1).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (2).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (3).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (4).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (5).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (6).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (7).png"))
            self.cow_attack_right_ani.append(Image("/images/Minigame/jack cow attack (8).png"))
            for sprite in self.cow_attack_right_ani:
                self.cow_attack_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (1).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (2).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (3).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (4).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (1).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (2).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (3).png"))
            self.cow_idle_right_ani.append(Image("/images/Minigame/jack cow idle (4).png"))
            for sprite in self.cow_idle_right_ani:
                self.cow_idle_left_ani.append(Transform(sprite, xzoom=-1.0))

            self.image = self.idle_right_ani[self.move_frame]

        def update(self, keyboard):
            self.move(keyboard)
            self.animate()

        def move(self, keyboard):
            self.acc = Vector(0, gravity)
            if keyboard["left"]:
                self.x_direction == "LEFT"
                self.acc.x = -1 * acceleration
            elif keyboard["right"]:
                self.x_direction == "RIGHT"
                self.acc.x = acceleration
            if keyboard["space"] and self.on_the_ground:
                self.jumping = True
                self.vel.y = - jump_height
                self.position.y -= jump_height
            if keyboard["enter"]:
                self.attacking = True

            self.vel.x += self.acc.x
            if abs(self.acc.x) < 0.1:
                self.acc.x = 0
                self.vel.x = 0
            if abs(self.vel.x) >= topspeed:
                if self.x_direction == "RIGHT":
                    self.vel.x = topspeed
                else:
                    self.vel.x = -topspeed
                self.acc.x = 0
            if self.acc.x > 0:
                self.acc.x -= friction
            elif self.acc.x < 0:
                self.acc.x += friction
            self.position.x += self.vel.x + self.acc.x
            self.check_collisions(handler.tilelist)
            self.vel.y += self.acc.y
            self.position.y += self.vel.y + self.acc.y
            self.check_collisions(handler.tilelist)

            if self.position.x < -(jack_width/2):
                self.position.x = -(jack_width/2)
            elif self.position.x > display_width:
                self.position.x = display_width - (jack_width/2)
            if self.position.y <= 0:
                self.position.y = 0
            elif self.position.y >= display_height + jack_height:
                self.position.y = display_height

        def check_collisions(self, tilelist):
            collision_list = 0
            for tile in tilelist:
                if tile.is_colliding(self):
                    if self.vel.y > 0:
                        collision_list += 1
                        self.position.y = tile.position.y - jack_height + 5
                        self.vel.y = 0
                        self.on_the_ground = True
            if collision_list == 0:
                self.on_the_ground = False

        def animate(self):
            pass

    class Tile(Sprite):
        def __init__(self, image_int, x, y, tilelist, tiletype):
            Sprite.__init__(self, 64, 32, x, y)

            if image_int == 0:
                self.image = Image('/images/Minigame/cement bottom.png')
            elif image_int == 1:
                self.image = Image('/images/Minigame/cement top.png')
            elif image_int == 2:
                self.image = Image('/images/Minigame/interior.png')
            elif image_int == 3:
                self.image = Image('/images/Minigame/scaffold.png')
            elif image_int == 4:
                self.image = Image('/images/Minigame/branch.png')
            elif image_int == 6:
                self.image = Image('/images/Minigame/elevator 1.png')

            tilelist.append(self)

        def update(self):
            self.position.x = self.position.x - scroll[0]
            self.position.y = self.position.y - scroll[1]

    class Bull(Tile):
        def __init__(self, image, x, y, tilelist, tiletype):
            Tile.__init__(self, image, x, y, tilelist, tiletype)
            self.tiletype = tiletype
            self.image = Image(image)
            self.position = Vector(x,y)
            self.vel = Vector(0,0)
            self.direction = random.randint(0,1)
            self.vel.x = random.randint(2,6)/2
            self.alive = True

    class Elevator(Tile):
        def __init__(self, image, x, y, tilelist, tiletype):
            Tile.__init__(self, image, x, y, tilelist, tiletype)
            self.tiletype = tiletype
            self.image = Image('/images/Minigame/elevator 1.png')
            self.position = Vector(x,y)

    tilelist = []
    tile_width = 64
    tile_height = 32
    tile_map_1 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,5,-1,-1,-1,-1,3,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,-1,-1,-1,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,3,-1,-1,-1,-1,-1,-1,-1,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,3,3,3,3,3,3,3,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]

    for r in range(len(tile_map_1)):
        for c in range(len(tile_map_1[r])):
            if tile_map_1[r][c] == 5: ##jack
                pass
            elif tile_map_1[r][c] == 0:
                Tile(0, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'cement bottom')
            elif tile_map_1[r][c] == 1:
                Tile(1, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'cement top')
            elif tile_map_1[r][c] == 2:
                Tile(2, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'interior')
            elif tile_map_1[r][c] == 3:
                Tile(3, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'scaffold')
            elif tile_map_1[r][c] == 4:
                Bull(4, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'bull')
            elif tile_map_1[r][c] == 6:
                Elevator(6, c * tile_width - scroll[0], r * tile_height - scroll[1], tilelist, 'elevator')
    player = Player(jack_width, jack_height, 0, 0)
    background = Background(display_width, display_height, 0,0)

    class Handler(renpy.Displayable):
        def __init__(self, player, tilelist):
            renpy.Displayable.__init__(self)
            self.window_size = Vector(1920, 960)
            self.tilelist = tilelist
            self.keyboard = {"up": False, "down": False, "left": False, "right": False, "space": False, "enter": False}

        def render(self, width, height, st, at):
            background.render(display, st, at)
            for tile in self.tilelist:
                tile.update()
                if -tile_height < tile.position.y < display_height + tile_height:
                    if -tile_width < tile.position.x < display_width + tile_width:
                        tile.render(display, st, at)
            player.update(handler.keyboard)
            player.render(display, st, at)
            true_scroll[0] += (player.position.x-(display_width/2))/10
            true_scroll[1] += (player.position.y-(display_height/2))/10
            scroll = true_scroll.copy()
            scroll[0] = int(scroll[0])
            scroll[1] = int(scroll[1])
            renpy.redraw(self, 0)
            return display

        def event(self, ev, x, y, st):
            # Handles events

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.keyboard["up"] = True
                elif ev.key == pygame.K_DOWN:
                    self.keyboard["down"] = True
                elif ev.key == pygame.K_LEFT:
                    self.keyboard["left"] = True
                elif ev.key == pygame.K_RIGHT:
                    self.keyboard["right"] = True
                elif ev.key == pygame.K_SPACE:
                    self.keyboard["space"] = True
                    self.can_trigger_space_action = True
                elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
                    self.keyboard["shift"] = True
                    self.can_trigger_shift_action = True
                elif ev.key == pygame.K_RETURN:
                    self.keyboard["enter"] = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    self.keyboard["up"] = False
                elif ev.key == pygame.K_DOWN:
                    self.keyboard["down"] = False
                elif ev.key == pygame.K_LEFT:
                    self.keyboard["left"] = False
                elif ev.key == pygame.K_RIGHT:
                    self.keyboard["right"] = False
                elif ev.key == pygame.K_SPACE:
                    self.keyboard["space"] = False
                elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
                    self.keyboard["shift"] = False
                elif ev.key == pygame.K_RETURN:
                    self.keyboard["enter"] = False
            else:
                if renpy.map_event(ev, "pad_a_press"):
                    self.keyboard["space"] = True
                    self.can_trigger_space_action = True
                elif renpy.map_event(ev, "pad_a_release"):
                    self.keyboard["space"] = False

                if renpy.map_event(ev, "pad_b_press"):
                    self.keyboard["enter"] = True
                    self.can_trigger_shift_action = True
                elif renpy.map_event(ev, "pad_b_release"):
                    self.keyboard["enter"] = False

                if renpy.map_event(ev, "pad_lefty_neg") or renpy.map_event(ev, "pad_righty_neg") or renpy.map_event(ev, "pad_dpup_press"):
                    self.keyboard["up"] = True
                elif ((renpy.map_event(ev, "pad_lefty_zero") or renpy.map_event(ev, "pad_righty_zero")) and self.keyboard["up"]) or renpy.map_event(ev, "pad_dpup_release"):
                    self.keyboard["up"] = False

                if renpy.map_event(ev, "pad_lefty_pos") or renpy.map_event(ev, "pad_righty_pos") or renpy.map_event(ev, "pad_dpdown_press"):
                    self.keyboard["down"] = True
                elif ((renpy.map_event(ev, "pad_lefty_zero") or renpy.map_event(ev, "pad_righty_zero")) and self.keyboard["down"]) or renpy.map_event(ev, "pad_dpdown_release"):
                    self.keyboard["down"] = False

                if renpy.map_event(ev, "pad_leftx_neg") or renpy.map_event(ev, "pad_rightx_neg") or renpy.map_event(ev, "pad_dpleft_press"):
                    self.keyboard["left"] = True
                elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["left"]) or renpy.map_event(ev, "pad_dpleft_release"):
                    self.keyboard["left"] = False

                if renpy.map_event(ev, "pad_leftx_pos") or renpy.map_event(ev, "pad_rightx_pos") or renpy.map_event(ev, "pad_dpright_press"):
                    self.keyboard["right"] = True
                elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["right"]) or renpy.map_event(ev, "pad_dpright_release"):
                    self.keyboard["right"] = False

            # Ensure the screen updates
            renpy.restart_interaction()

            # If the player loses, return it
            #if self.player.died:
            #    return self.player.died
            #else:
            raise renpy.IgnoreEvent()

default handler = Handler(player, tilelist)

screen minigame(level):
    frame:
        yminimum 1080
        background "#000000"
        add "images/Minigame/background BIGGER.png" yalign 0.5
        add handler yalign 0.5
        textbutton "click to skip":
            action Return()
