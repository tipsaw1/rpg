from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self, all_sprites, enemies)
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        print(pygame.sprite.spritecollideany(self, players))

