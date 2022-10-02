from pico2d import *

open_canvas(1680, 1050)

character = load_image('character.png')
x=400
y=90
clear_canvas_now()
character.draw_now(800,500)
delay(5)



close_canvas()
