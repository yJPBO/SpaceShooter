from random import choice
import random
import pygame


from GameShooter.Const import C_ORANGE, C_RED, C_WHITE, C_YELLOW, DIFFICULTY_INCREASE_MODIFIER, DIFFICULTY_INCREASE_TIME, EVENT_DIFFICULTY_INCREASE, EVENT_ENEMY, EVENT_IFRAME, GLOBAL_VOLUME, MENU_OPTION, SCOREBG_HEIGHT, SPAWN_TIME, WIN_HEIGHT, WIN_WIDTH
from GameShooter.Enemy import Enemy
from GameShooter.Entity import Entity
from GameShooter.EntityFactory import EntityFactory
from GameShooter.EntityMediator import EntityMediator
from GameShooter.Player import Player


class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str) -> None:
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.score_entity: Entity = (EntityFactory.get_entity("ScoreBg")[0])
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("LevelBg"))
        player1 = EntityFactory.get_entity("Player1")
        self.entity_list.extend(player1)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player2 = EntityFactory.get_entity("Player2")
            self.entity_list.extend(player2)
        self.difficulty = 1
        pygame.time.set_timer(EVENT_ENEMY, int(SPAWN_TIME / self.difficulty))
        pygame.time.set_timer(EVENT_IFRAME, 100)
        pygame.time.set_timer(EVENT_DIFFICULTY_INCREASE,
                              DIFFICULTY_INCREASE_TIME)

    def run(self, player_score: list[int]):
        pygame.mixer.music.load("asset/level.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(GLOBAL_VOLUME)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            self.score_level_ui()
            self.level_text(10, f"FPS: {clock.get_fps():.0f}", C_WHITE,
                            (10, 10), -1)
            # self.level_text(10, f"{len(self.entity_list)}: Entities", C_WHITE,
            #                 (WIN_WIDTH - 10, 10), 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(
                        ("Enemy1", "Enemy1", "Enemy2", "Enemy2", "Enemy3"))
                    self.entity_list.extend(EntityFactory.get_entity(choice))
                if event.type == EVENT_IFRAME:
                    for ent in self.entity_list:
                        if ent.iframe > 0:
                            ent.iframe -= 1
                            if isinstance(ent, Player):
                                ent.damage_blink()
                        elif ent.iframe == 0 and isinstance(ent, Player):
                            pygame.image.load(
                                "asset/" + ent.name + ".png").convert_alpha()
                if event.type == EVENT_DIFFICULTY_INCREASE and self.difficulty < 10:
                    self.difficulty += DIFFICULTY_INCREASE_MODIFIER
                    pygame.time.set_timer(EVENT_ENEMY, int(
                        SPAWN_TIME / self.difficulty))

            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:
                return

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            for ent in self.entity_list:
                if isinstance(ent, Player) and ent.name == "Player1":
                    player_score[0] = ent.score
                if isinstance(ent, Player) and ent.name == "Player2":
                    player_score[1] = ent.score

    # Anchor:
    #   Center = 0
    #   Left = -1
    #   Right = 1
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, anchor: int = 0):
        text_font: pygame.font.Font = pygame.font.Font(
            "asset/font.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        if anchor == 0:
            text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)
            self.window.blit(source=text_surf, dest=text_rect)
        elif anchor == -1:
            text_rect: pygame.Rect = text_surf.get_rect(midleft=text_pos)
            self.window.blit(source=text_surf, dest=text_rect)
        elif anchor == 1:
            text_rect: pygame.Rect = text_surf.get_rect(midright=text_pos)
            self.window.blit(source=text_surf, dest=text_rect)

    def score_level_ui(self):
        # Score UI Background
        self.window.blit(source=self.score_entity.surf,
                         dest=self.score_entity.rect)
        for ent in self.entity_list:
            if ent.name == "Player1":
                surf_healthP1 = pygame.image.load("asset/health_icon.png")
                surf_scoreP1 = pygame.image.load("asset/score_icon.png")
                rect_healthP1 = surf_healthP1.get_rect(
                    center=(15, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 10))
                rect_scoreP1 = surf_scoreP1.get_rect(
                    center=(15, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 30))
                self.level_text(
                    15, f'Player 1', C_WHITE, (10, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) - 10), -1)
                self.level_text(
                    15, f'{ent.health}', C_WHITE, (30, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 10), -1)
                self.level_text(
                    15, f'{ent.score}', C_WHITE, (30, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 30), -1)

                self.window.blit(surf_healthP1, rect_healthP1)
                self.window.blit(surf_scoreP1, rect_scoreP1)
            if ent.name == "Player2":
                surf_healthP2 = pygame.image.load("asset/health_icon.png")
                surf_scoreP2 = pygame.image.load("asset/score_icon.png")
                rect_healthP2 = surf_healthP2.get_rect(
                    center=(WIN_WIDTH - 15, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 10))
                rect_scoreP2 = surf_scoreP2.get_rect(
                    center=(WIN_WIDTH - 15, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 30))
                self.level_text(
                    15, f'Player 2', C_WHITE, (WIN_WIDTH - 10, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) - 10), 1)
                self.level_text(
                    15, f'{ent.health}', C_WHITE, (WIN_WIDTH - 30, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 10), 1)
                self.level_text(
                    15, f'{ent.score}', C_WHITE, (WIN_WIDTH - 30, (WIN_HEIGHT - SCOREBG_HEIGHT / 2) + 30), 1)

                self.window.blit(surf_healthP2, rect_healthP2)
                self.window.blit(surf_scoreP2, rect_scoreP2)

        self.level_text(15, "Difficulty", C_WHITE,
                        (WIN_WIDTH / 2, WIN_HEIGHT - SCOREBG_HEIGHT / 2 - 10))
        difficulty_color = C_WHITE
        if self.difficulty >= 10:
            difficulty_color = C_RED
        elif self.difficulty > 6:
            difficulty_color = C_ORANGE
        elif self.difficulty > 3:
            difficulty_color = C_YELLOW

        self.level_text(20, f"{self.difficulty:.2f}", difficulty_color,
                        (WIN_WIDTH / 2, WIN_HEIGHT - SCOREBG_HEIGHT / 2 + 10))
