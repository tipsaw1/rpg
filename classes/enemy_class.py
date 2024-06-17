import pygame.sprite

from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image, level):
        # Setup
        pygame.sprite.Sprite.__init__(self, level.enemy_sprites, level.all_sprites)
        self.level = level
        # Image and rect
        self.image = pygame.transform.scale(image, (TILE_SIZE//2, TILE_SIZE//2))
        self.rect = self.image.get_rect(topleft = pos)
        # Stats
        self.damage = 10
        self.hp = 50
        # Movement
        self.dash_timer = 3000
        self.last_dashed = 0
        self.dash_length = 500
        self.dx, self.dy = 0,0

    def update(self):
        self.movement_pattern()
        self.move()

        hit = pygame.sprite.spritecollideany(self, player_sprite)
        if hit:
            hit.take_damage(self.damage)

    def move(self):
        self.rect.x += self.dx
        self.collide("x", self.level.obstacle_sprites)
        self.rect.y += self.dy
        self.collide("y", self.level.obstacle_sprites)

    def collide(self, direction, sprite_group):
        collision = pygame.sprite.spritecollideany(self, sprite_group)

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

    def movement_pattern(self):
        player_x =  player_sprite.sprite.rect.centerx
        player_y =  player_sprite.sprite.rect.centery
        x_distance = player_x- self.rect.centerx
        y_distance = player_y - self.rect.centery
        self.dx, self.dy = calculate_movement(x_distance, y_distance, 5)



class Dasher(Enemy):
    def __init__(self, pos, image, level):
        super().__init__(pos, image, level)
        self.image = pygame.transform.scale(image, (TILE_SIZE//4, TILE_SIZE//4))
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = 20
        self.hp = 20
        self.dx, self.dy = 0, 0

    def movement_pattern(self):
        player_x =  player_sprite.sprite.rect.centerx
        player_y =  player_sprite.sprite.rect.centery
        if pygame.time.get_ticks() - self.last_dashed >= self.dash_timer:
            x_distance = player_x- self.rect.centerx
            y_distance = player_y - self.rect.centery
            self.dx, self.dy = calculate_movement(x_distance, y_distance, 12)
            self.last_dashed = pygame.time.get_ticks()

        elif pygame.time.get_ticks() - self.last_dashed >= self.dash_length:
            x_distance = player_x - self.rect.centerx
            y_distance = player_y - self.rect.centery
            self.dx, self.dy = calculate_movement(x_distance, y_distance, 3)


