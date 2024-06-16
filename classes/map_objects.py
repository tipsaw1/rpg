from settings import *

class Map_object(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self, all_sprites, map_objects)
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
