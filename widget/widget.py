import sys

from inspect import isfunction
from .canvas import Canvas

from .event.event import SurfaceEvents

class Widget(Canvas, SurfaceEvents):
    def __init__(self, master, posX, posY, width, height):
        self.master = master
        self.posX = posX
        self.posY = posY
        self.absposX, self.absposY = posX, posY
        self.children = []
 
        if master != None and isinstance(master, Widget):
            self.absposX = self.master.posX + posX
            self.absposY = self.master.posY + posY
            self.master.children.append(self)

        Canvas.__init__(self, width, height)
        SurfaceEvents.__init__(self)

        self._on_init()

    def on_init(self):
        pass

    def on_render(self):
        self.master.blit(self, (self.posX, self.posY))

    def on_loop(self):
        pass

    def _update(self, events):
        events = self.process_events(events)
        class_list = self.__class__.mro()
        class_list.reverse()
        for class_obj in class_list:
            if issubclass(class_obj, Widget):
                class_obj.on_loop(self)
                class_obj.on_render(self)

        for child in self.children:
            if isinstance(child, Widget):
                child._update(events)

    def _on_init(self):
        self.on_init()
        for class_obj in self.__class__.mro():
            if issubclass(class_obj, Widget):
                class_obj.on_init(self)




