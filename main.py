# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.

import pygame
from Models.ball import ball
from Models.field import GameField

print(GameField.__module__)
print(GameField.__init__)

from Shared.settings import WIDTH, HEIGHT, FPS, BG_COLOR 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
game_ball = ball()
game_field = GameField(0, 0, WIDTH, HEIGHT)
running = True
dt = 0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BG_COLOR)
    game_field.draw(screen)
    goal_side = game_field.check_goal(game_ball)
    if goal_side is not None:
        running = False
    game_ball.ball_movement()
    game_ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


