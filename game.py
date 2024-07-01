import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Game settings
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height
player_speed = 10

object_width = 30
object_height = 30
object_speed = 7

# Game variables
score = 0
game_over = False

# Font
font = pygame.font.SysFont(None, 55)

def draw_player(x, y):
    pygame.draw.rect(screen, black, [x, y, player_width, player_height])

def draw_object(x, y):
    pygame.draw.rect(screen, red, [x, y, object_width, object_height])

def display_score(score):
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])

# Main game loop
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Ensure player stays within the screen
    player_x = max(0, min(player_x, screen_width - player_width))

    # Update object position
    object_y += object_speed
    if object_y > screen_height:
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)
        score += 1

    # Check for collision
    if (player_x < object_x < player_x + player_width or player_x < object_x + object_width < player_x + player_width) and (player_y < object_y + object_height < player_y + player_height):
        game_over = True

    # Draw everything
    screen.fill(white)
    draw_player(player_x, player_y)
    draw_object(object_x, object_y)
    display_score(score)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
