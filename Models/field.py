# Playing field (#5)
# Field class: draws the background and the 3 walls
# the ball bounces off (top, bottom, and the far side).
import pygame
isSinglePlayer = False

class GameField:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect, 10)
        pygame.draw.line(surface, (120, 120, 120), (0, 0), (0,720), 20)
        pygame.draw.line(surface, (0, 128, 0), (1280, 0), (1280,720), 20)
        pygame.draw.line(surface, (220, 220, 220), (640, 40), (640 ,100), 2)
        pygame.draw.line(surface, (220, 220, 220), (640, 140), (640 ,220), 2)
        pygame.draw.line(surface, (220, 220, 220), (640, 260), (640 ,340), 2)
        pygame.draw.line(surface, (220, 220, 220), (640, 380), (640 ,460), 2)
        pygame.draw.line(surface, (220, 220, 220), (640, 500), (640 ,580), 2)
        pygame.draw.line(surface, (220, 220, 220), (640, 620), (640 ,680), 2)

    
    def check_goal(self, ball):
        
        """Return "left" or "right" if the ball crossed that border, else None."""
        if ball.x - ball.radius <= self.rect.left:
            return "left"
        
        if ball.x + ball.radius >= self.rect.right and not isSinglePlayer:
            return "right"
        return None
    