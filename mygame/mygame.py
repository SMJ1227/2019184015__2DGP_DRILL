from pico2d import *


def handle_events():
    global running
    global dirrl
    global dirud

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


TUK_GROUND_FULL_WIDTH = 3500
TUK_GROUND_FULL_HEIGHT = 1500
open_canvas(TUK_GROUND_FULL_WIDTH, TUK_GROUND_FULL_HEIGHT)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_GROUND_FULL_WIDTH // 2
y = TUK_GROUND_FULL_HEIGHT // 2
dirrl = 0
dirud = 0
rl = 3
frame = 0


def running_stop():
    global frame
    global rl
    clear_canvas()
    tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * rl, 100, 100, x, y)
    update_canvas()
    delay(0.01)


def running_right():
    global frame
    global x, y
    for x in range(x, x + 1, 20):
        clear_canvas()
        tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += dirrl * 5
        y += dirud * 5
        delay(0.01)


def running_left():
    global frame
    global x, y
    for x in range(x, x - 1, -20):
        clear_canvas()
        tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        x += dirrl * 5
        y += dirud * 5
        delay(0.01)


def running_up():
    global frame
    global x, y
    for y in range(y, y + 1, 20):
        clear_canvas()
        tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += dirrl * 5
        y += dirud * 5
        delay(0.01)


def running_down():
    global frame
    global x, y
    for y in range(y, y - 1, -20):
        clear_canvas()
        tuk_ground.draw(TUK_GROUND_FULL_WIDTH // 2, TUK_GROUND_FULL_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        x += dirrl * 5
        y += dirud * 5
        delay(0.01)


while running:
    handle_events()

    if dirrl == 1:
        if x >= 3020:
            pass
        else:
            running_right()
            if rl == 2:
                rl += 1
    elif dirrl == -1:
        if x == 470:
            pass
        else:
            running_left()
            if rl == 3:
                rl -= 1
    elif dirud == 1:
        if y >= 1470:
            pass
        else:
            running_up()
    elif dirud == -1:
        if y <= 30:
            pass
        else:
            running_down()
    elif dirrl == 0 and dirud == 0:
        running_stop()

close_canvas()
