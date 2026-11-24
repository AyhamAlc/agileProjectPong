# Single-player mode (#7)
# Game class: main game loop (handle input, update, draw).
# Creates the field, ball and paddle and connects them.
import pygame

class Collision:

    def collision_detection(ball, paddles):
        """
        Check for collision between the ball and the paddle.
        If a collision is detected, reverse the ball's direction.
        """
        ball_rect = pygame.Rect(
            ball.x - ball.radius,
            ball.y - ball.radius,
            ball.radius * 2,
            ball.radius * 2,
        )
        for paddle in paddles.values():
            if paddle.rect.colliderect(ball_rect):
                ball.direction = (180- ball.direction) % 360  # Reverse the ball's horizontal direction
                offset = (ball.y - paddle.rect.centery) / (paddle.rect.height / 2)
                ball.direction += offset * 45  # Adjust the angle based on where it hit the
                # Ensure the ball's direction is within 0-360 degrees
                ball.direction = ball.direction % 360


    def wall_collision_detection(ball, field):
        """
        Check for collision between the ball and the top/bottom walls of the field.
        If a collision is detected, reverse the ball's vertical direction.
        """
        if ball.y - ball.radius <= field.rect.top or ball.y + ball.radius >= field.rect.bottom:
            ball.direction = (360 - ball.direction) % 360  # Reverse the ball's vertical direction

    def third_wall_collision_detection(ball, field):
        """
        Check for collision between the ball and the third wall (the far side) of the field.
        If a collision is detected, reverse the ball's horizontal direction.
        """
        if ball.x - ball.radius <= field.rect.left or ball.x + ball.radius >= field.rect.right:
            ball.direction = (180 - ball.direction) % 360  # Reverse the ball's horizontal direction