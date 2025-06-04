import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 48)

# Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.5
flap_power = -8

# Pipes
pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

# Score
score = 0

def create_pipe():
    height = random.randint(100, 400)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_rect = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    return top_rect, bottom_rect

# Create initial pipes
pipes.append(create_pipe())

def draw_bird(x, y):
    pygame.draw.circle(SCREEN, BLACK, (x, int(y)), bird_radius)

def draw_pipes(pipe_list):
    for top, bottom in pipe_list:
        pygame.draw.rect(SCREEN, GREEN, top)
        pygame.draw.rect(SCREEN, GREEN, bottom)

def check_collision(bird_y, pipe_list):
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
    if bird_y > HEIGHT or bird_y < 0:
        return True
    for top, bottom in pipe_list:
        if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
            return True
    return False

def show_score(score):
    text = FONT.render(str(score), True, BLACK)
    SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, 30))

# Main loop
running = True
while running:
    clock.tick(60)
    SCREEN.fill(BLUE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = flap_power

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Move pipes
    for i in range(len(pipes)):
        pipes[i] = (pipes[i][0].move(-pipe_velocity, 0), pipes[i][1].move(-pipe_velocity, 0))

    # Add new pipes
    if pipes[-1][0].x < WIDTH - 200:
        pipes.append(create_pipe())

    # Remove off-screen pipes
    if pipes[0][0].right < 0:
        pipes.pop(0)
        score += 1

    # Collision
    if check_collision(bird_y, pipes):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    draw_bird(bird_x, bird_y)
    draw_pipes(pipes)
    show_score(score)

    pygame.display.flip()
                                        