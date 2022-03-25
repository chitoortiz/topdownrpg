import pygame

from settings import *


class Intro:
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.title_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE + 30)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

    def title(self, title):
        text_surf = self.title_font.render(title, False, UI_BORDER_COLOR)
        x = self.display_surface.get_size()[0]//2
        y = self.display_surface.get_size()[1]//2
        text_rect = text_surf.get_rect(center=(x, y))

        self.display_surface.blit(text_surf, text_rect)

    def instructions(self):
        text_surf = self.font.render('Press SPACE to start game', False, UI_BORDER_COLOR)
        x = self.display_surface.get_size()[0]//2
        y = self.display_surface.get_size()[1] - 50
        text_rect = text_surf.get_rect(center=(x, y))

        self.display_surface.blit(text_surf, text_rect)

    def run(self):
        self.title('What if Zelda was a girl?')
        self.instructions()
