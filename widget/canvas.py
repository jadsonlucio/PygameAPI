from pygame import Surface

class Canvas(Surface):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__((width, height))
    
    

        