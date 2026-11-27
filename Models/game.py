# Single-player mode (#7)
# Game class: main game loop (handle input, update, draw).
# Creates the field, ball and paddle and connects them.
import pygame

from Shared.settings import BALL_SPEED_INCREMENT,INTERVAL_S, PADDLE_SPEED_INCREMENT

class LiveScoreBoard:

    def __init__(self, x, y, left_color, right_color, font_size=72, single_player=False,left_name='Player 1', right_name='Player 2'):
        self.left = 0
        self.right = 0
        self.left_name = left_name
        self.right_name = right_name
        self.x = x
        self.y = y
        self.left_color = left_color
        self.right_color = right_color
        self.font = pygame.font.Font(None,font_size)
        self.name_font = pygame.font.Font(None, 32)
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

        left_name = self.name_font.render(self.left_name, True, self.left_color)
        right_name = self.name_font.render(self.right_name, True, self.right_color)
        screen.blit(left_name, left_name.get_rect(center=(self.x - 550, self.y)))
        screen.blit(right_name, right_name.get_rect(center=(self.x + 550, self.y)))

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

class speed_modifier:

    def __init__(self):
        self.past_ms = 0

    def ball_speed_increment_with_time_intervals(self, dt):
        self.past_ms += dt

        if self.past_ms >= INTERVAL_S * 1000:
            self.past_ms -= INTERVAL_S * 1000
            return BALL_SPEED_INCREMENT

        return 0
    
    def paddle_speed_increment_with_time_intervals(self, dt):
        self.past_ms += dt

        if self.past_ms >= INTERVAL_S * 1000:
            self.past_ms -= INTERVAL_S * 1000
            return PADDLE_SPEED_INCREMENT

        return 0

class InputBox:
    def __init__(self, width, height, left, top, font, bg_color, txt_color,
                 text="", max_length=12):
        self.rect = pygame.Rect(left, top, width, height)
        self.font = font
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.text = text
        self.max_length = max_length
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
            elif len(self.text) < self.max_length and event.unicode.isprintable():
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        border = (255, 255, 0) if self.active else (120, 120, 120)
        pygame.draw.rect(surface, border, self.rect, 2)
        img = self.font.render(self.text, True, self.txt_color)
        surface.blit(img, img.get_rect(center=self.rect.center))

def run_name_screen(screen, clock, boxes):
    title_font = pygame.font.Font(None, 48)
    title = title_font.render("Enter player names", True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return boxes[0].text or "Player 1", boxes[1].text or "Player 2"
            for box in boxes:
                box.handle_event(event)
        screen.fill((0, 0, 0))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, 150)))
        for box in boxes:
            box.draw(screen)
        pygame.display.flip()
        clock.tick(60)