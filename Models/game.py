# Single-player mode (#7)
# Game class: main game loop (handle input, update, draw).
# Creates the field, ball and paddle and connects them.
import pygame

class LiveScoreBoard:

    def __init__(self, x, y, left_color, right_color, font_size=72, single_player=False):
        self.left = 0
        self.right = 0
        self.x = x
        self.y = y
        self.left_color = left_color
        self.right_color = right_color
        self.font = pygame.font.Font(None,font_size)
        self.past_ms = 0
        self.single_player = single_player

    def update(self,dt):
        if self.single_player == True:
            self.past_ms += dt
        

    def add_point (self, goal_side):
        if self.single_player == True:
            return
        if goal_side == "left":
            self.right += 1
        elif goal_side == "right":
            self.left += 1

    def reset(self):
        self.left = 0
        self.right = 0
        self.past_ms = 0

    def draw_score(self,screen):
        left_text = self.font.render(str(self.left), True, self.left_color)
        right_text = self.font.render(str(self.right), True, self.right_color)
        screen.blit(left_text, left_text.get_rect(center=(self.x - 100, self.y)))
        screen.blit(right_text, right_text.get_rect(center=(self.x + 100, self.y)))

    def draw_time(self,screen):
        seconds = self.past_ms // 1000
        time_str = f"{seconds // 60:02}:{seconds % 60:02}"
        text = self.font.render(time_str, True, self.left_color)
        screen.blit(text, text.get_rect(center=(self.x, self.y)))


    def draw(self,screen):
        if self.single_player:
            self.draw_time(screen)
        else:
            self.draw_score(screen)
        