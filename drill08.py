from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Bolls:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image_filename = random.choice(['ball21x21.png', 'ball41x41.png'])
        self.image = load_image(self.image_filename)

    def update(self):
        if self.y > 70:
            self.y -= random.randint(1, 30)
        else:
            if self.image_filename == 'ball21x21.png':
                self.y = 60
            else:
                self.y = 70

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team, bolls
    global world

    running = True
    world = []
    bolls = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    bolls = [Bolls() for i in range(20)]

    world += team
    world += bolls


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

close_canvas()
