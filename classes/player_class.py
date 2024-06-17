import pygame.sprite

import classes.enemy_class
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, hp, level):
        pygame.sprite.Sprite.__init__(self, player_sprite)
        self.level = level
        # Player image
        self.image = pygame.transform.scale(img.player_img, (TILE_SIZE//2, TILE_SIZE//2))
        self.rect = self.image.get_rect(topleft=pos)

        # Player stats
        self.normal_speed = speed
        self.speed = self.normal_speed
        self.dx = 0
        self.dy = 0
        self.max_hp = hp
        self.hp = hp
        # Attacking and taking damage
        self.facing = ""
        self.cooldown = 1500
        self.last_hit = -self.cooldown
        self.last_flash = 0
        # Inventory
        self.inventory = []

    # Update
    def update(self):
        self.speed = self.normal_speed
        self.image.fill("blue")
        self.check_keys()
        self.move()
        self.check_borders()

    # Checks for keyboard input
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy -= self.speed
            self.facing = "up"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy += self.speed
            self.facing = "down"
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx -= self.speed
            self.facing = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += self.speed
            self.facing = "right"
        if keys[pygame.K_SPACE]:
            self.speed *= 5

    # Moves the player
    def move(self):
        if self.dx != 0 or self.dy != 0:
            self.dx, self.dy = calculate_movement(self.dx, self.dy, self.speed)
        
        self.rect.x += self.dx
        self.collide('x')
        self.rect.y += self.dy
        self.collide('y')
        self.dx, self.dy = 0, 0

    # Checks for collisions
    def collide(self, direction):
        collision = pygame.sprite.spritecollideany(self, self.level.obstacle_sprites)

        if collision:
            if direction == "x":
                if self.dx > 0:
                    self.rect.right = collision.rect.left

                if self.dx < 0:
                    self.rect.left = collision.rect.right

            if direction == "y":
                if self.dy < 0:
                    self.rect.top = collision.rect.bottom

                if self.dy > 0:
                    self.rect.bottom = collision.rect.top

        if type(collision) == classes.enemy_class.Enemy:
            self.take_damage(collision.damage)

    # Allows player to move between screens
    def check_borders(self):
        if self.level.up:
            if self.rect.centery < 0:
                self.level = self.level.up
                self.level.__init__(self.level.map, self.level.background_color, self.level.wall_img, self.level.adjacents)
                self.rect.bottom = SCREEN_H

        if self.level.down:
            if self.rect.centery > SCREEN_H:
                self.level = self.level.down
                self.level.__init__(self.level.map, self.level.background_color, self.level.wall_img, self.level.adjacents)
                self.rect.top = 0
        if self.level.left:
            if self.rect.centerx < 0:
                self.level = self.level.left
                self.level.__init__(self.level.map, self.level.background_color, self.level.wall_img, self.level.adjacents)
                self.rect.right = SCREEN_W
        if self.level.right:
            if self.rect.centerx > SCREEN_W:
                self.level = self.level.right
                self.level.__init__(self.level.map, self.level.background_color, self.level.wall_img, self.level.adjacents)
                self.rect.left = 0

    # Take damage
    def take_damage(self, damage):
        if pygame.time.get_ticks() - self.last_hit >= self.cooldown:
            self.hp = max(self.hp-damage, 0)
            self.last_hit = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.last_hit <= 50:
            self.image.fill("red2")