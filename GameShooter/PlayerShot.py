from GameShooter.Const import ENTITY_SPEED
from GameShooter.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)
        self.rect = self.surf.get_rect(center=position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]
