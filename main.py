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
from Models.game import LiveScoreBoard
from Models.game import speed_modifier
import Models.field
from Models.game_over import GameOverScreen
print(GameField.__module__)
print(GameField.__init__)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
game_ball = ball()
speed_control = speed_modifier()
player_paddles = Paddle.init_x_mirrored_paddles(30, PADDLE_SIZES["m"], PADDLE_SPEED["medium"], 40, 40, False, (HEIGHT//2), PADDLE_COLOR)
game_field = GameField(0, 0, WIDTH, HEIGHT)
running = True
dt = 0       
scoreboard = LiveScoreBoard(screen.get_width() // 2, 50, (0, 128, 255), (255, 80, 80), single_player=Models.field.isSinglePlayer)

#gameover state 
game_over_active = False #check if game is paused and game over screen is active
game_over_ui = None
last_goal_side = None #for resetting the ball after game over, to know which side scored last

# start menu
menu = Menu(0, 0, WIDTH, HEIGHT, BG_COLOR)
choice = menu.run(screen)
if choice == "quit":
    pygame.quit()
    raise SystemExit
clock.tick()

while running:
   
    Collision.collision_detection(game_ball, player_paddles)
    Collision.wall_collision_detection(game_ball, game_field)
    Collision.third_wall_collision_detection(game_ball, game_field)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if the game is over, handle the game over screen events
        if game_over_active and game_over_ui:
            action = game_over_ui.handle_events(event)
            if action == "replay":
                game_over_active = False
                game_over_ui = None
                #when replaying, reset the ball to the last goal side so that the player who lost gets to serve
                scoreboard.reset()
                game_ball.reset(last_goal_side)

                for paddle in player_paddles.values():
                    paddle.reset()
            elif action == "menu":
                #TODO: implement a way to go back to the main menu without quitting the game
                running = False
            elif action == "quit":
                running = False

    # If GAME over is not active, check for goals and update the game state
    if not game_over_active:
        #check if goal is scored, if so, set game_over_active to True and create a GameOverScreen instance
        goal_side = game_field.check_goal(game_ball)

        if goal_side is not None:
            scoreboard.add_point(goal_side)
            last_goal_side = goal_side

            for paddle in player_paddles.values():
                paddle.reset()

            game_over_active = True
            winner_name = "Player 1" if goal_side == "right" else "Player 2"
            game_over_ui = GameOverScreen(screen, winner_name)
        game_ball.ball_movement()
        scoreboard.update(dt)

        """ball and paddle speed increment with time intervals"""
        increment = speed_control.ball_speed_increment_with_time_intervals(dt)
        if increment > 0:
            game_ball.increase_speed(increment)

        for paddle in player_paddles.values():
            paddle.increase_speed(increment)
      
    screen.fill(BG_COLOR)
    game_field.draw(screen)
    game_ball.draw(screen)
    for paddle in player_paddles.values():
        paddle.update_and_draw(pygame.key.get_pressed(), screen)

    scoreboard.draw(screen)

    #if game over is active, draw the game over screen on top of the game
    if game_over_active and game_over_ui:
        game_over_ui.draw()
        
    pygame.display.flip()
    dt = clock.tick(FPS)
    
pygame.quit()
