import pygame
import sys

from settings import *
from level import Level
from intro import Intro
from outro import Outro


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = None

        self.is_intro = True
        self.intro = Intro()

        self.dead = False
        self.outro = Outro()

        # sound
        main_sound = pygame.mixer.Sound('..\\audio\\main.ogg')
        main_sound.set_volume(0.5)
        # main_sound.play(loops=-1)

    def intro_screen(self):
        self.is_intro = True
        while self.is_intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level = Level()
                        self.is_intro = False
                        self.run()

            self.screen.fill(WATER_COLOR)
            self.intro.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def game_over(self):
        self.level = None
        self.dead = True
        while self.dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('retry')
                        self.level = Level()
                        self.dead = False
                        self.run()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(WATER_COLOR)
            self.outro.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        while self.level.player.health > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

        self.game_over()


if __name__ == '__main__':
    game = Game()
    game.intro_screen()
