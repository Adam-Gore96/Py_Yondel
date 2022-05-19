
import pygame

from pygame.mixer import Sound
from Game import mainGame
import pygame_textimport


pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

background = pygame.image.load('wallpapersden.com_castle-artwork_720x1280.png')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
gray = (128, 128, 128)
button_color_light = (170, 170, 170)
button_color_dark = (100, 100, 100)

x1 = 720
y1 = 720

res = (x1, y1)
title_screen = pygame.display.set_mode(res)

width = title_screen.get_width()

height = title_screen.get_height()

pygame.display.set_caption("Yondel Game")

smallfont = pygame.font.SysFont('Corbel', 35)

new_game_text = smallfont.render('New', True, white)
login_game_text = smallfont.render('Login', True, white)
Gamestart = mainGame
mOn = True

background_music = Sound("YongelTheme.wav")
background_music_channel = pygame.mixer.Channel(1)

FPS = 60
username_text = ''
password_text = ''

input_rect1 = pygame.Rect(100, 200, 140, 32)
input_rect2 = pygame.Rect(480, 200, 140, 32)

clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)

# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

def music_on(check: int):

    if check == 1 and not background_music_channel.get_busy():
        background_music_channel.play(background_music)
    if check == 0:
        background_music_channel.stop()


def draw_window(screen_name: str):

    if screen_name == "title":
        music_on(1)
        title_screen.blit(background, (0, 0))

        pygame.draw.rect(title_screen, button_color_dark, [width / 2, height / 2, 140, 40])

        pygame.draw.rect(title_screen, button_color_dark, [width / 4, height / 2, 140, 40])

        title_screen.blit(login_game_text, (width / 2, height / 2))
        title_screen.blit(new_game_text, (width / 4, height / 2))
        pygame.display.update()

    elif screen_name == "login":
        # print(screen_name)
        music_on(0)
        pygame.display.set_mode(res).fill(black)
        title_screen.fill(black)

        if active:
            color = color_active
        else:
            color = color_passive


        pygame.draw.rect(title_screen, color, input_rect1)
        pygame.draw.rect(title_screen, color, input_rect2)

        text_surface = base_font.render(username_text, True, (255, 255, 255))
        title_screen.blit(text_surface, (input_rect1.x+5, input_rect1.y+5))

        text_surface2 = base_font.render(password_text, True, (255, 255, 255))
        title_screen.blit(text_surface2, (input_rect2.x+5, input_rect2.y+5))

        # input_rect1.w = max(100, text_surface.get_width()+10)
        # input_rect2.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()


    elif screen_name == "register":
        # print(screen_name)
        music_on(0)
        pygame.display.set_mode(res).fill(black)
        pygame.display.update()


def main():
    working = True
    global username_text, password_text
    run = True
    currentScreen = "title"
    while run:

        for ev in pygame.event.get():
            draw_window(currentScreen)

            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False

            # checks if a mouse is clicked

            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the

                # button the game is terminated

                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    currentScreen = "login"
                    clock.tick(60)
                    # Gamestart.Games.log   in("saved")

                elif width/4 <= mouse[0] <= width/4+140 and height/2 <= mouse[1] <= height/2+40:
                    currentScreen = "register"
                    draw_window(currentScreen)
                    # Gamestart.Games.login("new")

            if ev.type == pygame.KEYDOWN:

                # Check for backspacet
                if ev.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    username_text = username_text[:-1]

                # Unicode standard is used for string
                # formation
                elif ev.key == pygame.K_TAB:
                    password_text = password_text[:-1]
                else:
                    username_text += ev.unicode

                if ev.key == pygame.K_RETURN:
                    print(f"Username {username_text}")
                    print(f"Password {password_text}")


        mouse = pygame.mouse.get_pos()
        pygame.display.update()

    pygame.quit()




main()
