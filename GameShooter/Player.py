import pygame
from GameShooter.PlayerShot import PlayerShot
from GameShooter.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, SCOREBG_HEIGHT, WIN_HEIGHT, WIN_WIDTH
from GameShooter.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)
        # self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.shoot_delay = 0
        self.visible = True

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT - SCOREBG_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
                return PlayerShot(f"{self.name}Shot", (self.rect.centerx, self.rect.top))

    def damage_blink(self):
        if self.visible:
            self.visible = False
            self.surf = pygame.image.load(
                "asset/" + self.name + "Damage.png").convert_alpha()
        else:
            self.visible = True
            self.surf = pygame.image.load(
                "asset/" + self.name + ".png").convert_alpha()
