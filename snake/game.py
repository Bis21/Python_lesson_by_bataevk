import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Установки имени окна
pygame.display.set_caption("Snake Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up game variables
SNAKE_SIZE = 10
SNAKE_SPEED = 15
FPS = pygame.time.Clock()


# apple
def get_apple_pos():
    return (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, 
            random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)


# Button
class Button:
    def __init__(self, x, y, width, height, text, color=BLUE, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 20)
        self.color = color
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    

class CheckBox:
    def __init__(self, x, y, text, size=20, checked=False, passed_color=GREEN, color=WHITE):
        self.rect = pygame.Rect(x, y, size, size)
        self.checked = checked
        self.color = color
        self.passed_color = passed_color
        self.text = text
    
    def draw(self, surface):
        font = pygame.font.SysFont("Arial", 20)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(left=self.rect.right + 5, centery=self.rect.centery)
        surface.blit(text_surface, text_rect)
        pygame.draw.rect(surface, self.passed_color if self.checked else self.color, self.rect)
    
    def toggle(self):
        """Toggle the checkbox state."""
        print(f"Checkbox state before toggle: {self.checked}")
        self.checked = not self.checked
        print(f"Checkbox toggled: {self.checked}")
    
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    
    def click(self, event):
        if self.is_clicked(event):
            print("Checkbox clicked")
            self.toggle()
    
    def check(self):
        return self.checked
    


# Useful functions -------------------

def get_apple_pos():
    return (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, 
            random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)


# SCREENS -------------------

def main_menu():
    font = pygame.font.SysFont("Arial", 36)
    text = font.render("Snake Game", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    checkbox = CheckBox(WIDTH // 2 - 100, HEIGHT // 2 - 50, "Enable walls", checked=False)
    start_button = Button(WIDTH // 2 - 50, HEIGHT // 2, 100, 50, "Start")
    while True:
        WINDOW.fill(BLACK)
        
        WINDOW.blit(text, text_rect)

        # Draw the checkbox
        checkbox.draw(WINDOW)
        start_button.draw(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start_button.is_clicked(event):
                return checkbox.check()
            checkbox.click(event)

        pygame.display.flip()

def game(enable_walls=False):
    global SNAKE_SIZE, WINDOW, FPS
    SNAKE_SPEED = 15
    # Создаем змейку
    snake_pos = deque([(100, 50), (90, 50), (80, 50)], maxlen=3)
    current_key = 's'

    # apple
    apple = get_apple_pos()

    GAME_OVER = False

    count_apples = 0


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
                    current_key = 'w' if current_key != 's' else current_key
                    break
                elif event.key == pygame.K_s:
                    print("Down")
                    current_key = 's' if current_key != 'w' else current_key
                    break
                elif event.key == pygame.K_a:
                    print("Left")
                    current_key = 'a' if current_key != 'd' else current_key
                    break
                elif event.key == pygame.K_d:
                    print("Right")
                    current_key = 'd' if current_key != 'a' else current_key
                    break

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
            if enable_walls:
                # Check for wall collisions
                if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
                    print("Game Over")
                    print(new_head)
                    return count_apples
            else:
                # Infifinite board
                if new_head[0] < 0:
                    new_head = (WIDTH - SNAKE_SIZE, new_head[1])
                elif new_head[0] >= WIDTH:
                    new_head = (0, new_head[1])
                elif new_head[1] < 0:
                    new_head = (new_head[0], HEIGHT - SNAKE_SIZE)
                elif new_head[1] >= HEIGHT:
                    new_head = (new_head[0], 0)
                
            # Check for game over conditions
            
            if new_head in snake_pos:
                print("Game Over")
                print(new_head)
                return count_apples


            
            if new_head == apple:
                apple = get_apple_pos()
                count_apples += 1
                SNAKE_SPEED += 1
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


        # Шриф  
        font = pygame.font.SysFont("Arial", 14)
        # Создаем текст
        text = font.render(f"Count apples: {count_apples}", True, WHITE)
        # Создаем прямоугольник текста
        text_rect = text.get_rect(topleft=(10, 10))

        WINDOW.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        FPS.tick(SNAKE_SPEED)

def game_over(count_apples):
    # Game over screen
    WINDOW.fill(BLACK)
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"Game Over: {count_apples}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WINDOW.blit(text, text_rect)
    # Draw the button
    restart_button = Button(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50, "Restart")
    restart_button.draw(WINDOW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if restart_button.is_clicked(event):
                return True

        pygame.display.flip()


# Запуск игры --------------------------------------

while True:
    enable_walls = main_menu()
    # Start the game
    count_apples = game(enable_walls=enable_walls)
    # Restart the game
    if not game_over(count_apples):
        break
