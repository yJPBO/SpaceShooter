import sys
import pygame

from GameShooter.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from GameShooter.Level import Level
from GameShooter.Menu import Menu
from GameShooter.Score import Score


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("SpaceShooter")
        icon = pygame.image.load("asset/Player1.png")
        pygame.display.set_icon(icon)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run(player_score)
                score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()
            else:
                pass
