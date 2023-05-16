# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Rect([36, 36, 568, 568])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "red", player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos = pygame.Rect.move(player_pos, 0, -100)
    if keys[pygame.K_s]:
        player_pos = pygame.Rect.move(player_pos, 0, +100)
    if keys[pygame.K_a]:
        player_pos = pygame.Rect.move(player_pos, -100, 0)
    if keys[pygame.K_d]:
        player_pos = pygame.Rect.move(player_pos, 100, 0)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
