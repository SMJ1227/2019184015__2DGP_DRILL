from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 90
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.item = None
        self.image = load_image('animation_sheet.png')
        self.ball = load_image('ball21x21.png')
        self.big_ball = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 10
        if self.x >= 800:
            self.x = 800
            self.dir = -1
        elif self.x <= 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 100 * 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100 * 1, 100, 100, self.x, self.y)
        if self.item == 'Ball':
            self.ball.draw(self.x+10, self.y+50)
        elif self.item == 'BigBall':
            self.big_ball.draw(self.x+10, self.y+50)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                   #game_framework.quit()
                    game_framework.change_state(title_state)
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(add_delete_state)
    delay(0.01)


boys = []
grass = None
running = True

def enter():
    global grass, running, team
    boys.append(Boy())
    boys.append(Boy())
    grass = Grass()
    running = True

def exit():
    global grass
    for boy in boys:
        del boy
    del grass


def update():
    for boy in boys:
        boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()

def add_one_boy():
    boys.append(Boy())

def delete_one_boy():
    if len(boys) >= 2:
        boys.pop() #리스트 맨 마지막 요소를 꺼낸다. 제거와 동일

def set_boy_items(item):
    for boy in boys:
        boy.item = item

def pause():
    pass

def resume():
    pass