

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Any
from functools import partial
from console import *



FPS = 30
WINDOW_SIZE = (800, 600)
# music = pygame.mixer.music.load('nhacnen.mp3')


class GAME_OPTIONS:
    run_loop_opt = True
    amluong_opt = True
    total_round = 1
    option_menu_main = None
    option_music = None
    
    def __init__(self) -> None:
        self.name = 'GAME_OPTIONS'  
        
gameoption = GAME_OPTIONS()



def on_button_click(value: str, text: Any = None) -> None:
    if value == "QUIT_MENU_OPTIONS":
        gameoption.run_loop_opt = False
    elif value == "AMLUONG_MENU_OPTIONS":
        if gameoption.amluong_opt == True:
            gameoption.amluong_opt = False
            pygame.mixer.music.stop()
            consolelog('TẮT ÂM LƯỢNG')
            pygame.display.set_mode((800, 600))
        else:
            gameoption.amluong_opt = True
            pygame.mixer.music.play(-1)
            consolelog('BẬT ÂM LƯỢNG')
            pygame.display.set_mode((800, 600))
    elif "TUYCHONSLC" in value:
            value = str.split(value,'|')
            gameoption.total_round = int(value[1])
            msg = "TỔNG SỐ LƯỢT CHƠI LÀ : " + value[1]
            consolelog(msg)
            pygame.display.set_mode((800, 600))
            
    elif "DOINHACNEN" in value:
            value = str.split(value,'|')
            if value[1] == '1' :
                gameoption.option_music = pygame.mixer.music.load('assets/nhacnen2.mp3')
            elif value[1] == '2' :
                gameoption.option_music = pygame.mixer.music.load('assets/nhacnen3.mp3')
            elif value[1] == '3' :
                gameoption.option_music = pygame.mixer.music.load('assets/nhacnen1.mp3')
            pygame.mixer.music.play(-1)

def paint_background(surface: 'pygame.Surface') -> None:
    """
    Paints a given surface with background color.
    :param surface: Pygame surface
    """
    surface.fill((128, 230, 198))


def make_long_menu() -> 'pygame_menu.Menu':
    """
    Create a long scrolling menu.
    :return: Menu
    """
    theme_menu = pygame_menu.themes.THEME_BLUE.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND

    # Main menu, pauses execution of the application
    menu = pygame_menu.Menu(
        height=500,
        theme=theme_menu,
        title='Tùy chọn',
        width=700
    )


    menu_tuychontslc = pygame_menu.Menu(
        height=500,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_SOLARIZED,
        title='Số lượt chơi với máy',
        width=700
    )


    # button_cochu = pygame_menu.Menu(
    #     height=400,
    #     onclose=pygame_menu.events.EXIT,
    #     theme=pygame_menu.themes.THEME_DARK,
    #     title='Tùy chọn cỡ chữ',
    #     width=600
    # )

    button_huongdan = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_DARK,
        title='Hưỡng dẫn',
        width=600
    )

    button_thaydoinhacnen = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_SOLARIZED,
        title='Thay đổi nhạc nền',
        width=600
    )

    menu.add.vertical_margin(20)  # Adds margin
    menu.add.button('Âm lượng', on_button_click , "AMLUONG_MENU_OPTIONS")
    menu.add.button('Thay đổi nhạc nền',button_thaydoinhacnen)
    
    # menu.add.button('Cỡ chữ', button_cochu)
    menu.add.button('Tùy chọn tổng số lượt chơi', menu_tuychontslc)
    menu.add.button('Hướng dẫn', button_huongdan)
    menu.add.vertical_margin(20)  # Adds margin
    
    
    
    menu.add.button('QUAY LẠI', on_button_click , "QUIT_MENU_OPTIONS")
    
    button_thaydoinhacnen.add.label(
        'LIST',
        max_char=40,
        align=pygame_menu.locals.ALIGN_CENTER,
        margin=(0, -1)
    )
    for i in range(1, 4):
        str_button_doinhacnen = "DOINHACNEN|" + str(i)
        button_thaydoinhacnen.add.button(str(i),on_button_click,str_button_doinhacnen)

    menu_tuychontslc.add.label(
        'ROUND',
        max_char=40,
        align=pygame_menu.locals.ALIGN_CENTER,
        margin=(0, -1)
    )
    for i in range(1, 15):
        str_button_cauhinh = "TUYCHONSLC|" + str(i)
        menu_tuychontslc.add.button(str(i),on_button_click,str_button_cauhinh)
    menu_tuychontslc.add.button('Quay lại', pygame_menu.events.BACK)
    # noinspection SpellCheckingInspection
    # button_cochu.add.label(
    #     'Chức năng này đang được cập nhật',
    #     max_char=33,
    #     align=pygame_menu.locals.ALIGN_LEFT,
    #     margin=(0, -1)
    # )
    button_huongdan.add.label(
        'Dưới đây là ba thể hiện phổ biến nhất. Cái Búa: Nắm các ngón tay lại . '
        'Cái Kéo: Hai ngón tay (ngón trỏ, ngón giữa) mở ra như chữ V, các ngón còn lại sẽ được nắm lại. '
        'Cái Bao: Xòe cả bàn tay ra. '
        'Để phân định thắng thua, người chơi cần nằm lòng quy tắc: Búa ăn kéo, thua Bao.'
        'Kéo cắt được Bao, thua Búa. Bao chùm được Búa, bị cắt bởi Kéo. Nếu người chơi ra dấu giống nhau sẽ được coi là hòa và sẽ tiến hành lại',
        max_char=40,
        align=pygame_menu.locals.ALIGN_LEFT,
        margin=(0, -1)
    )
    return menu


def options_menu(test: bool = False) -> None:
    
    screen = create_example_window('Options Menu', WINDOW_SIZE)
    gameoption.option_menu_main = make_long_menu()
    
    while True:
        events = pygame.event.get()
        gameoption.option_menu_main.update(events)
        gameoption.option_menu_main.draw(surface=screen)
        pygame.display.flip()
        
        if gameoption.run_loop_opt == False:
            gameoption.run_loop_opt = True
            break

