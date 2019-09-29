from inspect import isfunction
from canvas import Canvas

from event.event import SurfaceEvents

class Widget(Canvas, SurfaceEvents):
    def __init__(self, master, posX, posY, width, height):
        self.master = master
        self.posX = posX
        self.posY = posY
        self.children = []
 
        if master != None and isinstance(master, Widget):
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
        for base in self.__class__.__bases__:
            if issubclass(base, Widget) and base != Widget:
                base._update(self, events)
            elif base == Widget:
                Widget.on_loop(self)
                Widget.on_render(self)


        self.on_loop()
        self.on_render()

        for child in self.children:
            if isinstance(child, Widget):
                child._update(events)


    def _on_init(self):
        self.on_init()
        for base in self.__class__.__bases__:
            if issubclass(base, Widget) and base != Widget:
                base._on_init(self)
            elif base == Widget:
                Widget.on_init(self)



