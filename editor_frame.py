import imp
import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes

from editor_core import EditorCore

class EditorFrame:
    def __init__(self):
        self.window = pyglet.window.Window(850,750,"PyEdit")
        self.core = EditorCore()

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)

        @self.window.event
        def on_draw():
            self.window.clear()
            for new_line in self.core.get_list_of_lines():
                new_line.line_content.draw()
            self.core.line_manager.cursor.shape.draw()
        
        @self.window.event
        def on_key_press(symbol, modifiers):
            print(symbol)
            print(modifiers)
            self.core.process_non_char(symbol)
        
        @self.window.event
        def on_text(text):
            print(text)
            self.core.process_char(text)
            
        pyglet.app.run()