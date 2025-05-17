import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up game variables
SNAKE_SIZE = 10
SNAKE_SPEED = 15
FPS = pygame.time.Clock()

# Создаем змейку
snake_pos = deque([(100, 50), (90, 50), (80, 50)], maxlen=3)
current_key = 'a'

# apple
def get_apple_pos():
    return (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, 
            random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
apple = get_apple_pos()

while True:
    # Event handling
    new_head = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Up")
                current_key = 'w'
            elif event.key == pygame.K_s:
                print("Down")
                current_key = 's'
            elif event.key == pygame.K_a:
                print("Left")
                current_key = 'a'
            elif event.key == pygame.K_d:
                print("Right")
                current_key = 'd'

    # Update snake position based on the current key
    if current_key == 'w':
        new_head = (snake_pos[0][0], snake_pos[0][1] - SNAKE_SIZE)
    elif current_key == 's':
        new_head = (snake_pos[0][0], snake_pos[0][1] + SNAKE_SIZE)
    elif current_key == 'a':
        new_head = (snake_pos[0][0] - SNAKE_SIZE, snake_pos[0][1])
    elif current_key == 'd':
        new_head = (snake_pos[0][0] + SNAKE_SIZE, snake_pos[0][1])

    # If a new head position is calculated, add it to the snake
    if new_head:
        if new_head == apple:
            apple = get_apple_pos()
            snake_pos = deque(list(snake_pos), maxlen=snake_pos.maxlen + 1)
        snake_pos.appendleft(new_head)

    # Fill the background
    WINDOW.fill(BLACK)

    # Draw the snake
    for pos in snake_pos:
        # Создаем блок тела (квадратик)
        block = pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE)

        pygame.draw.rect(WINDOW, GREEN, block)

    # Draw the apple
    apple_block = pygame.Rect(apple[0], apple[1], SNAKE_SIZE, SNAKE_SIZE)
    pygame.draw.rect(WINDOW, RED, apple_block)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    FPS.tick(SNAKE_SPEED)
