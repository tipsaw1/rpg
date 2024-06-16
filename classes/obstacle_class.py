from settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, image, level):
        pygame.sprite.Sprite.__init__(self, level.obstacle_sprites)
        self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft = pos)


