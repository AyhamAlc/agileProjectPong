# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.

import pygame
from Models.ball import ball
from Models.game import Collision
from Models.paddle import Paddle
from Models.field import GameField
from Models.menu import Menu

print(GameField.__module__)
print(GameField.__init__)

from Shared.settings import WIDTH, HEIGHT, FPS, BG_COLOR 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
game_ball = ball()
player_paddle  = Paddle(20, 80, 10, 40, True)
game_field = GameField(0, 0, WIDTH, HEIGHT)
running = True
dt = 0

# start menu
menu = Menu(0, 0, WIDTH, HEIGHT, BG_COLOR)
choice = menu.run(screen)
if choice == "quit":
    pygame.quit()
    raise SystemExit

while running:
    Collision.collision_detection(game_ball, player_paddle)
    Collision.wall_collision_detection(game_ball, game_field)
    Collision.third_wall_collision_detection(game_ball, game_field)
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

    player_paddle.update(pygame.key.get_pressed(), screen.get_rect())
    player_paddle.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


