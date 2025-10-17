from GameShooter.EnemyShot import EnemyShot
from GameShooter.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED
from GameShooter.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]

    def shoot(self):
        if self.name == "Enemy3":
            return
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f'{self.name}Shot', (self.rect.centerx, self.rect.bottom))
