import pygame

# here is my list of menu_options = ["Start","Options", "Quit"] # for now
# I need to draw my menu text box woth title "Pong Game" and a button for each menu option stacked 
# I need to handle that when the game ends - the start menu appears
# I need two ways to activate each button. One by clicking with a mouse and the other by pressing a number?
# Start starts the game obviously, the game ending loop brings you back to the start menu, 
# and then quit closes all pygame windows and stops the menu loop, main loop and game loop?

class Button:
    """A clickable rectangle with a text label."""

    def __init__(self, text, center, font, width=300, height=70, color=(100, 100, 100)):
        self.text = text
        self.font = font
        self.color = color
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        label = self.font.render(self.text, True, "white")
        surface.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Menu:
    """
    This is the Start Menu for our game of Pong

    """
    def __init__(self, x, y, width, height, bg_color):
        # position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        # look
        self.bg_color = bg_color
        self.title_font = pygame.font.Font(None, 80)
        self.button_font = pygame.font.Font(None, 50)

        # buttons
        self.options = ["Start", "Quit"]
        self.buttons = []
        for i, option in enumerate(self.options):
            center = (width // 2, 300 + i * 100)
            self.buttons.append(Button(option, center, self.button_font))

    def draw(self, surface):
        # clear the window
        surface.fill(self.bg_color)

        # write the title
        title = self.title_font.render("Pong Game", True, "white")   # text, smoothing on, color
        title_rect = title.get_rect(center=(self.width // 2, 150))
        surface.blit(title, title_rect)

        # draw the buttons
        for button in self.buttons:
            button.draw(surface)


    def run(self, surface):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.is_clicked(event.pos):
                            return button.text.lower()   # "start" or "quit"
                    
            self.draw(surface)
            pygame.display.flip()