import pygame

from GameShooter.Const import C_PURPLE, C_WHITE, GLOBAL_VOLUME, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH


class Menu:
    def __init__(self, window) -> None:
        self.window = window
        self.surf = pygame.image.load(
            "asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load("asset/Menu.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(GLOBAL_VOLUME)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(85, "SPACE", C_WHITE,
                           (WIN_WIDTH/2, 90))
            self.menu_text(60, "SHOOTER", C_WHITE,
                           (WIN_WIDTH/2, 190))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        18, MENU_OPTION[i], C_PURPLE, ((WIN_WIDTH / 2), (400 + i*29)))
                else:
                    self.menu_text(
                        18, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), (400 + i*29)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(
            "asset/font.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
