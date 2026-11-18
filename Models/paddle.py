import pygame
import math
class Paddle:
    """
    Keyboard controlled paddle
    """
    def __init__(self, width: int, height: int, speed: int, left:int, top:int):
        """
        Create a paddle at (left, top) coordinates

        Args:
            width: Paddle width in pixels
            height: Paddle height in pixels
            speed: Distance to move per update, in pixels
            left: initial x-coordinate of paddle left edge
            top: initial y-coordinate of paddle top edge
        """
        self.width = width
        self.height = height
        self.speed = speed
        self.initial_xy = (left, top)
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the paddle on given surface
        """
        pygame.draw.rect(surface, color=(255, 255, 255), rect=self.rect)

    def update(self, keys: pygame.key.ScancodeWrapper, field_rect: pygame.Rect) -> None:
        """
        Update paddle position according to key's pressed.

        W and Up: paddle moves up, y value decreases

        S and Down: paddle moves down, y value increases

        Args:
            keys: pygame.key.get_pressed()
            field_rect: use current screen Rect
        """
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self._move(-self.speed)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self._move(self.speed)

        self.rect.clamp_ip(field_rect)#Limits paddle movement within field_rect


    def _move(self, amount: float) -> None:
        """
        Internal helper func
        Move vertically by amount of pixels;
        Positive values gives downward movement, 
        negative values give upward movement

        Args:
            amount: float, movement in pixels, rounded to int and added to rect.y
        """
        if amount > 0:
            self.rect.y += math.ceil(amount)
        elif amount < 0:
            self.rect.y += math.floor(amount)

    def reset(self) -> None:
        """
        Resets paddle to initial position
        """
        self.rect.topleft = self.initial_xy