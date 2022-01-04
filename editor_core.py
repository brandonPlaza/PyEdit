import pyglet
from pyglet.window import key
from line_manager import LineManager

class EditorCore():
    def __init__(self):
        self.line_manager = LineManager()
        
    
    def process_non_char(self):
        pass
    
    def process_char(self):
        pass