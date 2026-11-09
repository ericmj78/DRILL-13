import game_framework
import game_world
import pause_mode
from pico2d import *
from boy import Boy
from grass import Grass

boy = None


def handle_events():
    global boy
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)


def init():
    global boy
    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)
    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    if boy is not None and boy.state == 'RUN':
        boy.pressed_keys.clear()
        boy.dir = 0
        boy.stop_run()


def resume():
    pass


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    global boy
    game_world.clear()
    boy = None
