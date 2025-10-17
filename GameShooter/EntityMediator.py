from GameShooter.EnemyShot import EnemyShot
from GameShooter.Const import ENTITY_IFRAME, ENTITY_SCORE, SCOREBG_HEIGHT, WIN_HEIGHT
from GameShooter.Enemy import Enemy
from GameShooter.Entity import Entity
from GameShooter.Player import Player
from GameShooter.PlayerShot import PlayerShot


class EntityMediator:

    # Verify entities outside of the window
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT - SCOREBG_HEIGHT:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.bottom < 0:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.top > WIN_HEIGHT - SCOREBG_HEIGHT:
                ent.health = 0

    # Verify entities inside each other
    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction and ent1.iframe == 0 and ent2.iframe == 0:
            if (ent1.rect.right >= ent2.rect.left) and (ent1.rect.left <= ent2.rect.right) and (ent1.rect.bottom >= ent2.rect.top) and (ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

                # Shots do not active invulnerability frames
                if (isinstance(ent1, Player) and isinstance(ent2, EnemyShot)) or (isinstance(ent1, EnemyShot) and isinstance(ent2, Player)):
                    return
                ent1.iframe = ENTITY_IFRAME[ent1.name]
                ent2.iframe = ENTITY_IFRAME[ent2.name]

    # Increment Player score
    @staticmethod
    def __give_score(enemy: Entity, entity_list: list[Entity]):
        if enemy.last_dmg == "Player1Shot":
            for ent in entity_list:
                if ent.name == "Player1":
                    ent.score += enemy.score
        elif enemy.last_dmg == "Player2Shot":
            for ent in entity_list:
                if ent.name == "Player2":
                    ent.score += enemy.score

    # Verify all collision
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    # Verify health and remove entities
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                    ent.rect.centerx
                entity_list.remove(ent)
