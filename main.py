# Imports
from settings import *
import classes.player as player
import classes.enemy as enemy
import classes.map_objects as collideable

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
p1 = player.Player((SCREEN_W // 2, SCREEN_H // 2), 5)

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
                collideable.Map_object(event.pos, img.tree_img_1)

    # Player movement

    # Background color
    screen.fill("white")

    # Draw/update sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Screen update
    pygame.display.flip()
    clock.tick(60)

# Close window
pygame.quit()
