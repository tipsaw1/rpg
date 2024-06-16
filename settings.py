# Imports
import pygame
import random
import math
import assets.images as img
import assets.maps as maps

# Pygame setup
pygame.init()

# Sprite groups
player_group = pygame.sprite.GroupSingle()

# Screen info
SCREEN_W = 960
SCREEN_H = 960
TILE_SIZE = SCREEN_W/20
FPS = 60

def calculate_movement(dx, dy, speed):
    angle = math.atan2(dy, dx)
    dx = speed*math.cos(angle)
    dy = speed*math.sin(angle)
    return dx, dy
