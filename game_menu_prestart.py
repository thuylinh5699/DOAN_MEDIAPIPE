

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Any
from functools import partial
from options_menu import *
from game_menu_haimay import *
from game_menu_motmay import *
from game_menu_hainguoi import *
from mqtt_server import *
import threading


FPS = 30
WINDOW_SIZE = (800, 600)
# music = pygame.mixer.music.load('nhacnen.mp3')


class GAME_PRE_START_OPTIONS:
    run_loop_opt = True
    option_menu_main = None
    
    def __init__(self) -> None:
        self.name = 'GAME_OPTIONS'  
        
menu_prestart = GAME_PRE_START_OPTIONS()



def on_button_click(value: str, text: Any = None) -> None:
    if value == "TROVE":
        menu_prestart.run_loop_opt = False
    elif value == "NHANDIENAI" :
        thead_playgame = threading.Thread(target=play_game_motmay, args=(gameoption.total_round,))
        thead_playgame.start()
        thead_playgame.join
        menu_prestart.run_loop_opt = False
    elif value == "HAIMAY" :
        thead_playgame = threading.Thread(target=play_game_haimay, args=(gameoption.total_round,))
        thead_playgame.start()
        thead_playgame.join
        menu_prestart.run_loop_opt = False
    elif value == "KETNOIMAYCHU" :
        thead_playgame = threading.Thread(target=connect_mqtt, args=())
        thead_playgame.start()
        thead_playgame.join
    elif value == "TIMKIEM" :
        thead_playgame = threading.Thread(target=timkiemnguoichoi, args=())
        thead_playgame.start()
        thead_playgame.join
    elif value == "VAOPHONG" :
        if mqtt_option.timkiem == True:
            thead_playgame = threading.Thread(target=play_game_hainguoi, args=(5,))
            thead_playgame.start()
            thead_playgame.join
            menu_prestart.run_loop_opt = False
            gui_vaophong()
        else:
            print('Mời bạn tìm kiếm người chơi')
    elif value == "NGATKETNOI":
        thead_playgame = threading.Thread(target=disconnect_mqtt, args=())
        thead_playgame.start()
        thead_playgame.join
    



def make_long_menu() -> 'pygame_menu.Menu':
    """
    Create a long scrolling menu.
    :return: Menu
    """
    theme_menu = pygame_menu.themes.THEME_BLUE.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND
    menu = pygame_menu.Menu(
        height=500,
        theme=theme_menu,
        title='Chọn chế độ',
        width=700
    )
    
    menu.add.button('Chế độ người chơi đấu với máy', on_button_click , "NHANDIENAI")
    menu.add.button('Chế độ hai máy tự đấu với nhau', on_button_click , "HAIMAY")
    button_online = pygame_menu.Menu(
        height=400,
        theme=pygame_menu.themes.THEME_SOLARIZED,
        title='BẠN ĐÃ SẴN SÀNG CHƯA',
        width=600
    )
    menu.add.button('Chế độ Online hai người chơi',button_online)
    menu.add.button('Trở về', on_button_click , "QUIT_MENU_OPTIONS")
    button_online.add.button("Kết nối máy chủ",on_button_click,"KETNOIMAYCHU")
    button_online.add.button("Tìm kiếm người chơi",on_button_click,"TIMKIEM")
    button_online.add.button("Vào phòng",on_button_click,"VAOPHONG")
    button_online.add.button("Ngắt kết nối máy chủ",on_button_click,"NGATKETNOI")
    button_online.add.button("Trở về",on_button_click,"TROVE")
    return menu
    


def menu_prestart_func(test: bool = False) -> None:
    
    screen = create_example_window('Pre StartGame', WINDOW_SIZE)
    menu_prestart.option_menu_main = make_long_menu()
    
    while True:
        events = pygame.event.get()
        menu_prestart.option_menu_main.update(events)
        menu_prestart.option_menu_main.draw(surface=screen)
        pygame.display.flip()
        
        if menu_prestart.run_loop_opt == False:
            menu_prestart.run_loop_opt = True
            break

