import pygame
# C
C_WHITE = (255, 255, 255)
C_PURPLE = (204, 102, 255)
C_YELLOW = (255, 255, 102)
C_RED = (204, 0, 0)
C_ORANGE = (255, 153, 0)
# D

# time to increase the difficulty (in milliseconds)
DIFFICULTY_INCREASE_TIME = 5000
# Difficulty increase on event
DIFFICULTY_INCREASE_MODIFIER = 1

# E

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_IFRAME = pygame.USEREVENT + 2
EVENT_DIFFICULTY_INCREASE = pygame.USEREVENT + 3


ENTITY_HEALTH = {
    'ScoreBg': 999,
    'LevelBg0': 999,
    'LevelBg1': 999,
    'Player1': 500,
    'Player1Shot': 1,
    'Player2': 500,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Enemy3': 100,
}

ENTITY_DAMAGE = {
    'ScoreBg': 0,
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player1': 999,
    'Player1Shot': 25,
    'Player2': 999,
    'Player2Shot': 20,
    'Enemy1': 100,
    'Enemy1Shot': 20,
    'Enemy2': 100,
    'Enemy2Shot': 25,
    'Enemy3': 300,
}

ENTITY_SCORE = {
    'ScoreBg': 999,
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 250,
}

ENTITY_SPEED = {
    'ScoreBg': 0,
    "LevelBg0": 2,
    "LevelBg1": 1,
    "Player1": 5,
    "Player1Shot": 7,
    "Player2": 5,
    "Player2Shot": 7,
    "Enemy1": 2,
    "Enemy1Shot": 4,
    "Enemy2": 2,
    "Enemy2Shot": 4,
    "Enemy3": 1,
}

# 1 = 100ms
ENTITY_IFRAME = {
    'ScoreBg': 0,
    "LevelBg0": 0,
    "LevelBg1": 0,
    "Player1": 10,
    "Player1Shot": 0,
    "Player2": 10,
    "Player2Shot": 0,
    "Enemy1": 0,
    "Enemy1Shot": 0,
    "Enemy2": 0,
    "Enemy2Shot": 0,
    "Enemy3": 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 25,
    'Player2': 20,
    'Enemy1': 80,
    'Enemy2': 110,
    'Enemy3': 1,
}

# G
# (0 - 1)
GLOBAL_VOLUME = 0.4

# M

MENU_OPTION = ('SINGLEPLAYER',
               'COOPERATIVE',
               'COMPETITIVE',
               'SCORE',
               'EXIT')

# P

PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RCTRL}

# s

SCOREBG_HEIGHT = 100
SPAWN_TIME = 2000


# W

WIN_WIDTH = 512
WIN_HEIGHT = 640


SCORE_POS = {'Title': (WIN_WIDTH / 2, 70),
             'EnterName': (WIN_WIDTH / 2, 250),
             'Label': (WIN_WIDTH / 2, 150),
             'Name': (WIN_WIDTH / 2, 310),
             0: (WIN_WIDTH / 2, 190),
             1: (WIN_WIDTH / 2, 220),
             2: (WIN_WIDTH / 2, 250),
             3: (WIN_WIDTH / 2, 280),
             4: (WIN_WIDTH / 2, 310),
             5: (WIN_WIDTH / 2, 340),
             6: (WIN_WIDTH / 2, 370),
             7: (WIN_WIDTH / 2, 400),
             8: (WIN_WIDTH / 2, 430),
             9: (WIN_WIDTH / 2, 460),
             'GameOver': (WIN_WIDTH / 2, 100)
             }
