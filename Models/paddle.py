import pygame
import math
from Shared.settings import WIDTH, PADDLE_MAX_SPEED, PADDLE_SPEED_INCREMENT
class Paddle:
    """
    Keyboard controlled paddle
    """
    def __init__(
            self, 
            width: int, 
            height: int, 
            speed: int, 
            left:int, 
            top:int, 
            is_wasd: bool, 
            center_y: int,
            color: pygame.Color):
        """
        Create a paddle at (left, top) coordinates centered on the y-axis

        Args:
            width: Paddle width in pixels
            height: Paddle height in pixels
            speed: Distance to move per update, in pixels
            left: initial x-coordinate of paddle left edge
            top: initial y-coorindate of paddle top edge
            is_wasd: boolean to set controlls as W and S or UP and DOWN
            center_y: starting position of the paddle center on the y axis
            color: the color of the paddle
        """
        self.width = width
        self.height = height
        self.initial_speed = speed
        self.current_speed = speed
        self.max_speed = PADDLE_MAX_SPEED
        self.speed = speed
        self.rect = pygame.Rect(left, top, width, height)
        self.rect.centery = center_y
        self.initial_topleft = self.rect.topleft
        self.color = color
        if is_wasd:
            self.key_up = pygame.K_w
            self.key_down = pygame.K_s
        else:
            self.key_up = pygame.K_UP
            self.key_down = pygame.K_DOWN
    

    def init_x_mirrored_paddles(
            width: int, 
            height: int, 
            speed: int, 
            left:int, 
            top:int, 
            left_is_wasd: bool, 
            center_y: int,
            color: pygame.Color) -> dict[str, Paddle]:
        """
        Create a dictionary of 2 paddles mirrored and centered on the y-axis

        Keys: "left", "right"

        Args:
            width: Paddle width in pixels
            height: Paddle height in pixels
            speed: Paddle distance to move per update, in pixels
            left: Left paddle initial x-coordinate of paddle left edge, right paddle mirrors in y-axis
            top: initial y-coorindate of noth paddle's top edge
            left_is_wasd: boolean to set controlls, true: left paddle W and S, right paddle UP and DOWN
            center_y: starting position of both paddle's center on the y axis
            color: the color of the paddle's
        """
        left_paddle = Paddle(width, height, speed, left, top, left_is_wasd, center_y, color)
        right_paddle = Paddle(width, height, speed, (WIDTH -(left + width)), top, not left_is_wasd, center_y, color)

        return {"left": left_paddle, "right": right_paddle}

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the paddle on given surface
        """
        pygame.draw.rect(surface, self.color, self.rect)

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

        self._move(self.current_speed * direction)

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

    def increase_speed(self, increment):
        self.current_speed = min(
            self.current_speed + increment,
            self.max_speed)
            
    def reset(self):
        self.rect.topleft = self.initial_topleft
        self.current_speed = self.initial_speed # Reset speed to initial speed

    def update_and_draw(self, keys: pygame.key.ScancodeWrapper, field_rect: pygame.Rect) -> None:
        """
        Update paddle position according to key's pressed and draw on given surface.

        W and Up: paddle moves up, y value decreases

        S and Down: paddle moves down, y value increases

        Args:
            keys: pygame.key.get_pressed()
            field_rect: use current screen Rect
        """
        self.update(keys, field_rect.get_rect())
        self.draw(field_rect)