import pygame, sys
from button import Button

from options_menu import *
from game_menu_prestart import *

import threading
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("GAME OĂN TÙ TÌ")

BG = pygame.image.load("assets/background.jpeg")
gameoption.option_music = pygame.mixer.music.load('assets/nhacnen2.mp3')

pygame.mixer.music.play(-1)



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/OpenSans-Regular.ttf", size)



def main_menu():
    while True:


        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="BẮT ĐẦU", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="TÙY CHỌN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="THOÁT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu_prestart_func()
                    pygame.display.set_mode((1280, 720))
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_menu()
                    pygame.display.set_mode((1280, 720))
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        try:
            pygame.display.update()
        except:
            pass
        
        
main_menu()