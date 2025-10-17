import datetime
import sys
import pygame

from GameShooter.Const import C_WHITE, GLOBAL_VOLUME, MENU_OPTION, SCORE_POS
from GameShooter.DBProxy import DBProxy


class Score:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.surf = pygame.image.load("asset/LevelBg0.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer.music.load("asset/GameEnd.wav")
        pygame.mixer.music.play(0, 0, 100)
        pygame.mixer.music.set_volume(GLOBAL_VOLUME)
        db_proxy = DBProxy('DBScore')
        text = ''
        score = 0
        name = ''
        saved = False
        while not saved:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(70, "GAME", C_WHITE, SCORE_POS["GameOver"])
            self.score_text(
                70, "OVER", C_WHITE, (SCORE_POS["GameOver"][0], SCORE_POS["GameOver"][1] + 80))

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = "Enter Player1 name:"
            if game_mode == MENU_OPTION[1]:
                score = sum(player_score) / 2
                text = "Enter team name:"
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = "Enter player 1 name:"
                else:
                    score = player_score[1]
                    text = "Enter player 2 name:"

            self.score_text(15, text, C_WHITE, SCORE_POS['EnterName'])
            self.score_text(15, "(4 characters)", C_WHITE,
                            (SCORE_POS['EnterName'][0], SCORE_POS['EnterName'][1] + 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save(
                            {"name": name, "score": score,
                                "date": get_formatted_date()}
                        )
                        saved = True
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(32, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
        self.show()
        return

    def show(self):
        pygame.mixer.music.load("asset/Score.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(GLOBAL_VOLUME)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(60, "RANKING", C_WHITE, SCORE_POS['Title'])
        self.score_text(14, "NAME   SCORE         DATE      ",
                        C_WHITE, SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(
                14, f'{name} - {score:05d} - {date}', C_WHITE, SCORE_POS[list_score.index(
                    player_score)]
            )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(
            "asset/font.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
