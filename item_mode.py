from pico2d import load_image, SDL_KEYDOWN, SDLK_0, SDLK_1, SDLK_2

image = None
active = False
selected_ball_size = 1

KEY_TO_BALL_SIZE = {
    SDLK_0: 0,
    SDLK_1: 1,
    SDLK_2: 2,
}


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
    global selected_ball_size
    if not active or event.type != SDL_KEYDOWN:
        return False

    if event.key in KEY_TO_BALL_SIZE:
        selected_ball_size = KEY_TO_BALL_SIZE[event.key]
        player.set_ball_size(selected_ball_size)
        return True
    return False


def draw():
    if active and image is not None:
        image.draw(400, 300)
