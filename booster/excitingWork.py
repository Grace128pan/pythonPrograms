import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Boost Your Energy Game')

# Load assets
background_img = pygame.image.load('booster/background.jpg')  # Load a background image
watermelon_img = pygame.image.load('booster/watermelon.jpg')  # Load a watermelon image
watermelon_img = pygame.transform.scale(watermelon_img, (50, 50))  # Resize watermelon image

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Sounds
snappy_music = 'booster/schnippi.mp3'  # Load your snappy music file
schnippi_song = 'booster/schnippi.mp3'  # Load your schnippi song file
pygame.mixer.music.load(snappy_music)

# Game variables
clock = pygame.time.Clock()
watermelons = []
score = 0
game_over = False
start_time = 0

def show_message(message, y_offset=0):
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + y_offset))
    screen.blit(text, text_rect)

def spawn_watermelon():
    x = random.randint(0, SCREEN_WIDTH - watermelon_img.get_width())
    y = -watermelon_img.get_height()
    watermelons.append(pygame.Rect(x, y, watermelon_img.get_width(), watermelon_img.get_height()))

def draw_watermelons():
    for watermelon in watermelons:
        screen.blit(watermelon_img, (watermelon.x, watermelon.y))

def handle_watermelons():
    global score
    for watermelon in watermelons[:]:
        watermelon.y += 5  # Speed of falling
        if watermelon.top > SCREEN_HEIGHT:
            watermelons.remove(watermelon)
        if pygame.mouse.get_pressed()[0] and watermelon.collidepoint(pygame.mouse.get_pos()):
            watermelons.remove(watermelon)
            score += 1

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        show_message('Choose your mode:', -50)
        show_message('1. Sleepy', 0)
        show_message('2. Energetic', 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.music.play()
                    time.sleep(10)
                    pygame.mixer.music.stop()
                elif event.key == pygame.K_2:
                    running = False

def game_loop():
    global game_over, score, start_time
    score = 0
    start_time = time.time()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_q:
                    game_over = True

        screen.fill(WHITE)
        screen.blit(background_img, (0, 0))

        if random.randint(1, 20) == 1:
            spawn_watermelon()

        handle_watermelons()
        draw_watermelons()

        elapsed_time = time.time() - start_time
        timer_text = small_font.render(f'Time: {int(50 - elapsed_time)}s', True, BLACK)
        screen.blit(timer_text, (10, 10))

        score_text = small_font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 40))

        if elapsed_time > 50:
            game_over = True
            if score >= 20:
                pygame.mixer.music.load(schnippi_song)
                pygame.mixer.music.play()
                show_message('You Win!', -50)
            else:
                show_message('You Lose!', -50)
            show_message('Press Y to continue, N to quit', 50)

        pygame.display.flip()
        clock.tick(30)

    wait_for_retry()

def wait_for_retry():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_y, pygame.K_n]:
                    if event.key == pygame.K_y:
                        waiting = False
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        exit()
        
        show_message('Press Y to continue, N to quit', 50)
        pygame.display.flip()
        clock.tick(5)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    paused = False
                elif event.key == pygame.K_n:
                    pygame.quit()
                    exit()
        show_message('Paused', -50)
        show_message('Press Y to continue, N to quit', 50)
        pygame.display.flip()
        clock.tick(5)

def main():
    while True:
        main_menu()
        game_loop()

if __name__ == "__main__":
    main()
