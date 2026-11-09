from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {1: None, 2: None}

    def __init__(self, x, y, velocity, size=1):
        if size not in (1, 2):
            raise ValueError("공 크기는 1 또는 2여야 합니다.")

        if Ball.images[size] is None:
            image_name = 'ball21x21.png' if size == 1 else 'ball41x41.png'
            Ball.images[size] = load_image(image_name)

        self.image = Ball.images[size]
        self.x, self.y = x, y
        self.velocity = velocity
        self.size = size

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
