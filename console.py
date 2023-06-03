

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import threading
from typing import Any


class CONSOLE_PY_GAME:
    loop_console = True
    def __init__(self) -> None:
        self.name = 'CONSOLE PY GAME'  


console_pygame = CONSOLE_PY_GAME()

def on_button_click(value: str, text: Any = None) -> None:
    if value == "QUIT_MENU":
        console_pygame.loop_console = False


def make_long_menu(msg) -> 'pygame_menu.Menu':
    """
    Create a long scrolling menu.
    :return: Menu
    """
    theme_menu = pygame_menu.themes.THEME_BLUE.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND

    # Main menu, pauses execution of the application
    menu = pygame_menu.Menu(
        height=300,
        theme=theme_menu,
        title='Thông báo',
        width=500
    )
    menu.add.label(
        msg,
        max_char=35,
        align=pygame_menu.locals.ALIGN_CENTER,
        margin=(0, -1)
    )
    
    
    menu.add.button('OK', on_button_click , "QUIT_MENU")
    
    return menu


def consolelog(msg):
    
    screen = create_example_window('LOG', (500,300))
    option_menu_main = make_long_menu(msg)
    
    while True:
        events = pygame.event.get()
        option_menu_main.update(events)
        option_menu_main.draw(surface=screen)
        pygame.display.flip()
        if console_pygame.loop_console == False:
            console_pygame.loop_console = True
            break
        




