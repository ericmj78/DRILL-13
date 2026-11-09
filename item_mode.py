from pico2d import load_image

image = None
active = False
selected_ball_size = 1


def init():
    global image, active, selected_ball_size
    image = load_image('item_select.png')
    active = False
    selected_ball_size = 1


def finish():
    global image, active
    image = None
    active = False


def toggle():
    global active
    active = not active
    return active


def is_active():
    return active


def handle_event(event, player):
    return False


def draw():
    if active and image is not None:
        image.draw(400, 300)
