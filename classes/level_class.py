from settings import *
import classes.obstacle_class as obstacle_class
import classes.enemy_class as enemy_class
class Level:
    def __init__(self, map_grid, adjacents):
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.map = map_grid
        self.up, self.down, self.left, self.right = adjacents
        y_pos = 0
        for y in self.map:
            x_pos = 0
            for x in y:
                if x == "x":
                    obstacle_class.Obstacle((x_pos, y_pos), img.tree_img_1, self)
                if x == "!":
                    enemy_class.Enemy((x_pos, y_pos), img.enemy_img_1, self)

                x_pos += TILE_SIZE
            y_pos += TILE_SIZE

        print(self.obstacle_sprites)

    def draw(self, surface):
        self.obstacle_sprites.draw(surface)
        self.enemy_sprites.draw(surface)

    def update(self):
        self.obstacle_sprites.update()
        self.enemy_sprites.update()