import pygame
from event.custom_events import KEY_PRESSED_CODE

class SurfaceEvents:
    def __init__(self):
        self._dict_events = {
           pygame.KEYUP : self.key_up,
           pygame.KEYDOWN : self.key_down,
           pygame.MOUSEBUTTONUP : self.mouse_pressed,
           pygame.MOUSEBUTTONDOWN : self.mouse_released,
           pygame.MOUSEMOTION : self.mouse_moved,
           KEY_PRESSED_CODE : self.key_pressed

        }

    def process_events(self, events):
        allowed_events = []
        for event in events:
            if event.type in self._dict_events:
                event = self._dict_events[event.type](event)
            else:
                event = self.on_event(event)

            if event is not None:
                allowed_events.append(event)
        
        return allowed_events
        
    def mouse_pressed(self, event):
        return event
    
    def mouse_released(self, event):
        return event

    def mouse_clicked(self, event):
        return event
    
    def mouse_moved(self, event):
        return event
    
    def key_pressed(self, event):
        return event
    
    def key_up(self, event):
        return event

    def key_down(self, event):
        return event

    def on_event(self, event):
        return event
    
    def post_event(self, event):
        pygame.event.post(event)
