# music.py
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Global variables
playlist = []
current_song_index = 0
paused = False

def load_songs(files):
    global playlist
    playlist = files

def play_song():
    global paused
    if playlist:
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play(loops=0)
        paused = False

def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    play_song()

def prev_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
    else:
        current_song_index = len(playlist) - 1
    play_song()

def get_current_song():
    if playlist:
        return os.path.basename(playlist[current_song_index])
    return "No song playing"
