from pico2d import *
import random

def handle_events():
    global running
    global dirrl, dirud
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                dirrl += 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                dirrl -= 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                dirud += 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d or event.key == SDLK_RIGHT:
                dirrl -= 1
            elif event.key == SDLK_a or event.key == SDLK_LEFT:
                dirrl += 1
            elif event.key == SDLK_w or event.key == SDLK_UP:
                dirud -= 1
            elif event.key == SDLK_s or event.key == SDLK_DOWN:
                dirud += 1
    pass


TUK_GROUND_FULL_WIDTH = 1280
TUK_GROUND_FULL_HEIGHT = 1024
open_canvas(TUK_GROUND_FULL_WIDTH, TUK_GROUND_FULL_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
monster = load_image('kirby_running_right.png')

running = True
character_x = TUK_GROUND_FULL_WIDTH // 2
character_y = TUK_GROUND_FULL_HEIGHT // 2
monster_x = random.randint(0,TUK_GROUND_FULL_WIDTH)
monster_y = random.randint(0,TUK_GROUND_FULL_HEIGHT)
dirrl = 0
dirud = 0
rl = 3
frame = 0
t = 0


def running_stop():
    global frame
    global rl
    #clear_canvas()
    #tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * rl, 100, 100, character_x, character_y)
    #update_canvas()
    #delay(0.01)


def running_right():
    global frame
    global character_x, character_y
    for character_x in range(character_x, character_x + 1, 20):
        #clear_canvas()
        #tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
        #update_canvas()
        frame = (frame + 1) % 8
        character_x += dirrl * 5
        character_y += dirud * 5
        #delay(0.01)


def running_left():
    global frame
    global character_x, character_y
    for character_x in range(character_x, character_x - 1, -20):
        # clear_canvas()
        # tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 0, 100, 100, character_x, character_y)
        #update_canvas()
        frame = (frame - 1) % 8
        character_x += dirrl * 5
        character_y += dirud * 5
        #delay(0.01)


def running_up():
    global frame
    global character_x, character_y
    for character_y in range(character_y, character_y + 1, 20):
        # clear_canvas()
        # tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, character_x, character_y)
        #update_canvas()
        frame = (frame + 1) % 8
        character_x += dirrl * 5
        character_y += dirud * 5
        #delay(0.01)


def running_down():
    global frame
    global character_x, character_y
    for character_y in range(character_y, character_y - 1, -20):
        # clear_canvas()
        # tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, character_x, character_y)
        #update_canvas()
        frame = (frame - 1) % 8
        character_x += dirrl * 5
        character_y += dirud * 5
        #delay(0.01)


def character_moving():
    global character_x, character_y
    global dirrl, dirud, rl
    if dirrl == 1:
        if character_x >= 1280 or character_y <= 0 or character_y >= 1024:
            pass
        else:
            running_right()
            if rl == 2:
                rl += 1
    elif dirrl == -1:
        if character_x <= 0 or character_y <= 0 or character_y >= 1024:
            pass
        else:
            running_left()
            if rl == 3:
                rl -= 1
    elif dirud == 1:
        if character_y >= 1024:
            pass
        else:
            running_up()
    elif dirud == -1:
        if character_y <= 0:
            pass
        else:
            running_down()
    elif dirrl == 0 and dirud == 0:
        running_stop()


def monster_running():
    global frame, t
    global monster_x, monster_y
    global character_x, character_y
    for x in range(0, 800 + 1, 15):
        monster_x = (1 - t) * monster_x + t * character_x
        monster_y = (1 - t) * monster_y + t * character_y
        monster.clip_draw(frame * 93, 0, 88, 100, monster_x, monster_y)
        frame = (frame + 1) % 4
        t += 0.00000005
        if t >= 1:
            t -= 1



while running:
    handle_events()
    clear_canvas()
    tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
    character_moving()
    monster_running()
    update_canvas()
    delay(0.03)

close_canvas()
