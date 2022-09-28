from pico2d import *

open_canvas()
grass = load_image('grass.png')


def kirby_walking_right(frame):
    character = load_image('kirby_walking_right.png')
    for x in range(0, 800 + 1, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 96, 0, 95, 100, x, 90)

        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)
        get_events()


def kirby_walking_left(frame):
    character = load_image('kirby_walking_left.png')
    for x in range(800, 5 - 1, -5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 96, 0, 90, 100, x, 90)

        update_canvas()
        frame = (frame - 1) % 10
        delay(0.05)
        get_events()


def kirby_running_right(frame):
    character = load_image('kirby_running_right.png')
    for x in range(0, 800 + 1, 15):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 93, 0, 88, 100, x, 90)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()


def kirby_running_left(frame):
    character = load_image('kirby_running_left.png')
    for x in range(800, 15 - 1, -15):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 93, 0, 86, 100, x, 90)

        update_canvas()
        frame = (frame - 1) % 8
        delay(0.05)
        get_events()


def kirby_spin_right(frame):
    character = load_image('kirby_spin_right.png')
    for x in range(0, 800 + 1, 25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 108, 0, 100, 120, x, 90)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()


def kirby_spin_left(frame):
    character = load_image('kirby_spin_left.png')
    for x in range(800, 25 - 1, -25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 108, 0, 100, 120, x, 90)

        update_canvas()
        frame = (frame - 1) % 8
        delay(0.05)
        get_events()


def kirby_screaming(frame):
    character = load_image('kirby_screaming.png')
    for x in range(0, 800 + 1, 160):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 120, 400, 90)

        update_canvas()
        frame = (frame - 1) % 5
        delay(0.1)
        get_events()


kirby_walking_right(0)
kirby_walking_left(0)
kirby_running_right(0)
kirby_running_left(0)
kirby_spin_right(0)
kirby_spin_left(0)
kirby_screaming(0)

close_canvas()


#def kirby_rolling_right(frame):
#    character = load_image('kirby_rolling_right.png')
 #   for x in range(0, 800 + 1, 15):
  #      clear_canvas()
   #     grass.draw(400, 30)
    #    character.clip_draw(frame * 100, 0, 100, 110, x, 90)
#
 #       update_canvas()
  #      frame = (frame + 1) % 10
   #     delay(0.05)
    #    get_events()


#def kirby_rolling_left(frame):
 #   character = load_image('kirby_rolling_left.png')
  #  for x in range(800, 15-1, -15):
   #     clear_canvas()
    #    grass.draw(400, 30)
     #   character.clip_draw(frame * 105, 0, 100, 110, x, 90)
#
 #       update_canvas()
  #      frame = (frame - 1) % 10
   #     delay(0.05)
    #    get_events()


#kirby_rolling_right(0)
#kirby_rolling_left(0)