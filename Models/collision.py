import pygame
import Models.field

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
                offset = (ball.y - paddle.rect.centery) / (paddle.rect.height / 2)

                # Make sure the ball is moving towards the paddle before changing its direction, preventing the ball from getting stuck inside the paddle (AKA bounce towards the paddle)
                if 90 < ball.direction < 270:
                    ball.x = paddle.rect.right + ball.radius
                    new_dir = (180 - ball.direction) + offset * 45
                    # Normalize to [-180, 180] and clamp to [-75, 75] so it always goes right
                    new_dir = (new_dir + 180) % 360 - 180
                    ball.direction = max(-75, min(75, new_dir)) % 360
                    
                    ball.increase_speed()

                # Right paddle (ball was moving right: direction < 90 or > 270)
                elif ball.direction < 90 or ball.direction > 270:
                    ball.x = paddle.rect.left - ball.radius
                    new_dir = (180 - ball.direction) + offset * 45
                    # Clamp to [105, 255] so it always goes left
                    new_dir = new_dir % 360
                    ball.direction = max(105, min(255, new_dir))
                    
                    ball.increase_speed()


    def wall_collision_detection(ball, field):
        """
        Check for collision between the ball and the top/bottom walls of the field.
        If a collision is detected, reverse the ball's vertical direction.
        """
        if ball.y - ball.radius <= field.rect.top or ball.y + ball.radius >= field.rect.bottom:
            ball.direction = (360 - ball.direction) % 360  # Reverse the ball's vertical direction
            
            ball.increase_speed()

    def third_wall_collision_detection(ball, field):
        """
        Check for collision between the ball and the third wall (the far side) of the field.
        If a collision is detected, reverse the ball's horizontal direction.
        """
        if ball.x - ball.radius <= field.rect.left or ball.x + ball.radius >= field.rect.right and Models.field.isSinglePlayer:
            ball.direction = (180 - ball.direction) % 360  # Reverse the ball's horizontal direction
            
            ball.increase_speed()