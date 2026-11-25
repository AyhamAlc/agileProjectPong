import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 强制把最外层目录加进搜索路径


from Shared.settings import COLORS
import pygame


class GameOverScreen:

    def __init__(self, screen, winner_name):
        self.screen = screen
        self.winner_name = winner_name
        # self.p1_score = p1_score
        # self.p2_score = p2_score
        #self.max_rally = max_rally
        # Safe Font initialization
        if not pygame.font.get_init():
            pygame.font.init()
        
        self.font_title = pygame.font.SysFont(None, 40, bold=True)
        self.font_normal = pygame.font.SysFont(None, 22)
        self.font_small = pygame.font.SysFont(None, 18)

       #create a dark, semi-transparent overlay to cover the game when it shows up by SRCALPHA
        self.overlay = pygame.Surface((1280,720), pygame.SRCALPHA)
        self.overlay.fill((11,16,32,215))

       #create the main card rec
        self.card_rect = pygame.Rect(390, 90, 500, 540)

       #set up buttons
        self.btn_w = 420
        self.btn_h = 46
       #make sure the buttons are centered in the card
        btn_x =self.card_rect.centerx - self.btn_w // 2

        #define the clickable areas for the buttons
        self.replay_rect = pygame.Rect(btn_x, 420, self.btn_w, self.btn_h)
        self.menu_rect = pygame.Rect(btn_x, 480, self.btn_w, self.btn_h)
        self.quit_rect = pygame.Rect(btn_x, 540, self.btn_w, self.btn_h)

#check if the player clicked a button or pressed a key
    def handle_events(self, event):
        #MOUNSECLICKS 1 means that left click 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.replay_rect.collidepoint(mouse_pos):
                return "replay"
            elif self.menu_rect.collidepoint(mouse_pos):
                return "menu"
            elif self.quit_rect.collidepoint(mouse_pos):
                return "quit"
        #KEYBOARD INPUTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return "replay"
            elif event.key == pygame.K_m:
                return "menu"
            elif event.key == pygame.K_q:
                return "quit"
        
        return None

#draw everything in the screen
    def draw(self):
        self.screen.blit(self.overlay, (0, 0))
        pygame.draw.rect(self.screen, COLORS["card_bg"], self.card_rect,border_radius=16)
        pygame.draw.rect(self.screen, COLORS["card_border"], self.card_rect, width=2, border_radius=16)
        #draw the top badge("Game Over")
        badge_rect = pygame.Rect(0,0,240,26)
        badge_rect.center = (self.card_rect.centerx,self.card_rect.top + 32)
        pygame.draw.rect(self.screen, COLORS["mint"], badge_rect, width=1, border_radius=12)
        badge_text = self.font_small.render("GAME OVER - MATCH ENDED", True, COLORS["mint"])
        self.screen.blit(badge_text, badge_text.get_rect(center=badge_rect.center))
        #draw the title
        title_text = self.font_title.render(f"{self.winner_name} Wins!", True, COLORS["text_light"])
        self.screen.blit(title_text, title_text.get_rect(center=(self.card_rect.centerx, self.card_rect.top + 80)))

        winner_text = self.font_normal.render(f"Congratulations {self.winner_name} reached the target!", True, COLORS["mint"])
        self.screen.blit(winner_text, winner_text.get_rect(center=(self.card_rect.centerx, self.card_rect.top + 120)))
        
        mouse_pos = pygame.mouse.get_pos()

        #replay button 
        #if mouse is inside the button area, change the color to hover color
        is_replay_hover = self.replay_rect.collidepoint(mouse_pos)
        pygame.draw.rect(self.screen, COLORS["mint_hover"] if is_replay_hover else COLORS["mint"], self.replay_rect, border_radius=8)
        replay_txt = self.font_normal.render("Replay", True, COLORS["text_dark"])
        self.screen.blit(replay_txt, replay_txt.get_rect(center=self.replay_rect.center))

        #main menu button 
        is_menu_hover = self.menu_rect.collidepoint(mouse_pos)
        pygame.draw.rect(self.screen, COLORS["btc_hover"] if is_menu_hover else COLORS["btc_sec"], self.menu_rect, border_radius=8)
        pygame.draw.rect(self.screen, COLORS["btc_border"], self.menu_rect, width=1, border_radius=8)
        menu_txt = self.font_normal.render("Main Menu", True, COLORS["text_light"])
        self.screen.blit(menu_txt, menu_txt.get_rect(center=self.menu_rect.center))

        #quit button
        is_quit_hover = self.quit_rect.collidepoint(mouse_pos)
        pygame.draw.rect(self.screen, COLORS["btc_hover"] if is_quit_hover else COLORS["btc_sec"], self.quit_rect, border_radius=8)
        pygame.draw.rect(self.screen, COLORS["btc_border"], self.quit_rect, width=1, border_radius=8)
        quit_txt = self.font_normal.render("Quit", True, COLORS["text_light"])
        self.screen.blit(quit_txt, quit_txt.get_rect(center=self.quit_rect.center))
