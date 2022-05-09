import pygame
import sys


import Game.mainGame
from Game import mainGame


class Screen:

    global mouse
    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)

    button_color_light = (170, 170, 170)
    button_color_dark = (100, 100, 100)

    x1 = 720
    y1 = 720

    res = (x1, y1)
    screen = pygame.display.set_mode(res)

    width = screen.get_width()

    height = screen.get_height()

    pygame.display.set_caption("Yondel Game")

    smallfont = pygame.font.SysFont('Corbel', 35)

    new_game_text = smallfont.render('New', True, white)
    login_game_text = smallfont.render('Login', True, white)

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked

            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the

                # button the game is terminated

                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    Gamestart = mainGame
                    Gamestart.Games.login("new")

         # fills the screen with a color

        screen.fill(black)

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,button_color_light,[width/2,height/2,140,40])

        else:
            pygame.draw.rect(screen,button_color_dark,[width/2,height/2,140,40])

            screen.blit(login_game_text, (width/2, height/2))

            # superimposing the text onto our button

        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,button_color_light,[width/2,height/2,140,40])

        else:
            pygame.draw.rect(screen,button_color_dark,[width/2,height/2,140,40])

            screen.blit(new_game_text, (width/2+40, height/2 +5))

        pygame.display.update()

