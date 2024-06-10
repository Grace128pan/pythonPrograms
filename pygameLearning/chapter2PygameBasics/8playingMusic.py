# a walkman
# there is a bug, previous button will exit the walkman; exit button did not work; others work fine
# we need add path of ffmpeg to system path in order to convert m4a to mp3 to make the program work


import pygame
import random
import sys
from pydub import AudioSegment
from pydub.utils import which
import os

# Ensure pydub uses the correct FFmpeg path
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Function to convert M4A to MP3
def convert_m4a_to_mp3(m4a_file):
    mp3_file = m4a_file.replace('.m4a', '.mp3')
    if not os.path.exists(mp3_file):  # Only convert if the MP3 doesn't already exist
        audio = AudioSegment.from_file(m4a_file, format='m4a')
        audio.export(mp3_file, format='mp3')
    return mp3_file

# List of songs to play
playlist = [
    'pygameLearning/chapter2PygameBasics/notEnough.m4a',
    'pygameLearning/chapter2PygameBasics/getThere.m4a'
]
current_track = 0

# Load background music to play when paused
background_music = [
    'pygameLearning/chapter2PygameBasics/rooster.m4a',
    'pygameLearning/chapter2PygameBasics/dobido.m4a',
    'pygameLearning/chapter2PygameBasics/schifty.m4a',
    'pygameLearning/chapter2PygameBasics/babyShark.m4a'
]

# Convert M4A files to MP3
converted_playlist = [convert_m4a_to_mp3(track) for track in playlist]
converted_background = [convert_m4a_to_mp3(track) for track in background_music]

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize Pygame
pygame.init()

# Set up the display window
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Music Player')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define button dimensions and positions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 20
BUTTON_X = (SCREEN_WIDTH - 5 * BUTTON_WIDTH - 4 * BUTTON_MARGIN) / 2
BUTTON_Y = (SCREEN_HEIGHT - BUTTON_HEIGHT) / 2

# Load button images
button_images = {
    'pause': pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT)),
    'play': pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT)),
    'next': pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT)),
    'previous': pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT)),
    'exit': pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
}

# Fill button images with color
for key in button_images:
    button_images[key].fill(GREEN)
    pygame.draw.rect(button_images[key], BLACK, button_images[key].get_rect(), 3)
    font = pygame.font.Font(None, 32)
    text = font.render(key.capitalize(), True, BLACK)
    text_rect = text.get_rect(center=(BUTTON_WIDTH // 2, BUTTON_HEIGHT // 2))
    button_images[key].blit(text, text_rect)

# Load and play the first track in the playlist
def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)

play_music(converted_playlist[current_track])

# Function to play random background music when paused
def play_random_background():
    random_bg_music = random.choice(converted_background)
    pygame.mixer.music.load(random_bg_music)
    pygame.mixer.music.play(-1)

# Main loop
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if BUTTON_X <= mouse_pos[0] <= BUTTON_X + BUTTON_WIDTH and \
               BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                if not paused:
                    pygame.mixer.music.pause()
                    play_random_background()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
            elif BUTTON_X + BUTTON_WIDTH + BUTTON_MARGIN <= mouse_pos[0] <= BUTTON_X + 2 * BUTTON_WIDTH + BUTTON_MARGIN and \
                 BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                current_track = (current_track - 1) % len(converted_playlist)
                play_music(converted_playlist[current_track])
            elif BUTTON_X + 2 * (BUTTON_WIDTH + BUTTON_MARGIN) <= mouse_pos[0] <= BUTTON_X + 3 * BUTTON_WIDTH + 2 * BUTTON_MARGIN and \
                 BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                current_track = (current_track + 1) % len(converted_playlist)
                play_music(converted_playlist[current_track])
            elif BUTTON_X + 3 * (BUTTON_WIDTH + BUTTON_MARGIN) <= mouse_pos[0] <= BUTTON_X + 4 * BUTTON_WIDTH + 3 * BUTTON_MARGIN and \
                 BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

    screen.fill(WHITE)
    for key, image in button_images.items():
        screen.blit(image, (BUTTON_X + (BUTTON_WIDTH + BUTTON_MARGIN) * list(button_images.keys()).index(key), BUTTON_Y))

    pygame.display.update()
