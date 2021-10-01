import pygame
from Game import *

pygame.init()
pygame.font.init()


def init_screen():
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    done = False

    font = pygame.font.Font(r"C:\Users\mistr\OneDrive\Documents\GitHub\Turnbased_RPG\Turnbased_RPG\EightBitDragon-anqx.ttf", 50)
    text = font.render("Hello, World", True, (255, 255, 255))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        screen.fill((0, 0, 0))
        screen.blit(text, (490, 300))

        pygame.display.flip()
        clock.tick(60)


# First Intro Game Title (ASCII)
init_screen()
# Ask user to start new or load game
slow_print("Hello there adventurer, would you like to start a new game or load a current save?")

# Add help option/command that gives the user info on the different stats and how they work

