import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 8
ENEMY_SPEED = 3
ENEMY_SPAWN_RATE = 60  # Lower values spawn more enemies
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Shooter")

# Load images
player_img = pygame.image.load("python/player.png")
player_rect = player_img.get_rect()
bullet_img = pygame.image.load("python/bullet.png")
enemy_img = pygame.image.load("python/enemy.png")

# Player initial position and dimensions
player_width, player_height = 30, 30
player_rect = pygame.Rect(WIDTH // 60 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)

# Dimensions for enemy
enemy_width, enemy_height = 30, 30

# Lists to store bullets and enemies
bullets = []
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game over text
game_over_text = font.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        if len(bullets) < 3:
            bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 12)
            bullets.append(bullet)

    # Move bullets
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        enemy = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 40)
        enemies.append(enemy)

    # Move enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player, bullets, and enemies
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Game over screen
screen.fill((0, 0, 0))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.delay(2000)

pygame.quit()
sys.exit()
