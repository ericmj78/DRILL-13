import game_framework
import game_world
from pico2d import *


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_p:
                game_framework.pop_mode()
                return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
