import pygame
from widget import Widget
from test_widget import Test
from event.custom_events import KEY_PRESSED_CODE

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
            self.post_key_events()
            events = pygame.event.get()
            self._update(events)

        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def on_init(self):
        pass
    
    def on_render(self):
        self.fill((0,0,0))
        pygame.display.flip()

    def post_key_events(self):
        keys_stats = pygame.key.get_pressed()
        for key_code, key_state in enumerate(keys_stats):
            if key_state:
                self.post_event(pygame.event.Event(KEY_PRESSED_CODE ,key_code = key_code))
    