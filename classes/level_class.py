from settings import *
import classes.obstacle_class as obstacle_class
import classes.enemy_class as enemy_class
class Level:
    def __init__(self, map_grid, background_color, wall_img):
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.map = map_grid
        self.up, self.down, self.left, self.right = None, None, None, None
        self.background_color = background_color
        self.wall_img = wall_img
        self.add_sprites()

    def draw(self, surface):
        surface.fill(self.background_color)
        self.obstacle_sprites.draw(surface)
        self.enemy_sprites.draw(surface)

    def update(self):
        self.obstacle_sprites.update()
        self.enemy_sprites.update()

    def add_sprites(self):
        y_pos = 0
        for y in self.map:
            x_pos = 0
            for x in y:
                if x == "x":
                    obstacle_class.Obstacle((x_pos, y_pos), self.wall_img, self)
                if x == "!":
                    enemy_class.Enemy((x_pos, y_pos), img.enemy_img_1, self)

                x_pos += TILE_SIZE
            y_pos += TILE_SIZE

    def set_adjacents(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right