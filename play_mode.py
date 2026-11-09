import game_framework
import game_world
import item_mode
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
            import title_mode
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode.toggle()
        elif not item_mode.handle_event(event, boy):
            boy.handle_event(event)


def init():
    global boy
    game_world.clear()
    item_mode.init()
    boy = Boy()
    boy.set_ball_size(item_mode.selected_ball_size)
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
    if not item_mode.is_active():
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_mode.draw()
    update_canvas()


def finish():
    global boy
    game_world.clear()
    item_mode.finish()
    boy = None
