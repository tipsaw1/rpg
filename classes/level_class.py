from settings import *
import classes.obstacle_class as obstacle_class
import classes.enemy_class as enemy_class


class Level:
    def __init__(self, map_grid, background_color, wall_img, adjacents):
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Map
        self.map = map_grid
        self.adjacents = adjacents
        self.up, self.down, self.left, self.right = self.adjacents
        self.background_color = background_color
        self.wall_img = wall_img
        self.add_sprites()

    def draw(self, surface):
        surface.fill(self.background_color)
        self.all_sprites.draw(surface)

    def update(self):
        self.all_sprites.update()

    def add_sprites(self):
        y_pos = 0
        for y in self.map:
            x_pos = 0
            for x in y:
                if x == "x":
                    obstacle_class.Obstacle((x_pos, y_pos), self.wall_img, self)
                if x == "!":
                    enemy_class.Dasher((x_pos, y_pos), img.enemy_img_1, self)
                if x == "?":
                    enemy_class.Enemy((x_pos, y_pos), img.enemy_img_1, self)
                x_pos += TILE_SIZE
            y_pos += TILE_SIZE

    def set_adjacents(self, up, down, left, right):
        self.adjacents = (up, down, left, right)
        self.up, self.down, self.left, self.right = self.adjacents
