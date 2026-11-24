# Shared constants used by all files:
# screen size, colours, FPS, paddle/ball sizes and speeds.
import pygame

WIDTH = 1280
HEIGHT =  720
FPS = 60
BG_COLOR = "black"

"""ball properties"""

X_CORD_CIRCLE = 640
Y_CORD_CIRCLE = 360
RADIUS = 12
BALL_COLOR = (255, 0 , 0)
SPEED = 15

"""Dictionary of all colors provided by pygame Color"""
"""Key is the Name entry on this table: https://www.pygame.org/docs/ref/color_list.html"""
COLORS = {
    name: pygame.Color(value)
    for name, value in pygame.color.THECOLORS.items()
}

"""Paddle properties"""
PADDLE_COLOR = COLORS["white"]
PADDLE_SIZES = {"l": HEIGHT // 2, "m": HEIGHT // 4, "s": HEIGHT // 6}
PADDLE_SPEED = {"fast": 20, "medium": 10, "slow": 5}
