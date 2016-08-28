import random

import pygame
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screenSizeX = 800
screenSizeY = 600

pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((screenSizeX, screenSizeY))
pygame.display.set_caption("Snake")

font = pygame.font.SysFont(None, 30)


def snake(snake_size):
    for XnY in snake_size:
        pygame.draw.rect(gameDisplay, red, [XnY[0], XnY[1], 10, 10])
    del snake_size[-1]


def message_to_screen(mgs, color, display_time):
    screen_text = font.render(mgs, True, color)
    gameDisplay.blit(screen_text, [screenSizeX / 2, screenSizeY / 2])
    pygame.display.update()
    time.sleep(display_time)
    screen_text = font.render(mgs, True, white)
    gameDisplay.blit(screen_text, [screenSizeX / 2, screenSizeY / 2])
    pygame.display.update()


def game_loop():
    gameExit = False
    lead_x = screenSizeX / 2
    lead_y = screenSizeY / 2
    appleX = round(random.randrange(0, screenSizeX / 10)) * 10
    appleY = round(random.randrange(0, screenSizeY / 10)) * 10
    lead_x_change = 0
    lead_y_change = 0
    snake_size = []

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x >= screenSizeX or lead_x < 0 or lead_y >= screenSizeY or lead_y < 0:
            message_to_screen("you loose !!", red, 2)
            message_to_screen("Would you like to try again ? press y/n", black, 5)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        return False
                    else:
                        return True
                gameExit = True

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, black, [appleX, appleY, 10, 10])
        snake_size.insert(0, [lead_x, lead_y])
        snake(snake_size)
        pygame.display.update()
        clock.tick(10)
        if appleX == lead_x and appleY == lead_y:
            appleX = round(random.randrange(0, screenSizeX / 10)) * 10
            appleY = round(random.randrange(0, screenSizeY / 10)) * 10
            snake_size.insert(0, [lead_x, lead_y])

    pygame.quit()
    quit()


gameQuit = False
while not gameQuit:
    gameQuit = game_loop()
