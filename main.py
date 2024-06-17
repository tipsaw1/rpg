# Imports
from settings import *
import classes.obstacle_class as obstacle_class
import classes.enemy_class as enemy_class
import classes.level_class as level_class
import classes.player_class as player_class

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

# Initialize the levels
level_1 = level_class.Level(maps.level_1_map, "navajowhite2", img.tree_img_1, (None, None, None, None))
level_2 = level_class.Level(maps.level_2_map, "brown", img.tree_img_2, (None, None, None, None))

# Set adjacent levels
level_1.set_adjacents(None, None, None, level_2)
level_2.set_adjacents(None, None, level_1, None)

# Player
p1 = player_class.Player((TILE_SIZE, TILE_SIZE), 5, 100, level_1)

# Game loop
running = True
while running:
    # Mouse and keyboard
    buttons = pygame.mouse.get_pressed()
    mouseX, mouseY = pygame.mouse.get_pos()

    # Events
    for event in pygame.event.get():
        # Quit when red X is pressed
        if event.type == pygame.QUIT:
            running = False

    # Draw/update sprites
    p1.level.update()
    p1.level.draw(screen)
    player_sprite.draw(screen)
    player_sprite.update()

    # Screen update
    pygame.display.flip()
    clock.tick(FPS)

# Close window
pygame.quit()
