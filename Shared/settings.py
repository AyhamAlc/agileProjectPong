# Shared constants used by all files:
# screen size, colours, FPS, paddle/ball sizes and speeds.
import pygame
import pygame.color

WIDTH = 1280
HEIGHT =  720
FPS = 60
BG_COLOR = "black"

"""ball properties"""

X_CORD_CIRCLE = 640
Y_CORD_CIRCLE = 360
RADIUS = 12
BALL_COLOR = (255, 0 , 0)
BALL_INITIAL_SPEED = 7
BALL_SPEED_INCREMENT = 0.5
BALL_MAX_SPEED = 25

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

# colors used in the game_over button and the start menu button are not included in this dictionary
#Surface & Background 
COLORS.update({
    "bg_color": pygame.Color("#0B1020"), #window background color
    "card_bg": pygame.Color("#131C2F"), #dialog card background color
    "card_border": pygame.Color("#26344E"), #dialog card border color
    # primary action
    "mint": pygame.Color("#5EF2D0"), 
    "mint_hover": pygame.Color("#7DF8DE"),
    # secondary action
    "btc_sec": pygame.Color("#1D2A44"),#muted button (main menu, quit)
    "btc_hover": pygame.Color("#293A5C"), #secondary button hover state
    "btc_border": pygame.Color("#2D3E5F"), #secondary button border color
    # text colors
    "text_light": pygame.Color("#F5F7FF"), #primary text color with high contrast
    "text_dark": pygame.Color("#0B1020"), #contrast text color for bright buttons
    "text_muted": pygame.Color("#A1AEC7"), #muted text color for subtitles and prompt text
    #player 2
    "player2": pygame.Color("#9D8CFF"), #Soft lilac for P2 paddle & badges
})