# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.

import pygame
from Models.ball import ball
from Models.collision import Collision
from Models.paddle import Paddle
from Models.field import GameField
from Models.menu import Menu
from Shared.settings import WIDTH, HEIGHT, FPS, BG_COLOR, PADDLE_SIZES, PADDLE_SPEED, PADDLE_COLOR

print(GameField.__module__)
print(GameField.__init__)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
game_ball = ball()
player_paddles = Paddle.init_x_mirrored_paddles(30, PADDLE_SIZES["m"], PADDLE_SPEED["medium"], 40, 40, False, (HEIGHT//2), PADDLE_COLOR)
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
    Collision.collision_detection(game_ball, player_paddles)
    Collision.wall_collision_detection(game_ball, game_field)
    Collision.third_wall_collision_detection(game_ball, game_field)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BG_COLOR)
    game_field.draw(screen)
    goal_side = game_field.check_goal(game_ball)
    if goal_side is not None:
        game_ball.reset(goal_side)
    game_ball.ball_movement()
    game_ball.draw(screen)

    for paddle in player_paddles.values():
        paddle.update_and_draw(pygame.key.get_pressed(), screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


