import sys
import pygame
import pyautogui
from settings import Settings
# from player_1 import Player_1
from pygame.locals import *
from PIL import Image
import json
import socket



class LostCity:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        with open('main/surface.json',"r",encoding='utf8') as f:
            self.surface_json:dict = json.load(f)
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.width_game_screen,self.settings.height_game_screen))
        self.settings.width =  self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        self.mouse_click_pos = (-1,-1)
        self.mouse_pos = (-1,-1)
        self.game_active_1 = True
        self.game_active_2 = False
        self.game_active_3 = False
        self.game_active_4 = False
        self.game_active_5 = False
        self.game_active_6 = False
        self.game_active_7 = False
        self.highlight_active_1 = False
        self.highlight_active_2 = False
        self.highlight_active_3 = False
        self.highlight_active_4 = False
        self.highlight_active_5 = False
        self.highlight_active_6 = False
        pygame.display.set_caption("Lost City")

    

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #侦听鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click_pos = pygame.mouse.get_pos()

            self._image_events()
            self._blit_events()
            self._check_button()
            self._blit_hightlight()
            self._highlight_button()

            pygame.display.flip()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_click_pos = (-1,-1)
            self.clock.tick(60)


# 绘制各个界面的原始图，一个检查鼠标点击的函数，开关为game_active
# 绘制高光图，一个检查鼠标碰到的函数，开关为highlight_active

#初始化图像
    def _image_events(self):
        #button_About_us_highlight
        self.button_About_us_highlight = pygame.image.load('main/images/button_About_us_highlight.png')
        self.button_About_us_highlight_2 = Image.open('main/images/button_About_us_highlight.png')
        self.button_About_us_highlight_width, self.button_About_us_highlight_height = self.button_About_us_highlight_2.size
        self.button_About_us_highlight_new = pygame.transform.scale(surface=self.button_About_us_highlight, size=(self.button_About_us_highlight_width * self.settings.RATIO_ALL, self.button_About_us_highlight_height * self.settings.RATIO_ALL))
        self.button_About_us_highlight_new_rect = self.button_About_us_highlight_new.get_rect()
        self.screen.blit(self.button_About_us_highlight_new, self.surface_json['button']['button_About_us_highlight'])



        #button_About_us_static
        self.button_About_us_static = pygame.image.load('main/images/button_About_us_static.png')
        self.button_About_us_static_2 = Image.open('main/images/button_About_us_static.png')
        self.button_About_us_static_width, self.button_About_us_static_height = self.button_About_us_static_2.size
        self.button_About_us_static_new = pygame.transform.scale(surface=self.button_About_us_static, size=(self.button_About_us_static_width * self.settings.RATIO_ALL, self.button_About_us_static_height * self.settings.RATIO_ALL))
        self.button_About_us_static_new_rect = self.button_About_us_static_new.get_rect()
        self.screen.blit(self.button_About_us_static_new, self.surface_json['button']['button_About_us_static'])



        #button_buy_dark
        self.button_buy_dark = pygame.image.load('main/images/button_buy_dark.png')
        self.button_buy_dark_2 = Image.open('main/images/button_buy_dark.png')
        self.button_buy_dark_width, self.button_buy_dark_height = self.button_buy_dark_2.size
        self.button_buy_dark_new = pygame.transform.scale(surface=self.button_buy_dark, size=(self.button_buy_dark_width * self.settings.RATIO_ALL, self.button_buy_dark_height * self.settings.RATIO_ALL))
        self.button_buy_dark_new_rect = self.button_buy_dark_new.get_rect()
        self.screen.blit(self.button_buy_dark_new, self.surface_json['button']['button_buy_dark'])



        #button_buy_shallow
        self.button_buy_shallow = pygame.image.load('main/images/button_buy_shallow.png')
        self.button_buy_shallow_2 = Image.open('main/images/button_buy_shallow.png')
        self.button_buy_shallow_width, self.button_buy_shallow_height = self.button_buy_shallow_2.size
        self.button_buy_shallow_new = pygame.transform.scale(surface=self.button_buy_shallow, size=(self.button_buy_shallow_width * self.settings.RATIO_ALL, self.button_buy_shallow_height * self.settings.RATIO_ALL))
        self.button_buy_shallow_new_rect = self.button_buy_shallow_new.get_rect()
        self.screen.blit(self.button_buy_shallow_new, self.surface_json['button']['button_buy_shallow'])



        #button_close_audio_highlight
        self.button_close_audio_highlight = pygame.image.load('main/images/button_close_audio_highlight.png')
        self.button_close_audio_highlight_2 = Image.open('main/images/button_close_audio_highlight.png')
        self.button_close_audio_highlight_width, self.button_close_audio_highlight_height = self.button_close_audio_highlight_2.size
        self.button_close_audio_highlight_new = pygame.transform.scale(surface=self.button_close_audio_highlight, size=(self.button_close_audio_highlight_width * self.settings.RATIO_ALL, self.button_close_audio_highlight_height * self.settings.RATIO_ALL))
        self.button_close_audio_highlight_new_rect = self.button_close_audio_highlight_new.get_rect()
        self.screen.blit(self.button_close_audio_highlight_new, self.surface_json['button']['button_close_audio_highlight'])



        #button_close_audio_static
        self.button_close_audio_static = pygame.image.load('main/images/button_close_audio_static.png')
        self.button_close_audio_static_2 = Image.open('main/images/button_close_audio_static.png')
        self.button_close_audio_static_width, self.button_close_audio_static_height = self.button_close_audio_static_2.size
        self.button_close_audio_static_new = pygame.transform.scale(surface=self.button_close_audio_static, size=(self.button_close_audio_static_width * self.settings.RATIO_ALL, self.button_close_audio_static_height * self.settings.RATIO_ALL))
        self.button_close_audio_static_new_rect = self.button_close_audio_static_new.get_rect()
        self.screen.blit(self.button_close_audio_static_new, self.surface_json['button']['button_close_audio_static'])



        #button_create_a_room_highlight
        self.button_create_a_room_highlight = pygame.image.load('main/images/button_create_a_room_highlight.png')
        self.button_create_a_room_highlight_2 = Image.open('main/images/button_create_a_room_highlight.png')
        self.button_create_a_room_highlight_width, self.button_create_a_room_highlight_height = self.button_create_a_room_highlight_2.size
        self.button_create_a_room_highlight_new = pygame.transform.scale(surface=self.button_create_a_room_highlight, size=(self.button_create_a_room_highlight_width * self.settings.RATIO_ALL, self.button_create_a_room_highlight_height * self.settings.RATIO_ALL))
        self.button_create_a_room_highlight_new_rect = self.button_create_a_room_highlight_new.get_rect()
        self.screen.blit(self.button_create_a_room_highlight_new, self.surface_json['button']['button_create_a_room_highlight'])



        #button_create_a_room_static
        self.button_create_a_room_static = pygame.image.load('main/images/button_create_a_room_static.png')
        self.button_create_a_room_static_2 = Image.open('main/images/button_create_a_room_static.png')
        self.button_create_a_room_static_width, self.button_create_a_room_static_height = self.button_create_a_room_static_2.size
        self.button_create_a_room_static_new = pygame.transform.scale(surface=self.button_create_a_room_static, size=(self.button_create_a_room_static_width * self.settings.RATIO_ALL, self.button_create_a_room_static_height * self.settings.RATIO_ALL))
        self.button_create_a_room_static_new_rect = self.button_create_a_room_static_new.get_rect()
        self.screen.blit(self.button_create_a_room_static_new, self.surface_json['button']['button_create_a_room_static'])



        #button_enter_your_room_address_highlight
        self.button_enter_your_room_address_highlight = pygame.image.load('main/images/button_enter_your_room_address_highlight.png')
        self.button_enter_your_room_address_highlight_2 = Image.open('main/images/button_enter_your_room_address_highlight.png')
        self.button_enter_your_room_address_highlight_width, self.button_enter_your_room_address_highlight_height = self.button_enter_your_room_address_highlight_2.size
        self.button_enter_your_room_address_highlight_new = pygame.transform.scale(surface=self.button_enter_your_room_address_highlight, size=(self.button_enter_your_room_address_highlight_width * self.settings.RATIO_ALL, self.button_enter_your_room_address_highlight_height * self.settings.RATIO_ALL))
        self.button_enter_your_room_address_highlight_new_rect = self.button_enter_your_room_address_highlight_new.get_rect()
        self.screen.blit(self.button_enter_your_room_address_highlight_new, self.surface_json['button']['button_enter_your_room_address_highlight'])



        #button_enter_your_room_address_static
        self.button_enter_your_room_address_static = pygame.image.load('main/images/button_enter_your_room_address_static.png')
        self.button_enter_your_room_address_static_2 = Image.open('main/images/button_enter_your_room_address_static.png')
        self.button_enter_your_room_address_static_width, self.button_enter_your_room_address_static_height = self.button_enter_your_room_address_static_2.size
        self.button_enter_your_room_address_static_new = pygame.transform.scale(surface=self.button_enter_your_room_address_static, size=(self.button_enter_your_room_address_static_width * self.settings.RATIO_ALL, self.button_enter_your_room_address_static_height * self.settings.RATIO_ALL))
        self.button_enter_your_room_address_static_new_rect = self.button_enter_your_room_address_static_new.get_rect()
        self.screen.blit(self.button_enter_your_room_address_static_new, self.surface_json['button']['button_enter_your_room_address_static'])



        #button_exit_dark
        self.button_exit_dark = pygame.image.load('main/images/button_exit_dark.png')
        self.button_exit_dark_2 = Image.open('main/images/button_exit_dark.png')
        self.button_exit_dark_width, self.button_exit_dark_height = self.button_exit_dark_2.size
        self.button_exit_dark_new = pygame.transform.scale(surface=self.button_exit_dark, size=(self.button_exit_dark_width * self.settings.RATIO_ALL, self.button_exit_dark_height * self.settings.RATIO_ALL))
        self.button_exit_dark_new_rect = self.button_exit_dark_new.get_rect()
        self.screen.blit(self.button_exit_dark_new, self.surface_json['button']['button_exit_dark'])



        #button_exit_shallow
        self.button_exit_shallow = pygame.image.load('main/images/button_exit_shallow.png')
        self.button_exit_shallow_2 = Image.open('main/images/button_exit_shallow.png')
        self.button_exit_shallow_width, self.button_exit_shallow_height = self.button_exit_shallow_2.size
        self.button_exit_shallow_new = pygame.transform.scale(surface=self.button_exit_shallow, size=(self.button_exit_shallow_width * self.settings.RATIO_ALL, self.button_exit_shallow_height * self.settings.RATIO_ALL))
        self.button_exit_shallow_new_rect = self.button_exit_shallow_new.get_rect()
        self.screen.blit(self.button_exit_shallow_new, self.surface_json['button']['button_exit_shallow'])



        #button_hide_dark
        self.button_hide_dark = pygame.image.load('main/images/button_hide_dark.png')
        self.button_hide_dark_2 = Image.open('main/images/button_hide_dark.png')
        self.button_hide_dark_width, self.button_hide_dark_height = self.button_hide_dark_2.size
        self.button_hide_dark_new = pygame.transform.scale(surface=self.button_hide_dark, size=(self.button_hide_dark_width * self.settings.RATIO_ALL, self.button_hide_dark_height * self.settings.RATIO_ALL))
        self.button_hide_dark_new_rect = self.button_hide_dark_new.get_rect()
        self.screen.blit(self.button_hide_dark_new, self.surface_json['button']['button_hide_dark'])



        #button_hide_shallow
        self.button_hide_shallow = pygame.image.load('main/images/button_hide_shallow.png')
        self.button_hide_shallow_2 = Image.open('main/images/button_hide_shallow.png')
        self.button_hide_shallow_width, self.button_hide_shallow_height = self.button_hide_shallow_2.size
        self.button_hide_shallow_new = pygame.transform.scale(surface=self.button_hide_shallow, size=(self.button_hide_shallow_width * self.settings.RATIO_ALL, self.button_hide_shallow_height * self.settings.RATIO_ALL))
        self.button_hide_shallow_new_rect = self.button_hide_shallow_new.get_rect()
        self.screen.blit(self.button_hide_shallow_new, self.surface_json['button']['button_hide_shallow'])



        #button_join_in_a_room_highlight
        self.button_join_in_a_room_highlight = pygame.image.load('main/images/button_join_in_a_room_highlight.png')
        self.button_join_in_a_room_highlight_2 = Image.open('main/images/button_join_in_a_room_highlight.png')
        self.button_join_in_a_room_highlight_width, self.button_join_in_a_room_highlight_height = self.button_join_in_a_room_highlight_2.size
        self.button_join_in_a_room_highlight_new = pygame.transform.scale(surface=self.button_join_in_a_room_highlight, size=(self.button_join_in_a_room_highlight_width * self.settings.RATIO_ALL, self.button_join_in_a_room_highlight_height * self.settings.RATIO_ALL))
        self.button_join_in_a_room_highlight_new_rect = self.button_join_in_a_room_highlight_new.get_rect()
        self.screen.blit(self.button_join_in_a_room_highlight_new, self.surface_json['button']['button_join_in_a_room_highlight'])



        #button_join_in_a_room_static
        self.button_join_in_a_room_static = pygame.image.load('main/images/button_join_in_a_room_static.png')
        self.button_join_in_a_room_static_2 = Image.open('main/images/button_join_in_a_room_static.png')
        self.button_join_in_a_room_static_width, self.button_join_in_a_room_static_height = self.button_join_in_a_room_static_2.size
        self.button_join_in_a_room_static_new = pygame.transform.scale(surface=self.button_join_in_a_room_static, size=(self.button_join_in_a_room_static_width * self.settings.RATIO_ALL, self.button_join_in_a_room_static_height * self.settings.RATIO_ALL))
        self.button_join_in_a_room_static_new_rect = self.button_join_in_a_room_static_new.get_rect()
        self.screen.blit(self.button_join_in_a_room_static_new, self.surface_json['button']['button_join_in_a_room_static'])



        #button_Multi_player_highlight
        self.button_Multi_player_highlight = pygame.image.load('main/images/button_Multi_player_highlight.png')
        self.button_Multi_player_highlight_2 = Image.open('main/images/button_Multi_player_highlight.png')
        self.button_Multi_player_highlight_width, self.button_Multi_player_highlight_height = self.button_Multi_player_highlight_2.size
        self.button_Multi_player_highlight_new = pygame.transform.scale(surface=self.button_Multi_player_highlight, size=(self.button_Multi_player_highlight_width * self.settings.RATIO_ALL, self.button_Multi_player_highlight_height * self.settings.RATIO_ALL))
        self.button_Multi_player_highlight_new_rect = self.button_Multi_player_highlight_new.get_rect()
        self.screen.blit(self.button_Multi_player_highlight_new, self.surface_json['button']['button_Multi_player_highlight'])



        #button_Muti_player_static
        self.button_Muti_player_static = pygame.image.load('main/images/button_Muti_player_static.png')
        self.button_Muti_player_static_2 = Image.open('main/images/button_Muti_player_static.png')
        self.button_Muti_player_static_width, self.button_Muti_player_static_height = self.button_Muti_player_static_2.size
        self.button_Muti_player_static_new = pygame.transform.scale(surface=self.button_Muti_player_static, size=(self.button_Muti_player_static_width * self.settings.RATIO_ALL, self.button_Muti_player_static_height * self.settings.RATIO_ALL))
        self.button_Muti_player_static_new_rect = self.button_Muti_player_static_new.get_rect()
        self.screen.blit(self.button_Muti_player_static_new, self.surface_json['button']['button_Muti_player_static'])



        #button_open_audio_highlight
        self.button_open_audio_highlight = pygame.image.load('main/images/button_open_audio_highlight.png')
        self.button_open_audio_highlight_2 = Image.open('main/images/button_open_audio_highlight.png')
        self.button_open_audio_highlight_width, self.button_open_audio_highlight_height = self.button_open_audio_highlight_2.size
        self.button_open_audio_highlight_new = pygame.transform.scale(surface=self.button_open_audio_highlight, size=(self.button_open_audio_highlight_width * self.settings.RATIO_ALL, self.button_open_audio_highlight_height * self.settings.RATIO_ALL))
        self.button_open_audio_highlight_new_rect = self.button_open_audio_highlight_new.get_rect()
        self.screen.blit(self.button_open_audio_highlight_new, self.surface_json['button']['button_open_audio_highlight'])



        #button_open_audio_static
        self.button_open_audio_static = pygame.image.load('main/images/button_open_audio_static.png')
        self.button_open_audio_static_2 = Image.open('main/images/button_open_audio_static.png')
        self.button_open_audio_static_width, self.button_open_audio_static_height = self.button_open_audio_static_2.size
        self.button_open_audio_static_new = pygame.transform.scale(surface=self.button_open_audio_static, size=(self.button_open_audio_static_width * self.settings.RATIO_ALL, self.button_open_audio_static_height * self.settings.RATIO_ALL))
        self.button_open_audio_static_new_rect = self.button_open_audio_static_new.get_rect()
        self.screen.blit(self.button_open_audio_static_new, self.surface_json['button']['button_open_audio_static'])



        #button_out_highlight
        self.button_out_highlight = pygame.image.load('main/images/button_out_highlight.png')
        self.button_out_highlight_2 = Image.open('main/images/button_out_highlight.png')
        self.button_out_highlight_width, self.button_out_highlight_height = self.button_out_highlight_2.size
        self.button_out_highlight_new = pygame.transform.scale(surface=self.button_out_highlight, size=(self.button_out_highlight_width * self.settings.RATIO_ALL, self.button_out_highlight_height * self.settings.RATIO_ALL))
        self.button_out_highlight_new_rect = self.button_out_highlight_new.get_rect()
        self.screen.blit(self.button_out_highlight_new, self.surface_json['button']['button_out_highlight'])



        #button_out_static
        self.button_out_static = pygame.image.load('main/images/button_out_static.png')
        self.button_out_static_2 = Image.open('main/images/button_out_static.png')
        self.button_out_static_width, self.button_out_static_height = self.button_out_static_2.size
        self.button_out_static_new = pygame.transform.scale(surface=self.button_out_static, size=(self.button_out_static_width * self.settings.RATIO_ALL, self.button_out_static_height * self.settings.RATIO_ALL))
        self.button_out_static_new_rect = self.button_out_static_new.get_rect()
        self.screen.blit(self.button_out_static_new, self.surface_json['button']['button_out_static'])



        #button_Rules_highlight
        self.button_Rules_highlight = pygame.image.load('main/images/button_Rules_highlight.png')
        self.button_Rules_highlight_2 = Image.open('main/images/button_Rules_highlight.png')
        self.button_Rules_highlight_width, self.button_Rules_highlight_height = self.button_Rules_highlight_2.size
        self.button_Rules_highlight_new = pygame.transform.scale(surface=self.button_Rules_highlight, size=(self.button_Rules_highlight_width * self.settings.RATIO_ALL, self.button_Rules_highlight_height * self.settings.RATIO_ALL))
        self.button_Rules_highlight_new_rect = self.button_Rules_highlight_new.get_rect()
        self.screen.blit(self.button_Rules_highlight_new, self.surface_json['button']['button_Rules_highlight'])



        #button_Rules_static
        self.button_Rules_static = pygame.image.load('main/images/button_Rules_static.png')
        self.button_Rules_static_2 = Image.open('main/images/button_Rules_static.png')
        self.button_Rules_static_width, self.button_Rules_static_height = self.button_Rules_static_2.size
        self.button_Rules_static_new = pygame.transform.scale(surface=self.button_Rules_static, size=(self.button_Rules_static_width * self.settings.RATIO_ALL, self.button_Rules_static_height * self.settings.RATIO_ALL))
        self.button_Rules_static_new_rect = self.button_Rules_static_new.get_rect()
        self.screen.blit(self.button_Rules_static_new, self.surface_json['button']['button_Rules_static'])



        #button_shop_dark
        self.button_shop_dark = pygame.image.load('main/images/button_shop_dark.png')
        self.button_shop_dark_2 = Image.open('main/images/button_shop_dark.png')
        self.button_shop_dark_width, self.button_shop_dark_height = self.button_shop_dark_2.size
        self.button_shop_dark_new = pygame.transform.scale(surface=self.button_shop_dark, size=(self.button_shop_dark_width * self.settings.RATIO_ALL, self.button_shop_dark_height * self.settings.RATIO_ALL))
        self.button_shop_dark_new_rect = self.button_shop_dark_new.get_rect()
        self.screen.blit(self.button_shop_dark_new, self.surface_json['button']['button_shop_dark'])



        #button_shop_shallow
        self.button_shop_shallow = pygame.image.load('main/images/button_shop_shallow.png')
        self.button_shop_shallow_2 = Image.open('main/images/button_shop_shallow.png')
        self.button_shop_shallow_width, self.button_shop_shallow_height = self.button_shop_shallow_2.size
        self.button_shop_shallow_new = pygame.transform.scale(surface=self.button_shop_shallow, size=(self.button_shop_shallow_width * self.settings.RATIO_ALL, self.button_shop_shallow_height * self.settings.RATIO_ALL))
        self.button_shop_shallow_new_rect = self.button_shop_shallow_new.get_rect()
        self.screen.blit(self.button_shop_shallow_new, self.surface_json['button']['button_shop_shallow'])



        #button_skip_dark
        self.button_skip_dark = pygame.image.load('main/images/button_skip_dark.png')
        self.button_skip_dark_2 = Image.open('main/images/button_skip_dark.png')
        self.button_skip_dark_width, self.button_skip_dark_height = self.button_skip_dark_2.size
        self.button_skip_dark_new = pygame.transform.scale(surface=self.button_skip_dark, size=(self.button_skip_dark_width * self.settings.RATIO_ALL, self.button_skip_dark_height * self.settings.RATIO_ALL))
        self.button_skip_dark_new_rect = self.button_skip_dark_new.get_rect()
        self.screen.blit(self.button_skip_dark_new, self.surface_json['button']['button_skip_dark'])



        #button_skip_shallow
        self.button_skip_shallow = pygame.image.load('main/images/button_skip_shallow.png')
        self.button_skip_shallow_2 = Image.open('main/images/button_skip_shallow.png')
        self.button_skip_shallow_width, self.button_skip_shallow_height = self.button_skip_shallow_2.size
        self.button_skip_shallow_new = pygame.transform.scale(surface=self.button_skip_shallow, size=(self.button_skip_shallow_width * self.settings.RATIO_ALL, self.button_skip_shallow_height * self.settings.RATIO_ALL))
        self.button_skip_shallow_new_rect = self.button_skip_shallow_new.get_rect()
        self.screen.blit(self.button_skip_shallow_new, self.surface_json['button']['button_skip_shallow'])



        #button_trap_dark
        self.button_trap_dark = pygame.image.load('main/images/button_trap_dark.png')
        self.button_trap_dark_2 = Image.open('main/images/button_trap_dark.png')
        self.button_trap_dark_width, self.button_trap_dark_height = self.button_trap_dark_2.size
        self.button_trap_dark_new = pygame.transform.scale(surface=self.button_trap_dark, size=(self.button_trap_dark_width * self.settings.RATIO_ALL, self.button_trap_dark_height * self.settings.RATIO_ALL))
        self.button_trap_dark_new_rect = self.button_trap_dark_new.get_rect()
        self.screen.blit(self.button_trap_dark_new, self.surface_json['button']['button_trap_dark'])



        #button_trap_shallow
        self.button_trap_shallow = pygame.image.load('main/images/button_trap_shallow.png')
        self.button_trap_shallow_2 = Image.open('main/images/button_trap_shallow.png')
        self.button_trap_shallow_width, self.button_trap_shallow_height = self.button_trap_shallow_2.size
        self.button_trap_shallow_new = pygame.transform.scale(surface=self.button_trap_shallow, size=(self.button_trap_shallow_width * self.settings.RATIO_ALL, self.button_trap_shallow_height * self.settings.RATIO_ALL))
        self.button_trap_shallow_new_rect = self.button_trap_shallow_new.get_rect()
        self.screen.blit(self.button_trap_shallow_new, self.surface_json['button']['button_trap_shallow'])



        #button_war_dark
        self.button_war_dark = pygame.image.load('main/images/button_war_dark.png')
        self.button_war_dark_2 = Image.open('main/images/button_war_dark.png')
        self.button_war_dark_width, self.button_war_dark_height = self.button_war_dark_2.size
        self.button_war_dark_new = pygame.transform.scale(surface=self.button_war_dark, size=(self.button_war_dark_width * self.settings.RATIO_ALL, self.button_war_dark_height * self.settings.RATIO_ALL))
        self.button_war_dark_new_rect = self.button_war_dark_new.get_rect()
        self.screen.blit(self.button_war_dark_new, self.surface_json['button']['button_war_dark'])



        #button_war_shallow
        self.button_war_shallow = pygame.image.load('main/images/button_war_shallow.png')
        self.button_war_shallow_2 = Image.open('main/images/button_war_shallow.png')
        self.button_war_shallow_width, self.button_war_shallow_height = self.button_war_shallow_2.size
        self.button_war_shallow_new = pygame.transform.scale(surface=self.button_war_shallow, size=(self.button_war_shallow_width * self.settings.RATIO_ALL, self.button_war_shallow_height * self.settings.RATIO_ALL))
        self.button_war_shallow_new_rect = self.button_war_shallow_new.get_rect()
        self.screen.blit(self.button_war_shallow_new, self.surface_json['button']['button_war_shallow'])



        #figure_player1_others
        self.figure_player1_others = pygame.image.load('main/images/figure_player1_others.png')
        self.figure_player1_others_2 = Image.open('main/images/figure_player1_others.png')
        self.figure_player1_others_width, self.figure_player1_others_height = self.figure_player1_others_2.size
        self.figure_player1_others_new = pygame.transform.scale(surface=self.figure_player1_others, size=(self.figure_player1_others_width * self.settings.RATIO_ALL, self.figure_player1_others_height * self.settings.RATIO_ALL))
        self.figure_player1_others_new_rect = self.figure_player1_others_new.get_rect()
        self.screen.blit(self.figure_player1_others_new, self.surface_json['figure']['figure_player1_others'])



        #figure_player1_you
        self.figure_player1_you = pygame.image.load('main/images/figure_player1_you.png')
        self.figure_player1_you_2 = Image.open('main/images/figure_player1_you.png')
        self.figure_player1_you_width, self.figure_player1_you_height = self.figure_player1_you_2.size
        self.figure_player1_you_new = pygame.transform.scale(surface=self.figure_player1_you, size=(self.figure_player1_you_width * self.settings.RATIO_ALL, self.figure_player1_you_height * self.settings.RATIO_ALL))
        self.figure_player1_you_new_rect = self.figure_player1_you_new.get_rect()
        self.screen.blit(self.figure_player1_you_new, self.surface_json['figure']['figure_player1_you'])



        #figure_player2_others
        self.figure_player2_others = pygame.image.load('main/images/figure_player2_others.png')
        self.figure_player2_others_2 = Image.open('main/images/figure_player2_others.png')
        self.figure_player2_others_width, self.figure_player2_others_height = self.figure_player2_others_2.size
        self.figure_player2_others_new = pygame.transform.scale(surface=self.figure_player2_others, size=(self.figure_player2_others_width * self.settings.RATIO_ALL, self.figure_player2_others_height * self.settings.RATIO_ALL))
        self.figure_player2_others_new_rect = self.figure_player2_others_new.get_rect()
        self.screen.blit(self.figure_player2_others_new, self.surface_json['figure']['figure_player2_others'])



        #figure_player2_you
        self.figure_player2_you = pygame.image.load('main/images/figure_player2_you.png')
        self.figure_player2_you_2 = Image.open('main/images/figure_player2_you.png')
        self.figure_player2_you_width, self.figure_player2_you_height = self.figure_player2_you_2.size
        self.figure_player2_you_new = pygame.transform.scale(surface=self.figure_player2_you, size=(self.figure_player2_you_width * self.settings.RATIO_ALL, self.figure_player2_you_height * self.settings.RATIO_ALL))
        self.figure_player2_you_new_rect = self.figure_player2_you_new.get_rect()
        self.screen.blit(self.figure_player2_you_new, self.surface_json['figure']['figure_player2_you'])



        #figure_player3_others
        self.figure_player3_others = pygame.image.load('main/images/figure_player3_others.png')
        self.figure_player3_others_2 = Image.open('main/images/figure_player3_others.png')
        self.figure_player3_others_width, self.figure_player3_others_height = self.figure_player3_others_2.size
        self.figure_player3_others_new = pygame.transform.scale(surface=self.figure_player3_others, size=(self.figure_player3_others_width * self.settings.RATIO_ALL, self.figure_player3_others_height * self.settings.RATIO_ALL))
        self.figure_player3_others_new_rect = self.figure_player3_others_new.get_rect()
        self.screen.blit(self.figure_player3_others_new, self.surface_json['figure']['figure_player3_others'])



        #figure_player3_you
        self.figure_player3_you = pygame.image.load('main/images/figure_player3_you.png')
        self.figure_player3_you_2 = Image.open('main/images/figure_player3_you.png')
        self.figure_player3_you_width, self.figure_player3_you_height = self.figure_player3_you_2.size
        self.figure_player3_you_new = pygame.transform.scale(surface=self.figure_player3_you, size=(self.figure_player3_you_width * self.settings.RATIO_ALL, self.figure_player3_you_height * self.settings.RATIO_ALL))
        self.figure_player3_you_new_rect = self.figure_player3_you_new.get_rect()
        self.screen.blit(self.figure_player3_you_new, self.surface_json['figure']['figure_player3_you'])



        #figure_player4_others
        self.figure_player4_others = pygame.image.load('main/images/figure_player4_others.png')
        self.figure_player4_others_2 = Image.open('main/images/figure_player4_others.png')
        self.figure_player4_others_width, self.figure_player4_others_height = self.figure_player4_others_2.size
        self.figure_player4_others_new = pygame.transform.scale(surface=self.figure_player4_others, size=(self.figure_player4_others_width * self.settings.RATIO_ALL, self.figure_player4_others_height * self.settings.RATIO_ALL))
        self.figure_player4_others_new_rect = self.figure_player4_others_new.get_rect()
        self.screen.blit(self.figure_player4_others_new, self.surface_json['figure']['figure_player4_others'])



        #figure_player4_you
        self.figure_player4_you = pygame.image.load('main/images/figure_player4_you.png')
        self.figure_player4_you_2 = Image.open('main/images/figure_player4_you.png')
        self.figure_player4_you_width, self.figure_player4_you_height = self.figure_player4_you_2.size
        self.figure_player4_you_new = pygame.transform.scale(surface=self.figure_player4_you, size=(self.figure_player4_you_width * self.settings.RATIO_ALL, self.figure_player4_you_height * self.settings.RATIO_ALL))
        self.figure_player4_you_new_rect = self.figure_player4_you_new.get_rect()
        self.screen.blit(self.figure_player4_you_new, self.surface_json['figure']['figure_player4_you'])



        #label_hiding_all
        self.label_hiding_all = pygame.image.load('main/images/label_hiding_all.png')
        self.label_hiding_all_2 = Image.open('main/images/label_hiding_all.png')
        self.label_hiding_all_width, self.label_hiding_all_height = self.label_hiding_all_2.size
        self.label_hiding_all_new = pygame.transform.scale(surface=self.label_hiding_all, size=(self.label_hiding_all_width * self.settings.RATIO_ALL, self.label_hiding_all_height * self.settings.RATIO_ALL))
        self.label_hiding_all_new_rect = self.label_hiding_all_new.get_rect()
        self.screen.blit(self.label_hiding_all_new, self.surface_json['label']['label_hiding_all'])



        #label_trapped_all
        self.label_trapped_all = pygame.image.load('main/images/label_trapped_all.png')
        self.label_trapped_all_2 = Image.open('main/images/label_trapped_all.png')
        self.label_trapped_all_width, self.label_trapped_all_height = self.label_trapped_all_2.size
        self.label_trapped_all_new = pygame.transform.scale(surface=self.label_trapped_all, size=(self.label_trapped_all_width * self.settings.RATIO_ALL, self.label_trapped_all_height * self.settings.RATIO_ALL))
        self.label_trapped_all_new_rect = self.label_trapped_all_new.get_rect()
        self.screen.blit(self.label_trapped_all_new, self.surface_json['label']['label_trapped_all'])



        #label_turn_player1
        self.label_turn_player1 = pygame.image.load('main/images/label_turn_player1.png')
        self.label_turn_player1_2 = Image.open('main/images/label_turn_player1.png')
        self.label_turn_player1_width, self.label_turn_player1_height = self.label_turn_player1_2.size
        self.label_turn_player1_new = pygame.transform.scale(surface=self.label_turn_player1, size=(self.label_turn_player1_width * self.settings.RATIO_ALL, self.label_turn_player1_height * self.settings.RATIO_ALL))
        self.label_turn_player1_new_rect = self.label_turn_player1_new.get_rect()
        self.screen.blit(self.label_turn_player1_new, self.surface_json['label']['label_turn_player1'])



        #label_turn_player2
        self.label_turn_player2 = pygame.image.load('main/images/label_turn_player2.png')
        self.label_turn_player2_2 = Image.open('main/images/label_turn_player2.png')
        self.label_turn_player2_width, self.label_turn_player2_height = self.label_turn_player2_2.size
        self.label_turn_player2_new = pygame.transform.scale(surface=self.label_turn_player2, size=(self.label_turn_player2_width * self.settings.RATIO_ALL, self.label_turn_player2_height * self.settings.RATIO_ALL))
        self.label_turn_player2_new_rect = self.label_turn_player2_new.get_rect()
        self.screen.blit(self.label_turn_player2_new, self.surface_json['label']['label_turn_player2'])



        #label_turn_player3
        self.label_turn_player3 = pygame.image.load('main/images/label_turn_player3.png')
        self.label_turn_player3_2 = Image.open('main/images/label_turn_player3.png')
        self.label_turn_player3_width, self.label_turn_player3_height = self.label_turn_player3_2.size
        self.label_turn_player3_new = pygame.transform.scale(surface=self.label_turn_player3, size=(self.label_turn_player3_width * self.settings.RATIO_ALL, self.label_turn_player3_height * self.settings.RATIO_ALL))
        self.label_turn_player3_new_rect = self.label_turn_player3_new.get_rect()
        self.screen.blit(self.label_turn_player3_new, self.surface_json['label']['label_turn_player3'])



        #label_turn_player4
        self.label_turn_player4 = pygame.image.load('main/images/label_turn_player4.png')
        self.label_turn_player4_2 = Image.open('main/images/label_turn_player4.png')
        self.label_turn_player4_width, self.label_turn_player4_height = self.label_turn_player4_2.size
        self.label_turn_player4_new = pygame.transform.scale(surface=self.label_turn_player4, size=(self.label_turn_player4_width * self.settings.RATIO_ALL, self.label_turn_player4_height * self.settings.RATIO_ALL))
        self.label_turn_player4_new_rect = self.label_turn_player4_new.get_rect()
        self.screen.blit(self.label_turn_player4_new, self.surface_json['label']['label_turn_player4'])



        #lost_city
        self.lost_city = pygame.image.load('main/images/lost_city.png')
        self.lost_city_2 = Image.open('main/images/lost_city.png')
        self.lost_city_width, self.lost_city_height = self.lost_city_2.size
        self.lost_city_new = pygame.transform.scale(surface=self.lost_city, size=(self.lost_city_width * self.settings.RATIO_ALL, self.lost_city_height * self.settings.RATIO_ALL))
        self.lost_city_new_rect = self.lost_city_new.get_rect()
        self.screen.blit(self.lost_city_new, self.surface_json['lost']['lost_city'])



        #point_end
        self.point_end = pygame.image.load('main/images/point_end.png')
        self.point_end_2 = Image.open('main/images/point_end.png')
        self.point_end_width, self.point_end_height = self.point_end_2.size
        self.point_end_new = pygame.transform.scale(surface=self.point_end, size=(self.point_end_width * self.settings.RATIO_ALL, self.point_end_height * self.settings.RATIO_ALL))
        self.point_end_new_rect = self.point_end_new.get_rect()
        self.screen.blit(self.point_end_new, self.surface_json['point']['point_end'])



        #point_hide
        self.point_hide = pygame.image.load('main/images/point_hide.png')
        self.point_hide_2 = Image.open('main/images/point_hide.png')
        self.point_hide_width, self.point_hide_height = self.point_hide_2.size
        self.point_hide_new = pygame.transform.scale(surface=self.point_hide, size=(self.point_hide_width * self.settings.RATIO_ALL, self.point_hide_height * self.settings.RATIO_ALL))
        self.point_hide_new_rect = self.point_hide_new.get_rect()
        self.screen.blit(self.point_hide_new, self.surface_json['point']['point_hide'])



        #point_player1
        self.point_player1 = pygame.image.load('main/images/point_player1.png')
        self.point_player1_2 = Image.open('main/images/point_player1.png')
        self.point_player1_width, self.point_player1_height = self.point_player1_2.size
        self.point_player1_new = pygame.transform.scale(surface=self.point_player1, size=(self.point_player1_width * self.settings.RATIO_ALL, self.point_player1_height * self.settings.RATIO_ALL))
        self.point_player1_new_rect = self.point_player1_new.get_rect()
        self.screen.blit(self.point_player1_new, self.surface_json['point']['point_player1'])



        #point_player2
        self.point_player2 = pygame.image.load('main/images/point_player2.png')
        self.point_player2_2 = Image.open('main/images/point_player2.png')
        self.point_player2_width, self.point_player2_height = self.point_player2_2.size
        self.point_player2_new = pygame.transform.scale(surface=self.point_player2, size=(self.point_player2_width * self.settings.RATIO_ALL, self.point_player2_height * self.settings.RATIO_ALL))
        self.point_player2_new_rect = self.point_player2_new.get_rect()
        self.screen.blit(self.point_player2_new, self.surface_json['point']['point_player2'])



        #point_player3
        self.point_player3 = pygame.image.load('main/images/point_player3.png')
        self.point_player3_2 = Image.open('main/images/point_player3.png')
        self.point_player3_width, self.point_player3_height = self.point_player3_2.size
        self.point_player3_new = pygame.transform.scale(surface=self.point_player3, size=(self.point_player3_width * self.settings.RATIO_ALL, self.point_player3_height * self.settings.RATIO_ALL))
        self.point_player3_new_rect = self.point_player3_new.get_rect()
        self.screen.blit(self.point_player3_new, self.surface_json['point']['point_player3'])



        #point_player4
        self.point_player4 = pygame.image.load('main/images/point_player4.png')
        self.point_player4_2 = Image.open('main/images/point_player4.png')
        self.point_player4_width, self.point_player4_height = self.point_player4_2.size
        self.point_player4_new = pygame.transform.scale(surface=self.point_player4, size=(self.point_player4_width * self.settings.RATIO_ALL, self.point_player4_height * self.settings.RATIO_ALL))
        self.point_player4_new_rect = self.point_player4_new.get_rect()
        self.screen.blit(self.point_player4_new, self.surface_json['point']['point_player4'])



        #point_war
        self.point_war = pygame.image.load('main/images/point_war.png')
        self.point_war_2 = Image.open('main/images/point_war.png')
        self.point_war_width, self.point_war_height = self.point_war_2.size
        self.point_war_new = pygame.transform.scale(surface=self.point_war, size=(self.point_war_width * self.settings.RATIO_ALL, self.point_war_height * self.settings.RATIO_ALL))
        self.point_war_new_rect = self.point_war_new.get_rect()
        self.screen.blit(self.point_war_new, self.surface_json['point']['point_war'])



        #ticket_railway
        self.ticket_railway = pygame.image.load('main/images/ticket_railway.png')
        self.ticket_railway_2 = Image.open('main/images/ticket_railway.png')
        self.ticket_railway_width, self.ticket_railway_height = self.ticket_railway_2.size
        self.ticket_railway_new = pygame.transform.scale(surface=self.ticket_railway, size=(self.ticket_railway_width * self.settings.RATIO_ALL, self.ticket_railway_height * self.settings.RATIO_ALL))
        self.ticket_railway_new_rect = self.ticket_railway_new.get_rect()
        self.screen.blit(self.ticket_railway_new, self.surface_json['ticket']['ticket_railway'])



        #ticket_road
        self.ticket_road = pygame.image.load('main/images/ticket_road.png')
        self.ticket_road_2 = Image.open('main/images/ticket_road.png')
        self.ticket_road_width, self.ticket_road_height = self.ticket_road_2.size
        self.ticket_road_new = pygame.transform.scale(surface=self.ticket_road, size=(self.ticket_road_width * self.settings.RATIO_ALL, self.ticket_road_height * self.settings.RATIO_ALL))
        self.ticket_road_new_rect = self.ticket_road_new.get_rect()
        self.screen.blit(self.ticket_road_new, self.surface_json['ticket']['ticket_road'])



        #ticket_ship
        self.ticket_ship = pygame.image.load('main/images/ticket_ship.png')
        self.ticket_ship_2 = Image.open('main/images/ticket_ship.png')
        self.ticket_ship_width, self.ticket_ship_height = self.ticket_ship_2.size
        self.ticket_ship_new = pygame.transform.scale(surface=self.ticket_ship, size=(self.ticket_ship_width * self.settings.RATIO_ALL, self.ticket_ship_height * self.settings.RATIO_ALL))
        self.ticket_ship_new_rect = self.ticket_ship_new.get_rect()
        self.screen.blit(self.ticket_ship_new, self.surface_json['ticket']['ticket_ship'])



        #window_cover
        self.window_cover = pygame.image.load('main/images/window_cover.png')
        self.window_cover_2 = Image.open('main/images/window_cover.png')
        self.window_cover_width, self.window_cover_height = self.window_cover_2.size
        self.window_cover_new = pygame.transform.scale(surface=self.window_cover, size=(self.window_cover_width * self.settings.RATIO_ALL, self.window_cover_height * self.settings.RATIO_ALL))
        self.window_cover_new_rect = self.window_cover_new.get_rect()
        self.screen.blit(self.window_cover_new, self.surface_json['window']['window_cover'])



        #window_ending
        self.window_ending = pygame.image.load('main/images/window_ending.png')
        self.window_ending_2 = Image.open('main/images/window_ending.png')
        self.window_ending_width, self.window_ending_height = self.window_ending_2.size
        self.window_ending_new = pygame.transform.scale(surface=self.window_ending, size=(self.window_ending_width * self.settings.RATIO_ALL, self.window_ending_height * self.settings.RATIO_ALL))
        self.window_ending_new_rect = self.window_ending_new.get_rect()
        self.screen.blit(self.window_ending_new, self.surface_json['window']['window_ending'])



        #window_input
        self.window_input = pygame.image.load('main/images/window_input.png')
        self.window_input_2 = Image.open('main/images/window_input.png')
        self.window_input_width, self.window_input_height = self.window_input_2.size
        self.window_input_new = pygame.transform.scale(surface=self.window_input, size=(self.window_input_width * self.settings.RATIO_ALL, self.window_input_height * self.settings.RATIO_ALL))
        self.window_input_new_rect = self.window_input_new.get_rect()
        self.screen.blit(self.window_input_new, self.surface_json['window']['window_input'])



        #window_main
        self.window_main = pygame.image.load('main/images/window_main.png')
        self.window_main_2 = Image.open('main/images/window_main.png')
        self.window_main_width, self.window_main_height = self.window_main_2.size
        self.window_main_new = pygame.transform.scale(surface=self.window_main, size=(self.window_main_width * self.settings.RATIO_ALL, self.window_main_height * self.settings.RATIO_ALL))
        self.window_main_new_rect = self.window_main_new.get_rect()
        self.screen.blit(self.window_main_new, self.surface_json['window']['window_main'])



        #window_main_map
        self.window_main_map = pygame.image.load('main/images/window_main_map.png')
        self.window_main_map_2 = Image.open('main/images/window_main_map.png')
        self.window_main_map_width, self.window_main_map_height = self.window_main_map_2.size
        self.window_main_map_new = pygame.transform.scale(surface=self.window_main_map, size=(self.window_main_map_width * self.settings.RATIO_ALL, self.window_main_map_height * self.settings.RATIO_ALL))
        self.window_main_map_new_rect = self.window_main_map_new.get_rect()
        self.screen.blit(self.window_main_map_new, self.surface_json['window']['window_main_map'])



        #window_matching
        self.window_matching = pygame.image.load('main/images/window_matching.png')
        self.window_matching_2 = Image.open('main/images/window_matching.png')
        self.window_matching_width, self.window_matching_height = self.window_matching_2.size
        self.window_matching_new = pygame.transform.scale(surface=self.window_matching, size=(self.window_matching_width * self.settings.RATIO_ALL, self.window_matching_height * self.settings.RATIO_ALL))
        self.window_matching_new_rect = self.window_matching_new.get_rect()
        self.screen.blit(self.window_matching_new, self.surface_json['window']['window_matching'])



        #window_shop
        self.window_shop = pygame.image.load('main/images/window_shop.png')
        self.window_shop_2 = Image.open('main/images/window_shop.png')
        self.window_shop_width, self.window_shop_height = self.window_shop_2.size
        self.window_shop_new = pygame.transform.scale(surface=self.window_shop, size=(self.window_shop_width * self.settings.RATIO_ALL, self.window_shop_height * self.settings.RATIO_ALL))
        self.window_shop_new_rect = self.window_shop_new.get_rect()
        self.screen.blit(self.window_shop_new, self.surface_json['window']['window_shop'])



        #words_matching_1
        self.words_matching_1 = pygame.image.load('main/images/words_matching_1.png')
        self.words_matching_1_2 = Image.open('main/images/words_matching_1.png')
        self.words_matching_1_width, self.words_matching_1_height = self.words_matching_1_2.size
        self.words_matching_1_new = pygame.transform.scale(surface=self.words_matching_1, size=(self.words_matching_1_width * self.settings.RATIO_ALL, self.words_matching_1_height * self.settings.RATIO_ALL))
        self.words_matching_1_new_rect = self.words_matching_1_new.get_rect()
        self.screen.blit(self.words_matching_1_new, self.surface_json['words']['words_matching_1'])



        #words_matching_2
        self.words_matching_2 = pygame.image.load('main/images/words_matching_2.png')
        self.words_matching_2_2 = Image.open('main/images/words_matching_2.png')
        self.words_matching_2_width, self.words_matching_2_height = self.words_matching_2_2.size
        self.words_matching_2_new = pygame.transform.scale(surface=self.words_matching_2, size=(self.words_matching_2_width * self.settings.RATIO_ALL, self.words_matching_2_height * self.settings.RATIO_ALL))
        self.words_matching_2_new_rect = self.words_matching_2_new.get_rect()
        self.screen.blit(self.words_matching_2_new, self.surface_json['words']['words_matching_2'])



        #words_matching_3
        self.words_matching_3 = pygame.image.load('main/images/words_matching_3.png')
        self.words_matching_3_2 = Image.open('main/images/words_matching_3.png')
        self.words_matching_3_width, self.words_matching_3_height = self.words_matching_3_2.size
        self.words_matching_3_new = pygame.transform.scale(surface=self.words_matching_3, size=(self.words_matching_3_width * self.settings.RATIO_ALL, self.words_matching_3_height * self.settings.RATIO_ALL))
        self.words_matching_3_new_rect = self.words_matching_3_new.get_rect()
        self.screen.blit(self.words_matching_3_new, self.surface_json['words']['words_matching_3'])



        #words_please_wait_1
        self.words_please_wait_1 = pygame.image.load('main/images/words_please_wait_1.png')
        self.words_please_wait_1_2 = Image.open('main/images/words_please_wait_1.png')
        self.words_please_wait_1_width, self.words_please_wait_1_height = self.words_please_wait_1_2.size
        self.words_please_wait_1_new = pygame.transform.scale(surface=self.words_please_wait_1, size=(self.words_please_wait_1_width * self.settings.RATIO_ALL, self.words_please_wait_1_height * self.settings.RATIO_ALL))
        self.words_please_wait_1_new_rect = self.words_please_wait_1_new.get_rect()
        self.screen.blit(self.words_please_wait_1_new, self.surface_json['words']['words_please_wait_1'])



        #words_please_wait_2
        self.words_please_wait_2 = pygame.image.load('main/images/words_please_wait_2.png')
        self.words_please_wait_2_2 = Image.open('main/images/words_please_wait_2.png')
        self.words_please_wait_2_width, self.words_please_wait_2_height = self.words_please_wait_2_2.size
        self.words_please_wait_2_new = pygame.transform.scale(surface=self.words_please_wait_2, size=(self.words_please_wait_2_width * self.settings.RATIO_ALL, self.words_please_wait_2_height * self.settings.RATIO_ALL))
        self.words_please_wait_2_new_rect = self.words_please_wait_2_new.get_rect()
        self.screen.blit(self.words_please_wait_2_new, self.surface_json['words']['words_please_wait_2'])



        #words_please_wait_3
        self.words_please_wait_3 = pygame.image.load('main/images/words_please_wait_3.png')
        self.words_please_wait_3_2 = Image.open('main/images/words_please_wait_3.png')
        self.words_please_wait_3_width, self.words_please_wait_3_height = self.words_please_wait_3_2.size
        self.words_please_wait_3_new = pygame.transform.scale(surface=self.words_please_wait_3, size=(self.words_please_wait_3_width * self.settings.RATIO_ALL, self.words_please_wait_3_height * self.settings.RATIO_ALL))
        self.words_please_wait_3_new_rect = self.words_please_wait_3_new.get_rect()
        self.screen.blit(self.words_please_wait_3_new, self.surface_json['words']['words_please_wait_3'])

#绘制原图
    def _blit_events(self):
        if self.game_active_1:
            """封面"""      
            self.screen.blit(self.window_cover_new,(0,0))           
            self.screen.blit(self.words_please_wait_1_new,self.surface_json['words']['words_please_wait_1'])

        if self.game_active_2:
            """进入界面"""
            pass
 
        if self.game_active_3:
            """成员等待界面"""
            pass


        if self.game_active_4:
            """房间界面"""
            pass

        if self.game_active_5:
            """大战界面"""
            pass

        if self.game_active_6:
            """商店界面"""
            pass

        if self.game_active_7:
            """结算界面"""
            pass
#点击按钮，切换界面
    def _check_button(self):       
        if self.window_cover_new_rect.collidepoint(self.mouse_click_pos):
            self.game_active_1 = False
            self.game_active_2 = True

        if self.button_Muti_player_static_new_rect.collidepoint(self.mouse_click_pos):
            self.game_active_2 = False
            self.game_active_3 = True
#绘制变亮的按钮
    def _blit_hightlight(self):
        if self.highlight_active_1:
            pass
        if self.highlight_active_2:
            pass
        if self.highlight_active_3:
            pass
        if self.highlight_active_4:
            pass
        if self.highlight_active_5:
            pass
        if self.highlight_active_6:
            pass
#鼠标移动到按钮上
    def _highlight_button(self):
        if self.button_Muti_player_static_new_rect.collidepoint(self.mouse_pos):
            self.highlight_active_1 = True         



#定义服务器名称
HOST = '0.0.0.0'
PORT = 400
BUFSIZE = 1024
ADDR = (HOST,PORT)

#定义服务器属性
tcpsersock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsersock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpsersock.bind(ADDR)
tcpsersock.listen(1)
inputs=[tcpsersock]
print(inputs)
if __name__ == '__main__':
    #创建游戏实例并运行游戏
    lc = LostCity()
    lc.run_game()
