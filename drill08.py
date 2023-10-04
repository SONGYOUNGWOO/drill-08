from pico2d import *
import random


# Game object class here
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
    global team
    global world
    # 이 코드의 장점은 update wolrd 와 render world를 건드릴 필요 없이
    # 이제 클래스만을 wolrd 만을 고쳐서 사용할 수 있다.
    # global boy

    running = True
    world = []

    grass = Grass()
    world.append(grass)
    # boy = Boy()

    team = [Boy() for i in range(11)]
    world += team


def update_world():
    # grass.update()
    # # boy.update()
    # for boy in team:
    #     boy.update()
    # pass

    for o in world:
        o.update()


def render_world():
    clear_canvas()
    # grass.draw()
    # # boy.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()

    update_canvas()


open_canvas()
# initialization code 초기화 코드
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

# finalization code

close_canvas()
