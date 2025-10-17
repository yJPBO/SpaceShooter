from GameShooter.Const import ENTITY_SPEED, WIN_HEIGHT
from GameShooter.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple = (0, 0)) -> None:
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0

    def shot(self):
        pass
