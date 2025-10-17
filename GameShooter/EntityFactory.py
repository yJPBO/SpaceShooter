import random
from GameShooter.Background import Background
from GameShooter.Const import SCOREBG_HEIGHT, WIN_HEIGHT, WIN_WIDTH
from GameShooter.Enemy import Enemy
from GameShooter.Entity import Entity
from GameShooter.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)) -> list[Entity]:
        match entity_name:
            case "LevelBg":
                list_bg = []
                for i in range(2):
                    list_bg.append(Background(f'LevelBg{i}', (0, 0)))
                    list_bg.append(Background(
                        f'LevelBg{i}', (0, 0 - WIN_HEIGHT)))
                return list_bg
            case "ScoreBg":
                return [Background(f'ScoreBg', (0, WIN_HEIGHT - SCOREBG_HEIGHT))]
            case "Player1":
                return [Player("Player1", ((WIN_WIDTH / 2) - 32, WIN_HEIGHT - 100 - SCOREBG_HEIGHT))]
            case "Player2":
                return [Player("Player2", ((WIN_WIDTH / 2) - 32, WIN_HEIGHT - 100 - SCOREBG_HEIGHT))]
            case "Enemy1":
                return [Enemy("Enemy1", ((random.randint(5, WIN_WIDTH - 64)), -65))]
            case "Enemy2":
                return [Enemy("Enemy2", ((random.randint(5, WIN_WIDTH - 64)), -65))]
            case "Enemy3":
                return [Enemy("Enemy3", ((random.randint(5, WIN_WIDTH - 64)), -65))]
        return []
