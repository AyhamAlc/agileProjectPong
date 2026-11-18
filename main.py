# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.

import pygame
from settings import WIDTH, HEIGHT, FPS, BG_COLOR

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
running = True
dt = 0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    

    screen.fill(BG_COLOR)
   
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()