# Imports
from settings import *
import classes.obstacle_class as obstacle_class
import classes.enemy_class as enemy_class
import classes.level_class as level_class
import classes.player_class as player_class

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
level_1 = level_class.Level(maps.level_1_map, (1,2,3,4))
p1 = player_class.Player((TILE_SIZE, TILE_SIZE), 5, level_1)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                obstacle_class.Obstacle(event.pos, img.tree_img_1, level_1)

    # Player movement

    # Background color
    screen.fill("white")

    # Draw/update sprites
    players.draw(screen)
    players.update()
    level_1.update()
    level_1.draw(screen)

    # Screen update
    pygame.display.flip()
    clock.tick(FPS)

# Close window
pygame.quit()
