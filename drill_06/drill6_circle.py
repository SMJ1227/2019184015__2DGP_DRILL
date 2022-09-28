from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

angle=270

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    x = 400 + (250*(math.cos(angle/360*2*math.pi)))
    y = 340 + (250*(math.sin(angle/360*2*math.pi)))
    character.draw_now(x,y)
    angle = angle + 2
    delay(0.001)

close_canvas()
