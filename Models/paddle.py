import pygame
import math
from Shared.settings import HEIGHT
class Paddle:
    """
    Keyboard controlled paddle
    """
    def __init__(self, width: int, height: int, speed: int, left:int, is_wasd: bool):
        """
        Create a paddle at (left, top) coordinates centered on the y-axis

        Args:
            width: Paddle width in pixels
            height: Paddle height in pixels
            speed: Distance to move per update, in pixels
            left: initial x-coordinate of paddle left edge
            is_wasd: boolean to set controlls as W and S or UP and DOWN
        """
        CENTER_Y = HEIGHT // 2
        self.width = width
        self.height = height
        self.speed = speed
        self.initial_topleft = (left, CENTER_Y)
        self.rect = pygame.Rect(left, CENTER_Y, width, height)
        if is_wasd:
            self.key_up = pygame.K_w
            self.key_down = pygame.K_s
        else:
            self.key_up = pygame.K_UP
            self.key_down = pygame.K_DOWN

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
        direction = self._get_direction(keys)

        self._move(self.speed * direction)

        self.rect.clamp_ip(field_rect)#Limits paddle movement within field_rect

    def _get_direction(self, keys:pygame.key.ScancodeWrapper) -> int:
        """
        Internal helper func for update()
        Returns the direction of pressed keys

        Args:
            keys: the same keys arg as in update()
        Returns:
            int: An integer representing the direction of input, 1 for down, -1 for up, 0 for no/dual input
        """
        key_up = keys[self.key_up]
        key_down = keys[self.key_down]
        return int(key_down) - int(key_up)


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
        self.rect.topleft = self.initial_topleft