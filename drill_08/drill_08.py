from pico2d import *


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 2
            elif event.key == SDLK_LEFT:
                dir -= 2
            elif event.key == SDLK_UP:
                dir += 1
            elif event.key == SDLK_DOWN:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 2
            elif event.key == SDLK_LEFT:
                dir += 2
            elif event.key == SDLK_UP:
                dir -= 1
            elif event.key == SDLK_DOWN:
                dir += 1
    pass


open_canvas(1280, 1024)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
dir = 0


def running_stop(frame):
    clear_canvas()
    tuk_ground.draw(1280 // 2, 1024 // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
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
        x += dir * 5
        delay(0.01)


def running_left(frame):
    global x
    for x in range(x, x - 1, -10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        x += dir * 5
        delay(0.01)


def running_up(frame):
    global x, y
    for y in range(y, y + 1, 10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += dir * 5
        delay(0.01)


def running_down(frame):
    global x, y
    for y in range(y, y - 1, -10):
        clear_canvas()
        tuk_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame - 1) % 8
        y += dir * 5
        delay(0.01)

while running:
    handle_events()
    if x == 1280:
        running_stop(0)
    elif dir == 2:
        running_right(0)
    elif dir == 0:
        running_stop(0)
    elif dir == -2:
        running_left(0)
    elif dir == 1:
        running_up(0)
    elif dir == -1:
        running_down(0)





close_canvas()

