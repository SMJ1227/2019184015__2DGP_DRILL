import pico2d
import play_state
import logo_state

pico2d.open_canvas()

states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

#start_state = logo_state
#logo_state.enter()
#while logo_state.running:
#    logo_state.handle_events()
#    logo_state.update()
#    logo_state.draw()
#   pico2d.delay(0.05)
#logo_state.exit()
#
#play_state.enter()
#while play_state.running:
#    play_state.handle_events()
#    play_state.update()
#    play_state.draw()
#    pico2d.delay(0.05)
#play_state.exit()

pico2d.close_canvas()
