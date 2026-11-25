import pygame
import math
from Shared.settings import X_CORD_CIRCLE, Y_CORD_CIRCLE, RADIUS, BALL_COLOR , SPEED

class ball:

    def __init__(self):
        self.x = float(X_CORD_CIRCLE)
        self.y = float(Y_CORD_CIRCLE)
        self.radius = RADIUS
        self.color = BALL_COLOR
        self.speed = SPEED
        self.direction = 180  # Default direction in degrees (0 is to the right)



    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


    def ball_movement(self):
        """
        Move the ball at its configured speed in the given direction.

        Args:
            direction: Angle in degrees, where 0 is to the right and 90 is down
        """
        rad = math.radians(self.direction)

        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

    def choose_ball_direction(self, goal_side):
                if goal_side == "left":
                    return 180
                else:
                    return 0


    def reset(self, goal_side):
        self.x = float(X_CORD_CIRCLE)
        self.y = float(Y_CORD_CIRCLE)
        if goal_side is None:
            self.direction = 180 
        else:
            self.direction = self.choose_ball_direction(goal_side)

