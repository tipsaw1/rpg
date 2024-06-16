# Imports
import pygame
import random
import math
import assets.images as img

# Pygame setup
pygame.init()

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.GroupSingle()
map_objects = pygame.sprite.Group()

# Screen info
SCREEN_W = 1280
SCREEN_H = 960
clock = pygame.time.Clock()
fps = 60

def calculate_movement(dx, dy, speed):
    angle = math.atan2(dy, dx)
    dx = speed*math.cos(angle)
    dy = speed*math.sin(angle)
    return dx, dy
