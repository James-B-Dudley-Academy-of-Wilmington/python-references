# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = [
        pygame.Vector2(400, 700),
        pygame.Vector2(500, 300),
        pygame.Vector2(700, 400)
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.polygon(screen, "yellow", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[0].y -= 300 * dt
        player_pos[1].y -= 300 * dt
        player_pos[2].y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos[0].y += 300 * dt
        player_pos[1].y += 300 * dt
        player_pos[2].y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos[0].x -= 300 * dt
        player_pos[1].x -= 300 * dt
        player_pos[2].x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos[0].x += 300 * dt
        player_pos[1].x += 300 * dt
        player_pos[2].x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
