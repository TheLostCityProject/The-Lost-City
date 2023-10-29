import pyautogui
import pygame,sys
width_player_screen,height_player_screen = (pyautogui.size())
ratio_playerscreen = width_player_screen/height_player_screen
ratio_mapcreen = 2300/1350

if(ratio_playerscreen > ratio_mapcreen):                      # define the width and height of the window of the game
    height_game_screen = height_player_screen
    width_game_screen = ratio_mapcreen * height_game_screen
    width_game_screen -= 80*ratio_mapcreen
    height_game_screen -= 80
else:
    width_game_screen = width_player_screen
    height_game_screen = width_game_screen / ratio_mapcreen

print(height_player_screen)
print(width_player_screen)
print(height_game_screen)
print(width_game_screen)
print(ratio_playerscreen)
print(ratio_mapcreen)

while True:
    pygame.init()
    icon = pygame.image.load("My_solution\image\lost_city.png")                     # initialize the screen
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((width_game_screen,height_game_screen))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            

