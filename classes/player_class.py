import pygame.sprite

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, level):
        pygame.sprite.Sprite.__init__(self, all_sprites, players)
        self.inventory = []
        self.image = pygame.transform.scale(img.player_img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = speed
        self.facing = ""
        self.level = level
        self.dx = 0
        self.dy = 0

    # Update
    def update(self):
        self.check_keys()
        self.move()

    # Checks for keyboard input
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dy -= self.speed
            self.facing = "up"
        if keys[pygame.K_DOWN]:
            self.dy += self.speed
            self.facing = "down"
        if keys[pygame.K_LEFT]:
            self.dx -= self.speed
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.dx += self.speed
            self.facing = "right"

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

