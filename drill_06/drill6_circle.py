from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
x_angle=0
y_angle=270

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

    delay(1)

close_canvas()
