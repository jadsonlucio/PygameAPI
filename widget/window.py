import pygame
from .widget import Widget
from .event.custom_events import set_custom_events

class Window(Widget):
    def __init__(self, title, width, height, posX, posY):
        self.__running = False
        self.title = title 
        self.__display_surf = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
    
        super().__init__(self.__display_surf, posX, posY, width, height)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False

    def on_execute(self):
        self.__running = True
        while(self.__running):
            set_custom_events()
            events = pygame.event.get()
            self._update(events)

        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
    
    def on_render(self):
        pygame.display.flip()

