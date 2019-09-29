import pygame
from .custom_events import *

class SurfaceEvents:
    def __init__(self):
        self._dict_mouse_events = {
            pygame.MOUSEBUTTONDOWN : self.mouse_down,
            pygame.MOUSEBUTTONUP : self.mouse_up,
            pygame.MOUSEMOTION : self.mouse_moved,
            MOUSECLICKED : self.mouse_clicked,
            MOUSEHOLD : self.mouse_hold
        }

        self._dict_key_events = {
            pygame.KEYUP : self.key_up,
            pygame.KEYDOWN : self.key_down,
            KEYHOLD : self.key_hold,
            KEYPRESSED : self.key_pressed
        }

    def process_events(self, events):
        allowed_events = []
        for event in events:
            if event.type in self._dict_key_events:
                event = self._key_event(event)
            elif event.type in self._dict_mouse_events:
                event = self._mouse_event(event)
            else:
                event = self.on_event(event)


            if event is not None:
                allowed_events.append(event)
        
        return allowed_events
        
    def mouse_up(self, event):
        return event

    def mouse_down(self, event):
        return event

    def mouse_clicked(self, event):
        return event
    
    def mouse_moved(self, event):
        return event

    def mouse_hold(self, event):
        return event
    
    def key_pressed(self, event):
        return event

    def key_hold(self, event):
        return event
    
    def key_up(self, event):
        return event

    def key_down(self, event):
        return event

    def on_event(self, event):
        return event

    def _mouse_event(self, event):
        return self._dict_mouse_events[event.type](event)

    def _key_event(self, event):
        return self._dict_key_events[event.type](event)