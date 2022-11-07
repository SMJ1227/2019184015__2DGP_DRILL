from pico2d import *

class Grass:
    def __init__(self):
        self.layer = 0
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        if self.layer == 0:
            self.image.draw(400, 50)
            self.layer += 1
        elif self.layer == 1:
            self.image.draw(400, 30)
            self.layer -= 1