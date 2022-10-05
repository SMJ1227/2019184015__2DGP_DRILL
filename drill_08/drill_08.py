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
            if event.key == SDLK_RIGHT:
                dirrl += 1
            elif event.key == SDLK_LEFT:
                dirrl -= 1
            elif event.key == SDLK_UP:
                dirud += 1
            elif event.key == SDLK_DOWN:
                dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirrl -= 1
            elif event.key == SDLK_LEFT:
                dirrl += 1
            elif event.key == SDLK_UP:
                dirud -= 1
            elif event.key == SDLK_DOWN:
                dirud += 1
    pass


open_canvas(1280, 1024)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 1280 // 2
y = 1024 // 2
dirrl = 0
dirud = 0
rl = 3


def running_stop(frame):
    global rl
    clear_canvas()
    tuk_ground.draw(1280 // 2, 1024 // 2)
    character.clip_draw(frame * 100, 100 * rl, 100, 100, x, y)
    update_canvas()
    delay(0.01)


def running_right(frame):
    global x
    for x in range(x, x + 1, 10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += dirrl * 5
        delay(0.01)


def running_left(frame):
    global x
    for x in range(x, x - 1, -10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        x += dirrl * 5
        delay(0.01)


def running_up(frame):
    global x, y
    for y in range(y, y + 1, 10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += dirud * 5
        delay(0.01)


def running_down(frame):
    global x, y
    for y in range(y, y - 1, -10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * (rl-2), 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        y += dirud * 5
        delay(0.01)


while running:
    handle_events()

    if dirrl == 1:
        if x == 1280:
            pass
        else:
            running_right(0)
            if rl == 2:
                rl += 1
    elif dirrl == -1:
        if x == 0:
            pass
        else:
            running_left(0)
            if rl == 3:
                rl -= 1
    elif dirud == 1:
        if y > 1024:
            pass
        else:
            running_up(0)
    elif dirud == -1:
        if y < 0:
            pass
        else:
            running_down(0)
    elif dirrl == 0 and dirud == 0:
        running_stop(0)

close_canvas()
