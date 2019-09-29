import pygame
from pygame.event import EventType

KEYPRESSED = 30
KEYHOLD = 29

MOUSECLICKED = 31
MOUSEHOLD = 32

MOUSE_STATS_CACHE = None
KEYS_STATS_CACHE = None

def add_custom_event(event):
    pygame.event.post(event)

def set_key_custom_events():
    global KEYS_STATS_CACHE
    keys_stats = pygame.key.get_pressed()
    if KEYS_STATS_CACHE is None:
        KEYS_STATS_CACHE = keys_stats

    for key_code, key_state in enumerate(keys_stats):
        if KEYS_STATS_CACHE[key_code] and not key_state:
            add_custom_event(pygame.event.Event(KEYPRESSED, key = key_code))
        if key_state:
            add_custom_event(pygame.event.Event(KEYHOLD, key = key_code))
    
    KEYS_STATS_CACHE = keys_stats

def set_mouse_custom_event():
    global MOUSE_STATS_CACHE
    mouse_stats = pygame.mouse.get_pressed()
    if MOUSE_STATS_CACHE is None:
        MOUSE_STATS_CACHE = mouse_stats

    for mouse_key_code, mouse_key_state in enumerate(mouse_stats):
        if MOUSE_STATS_CACHE[mouse_key_code] and not mouse_key_state:
            add_custom_event(pygame.event.Event(MOUSECLICKED, key = mouse_key_state))
        if mouse_key_state:
            add_custom_event(pygame.event.Event(MOUSEHOLD, key = mouse_key_state))

    MOUSE_STATS_CACHE = mouse_stats

def set_custom_events():
    set_key_custom_events()
    set_mouse_custom_event()