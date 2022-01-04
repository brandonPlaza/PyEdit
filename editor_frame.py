import pyglet
from pyglet.window import key
from pyglet.window import mouse

class EditorFrame:
    def __init__(self):
        self.window = pyglet.window.Window(850,750,"PyEdit")

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)

        @self.window.event
        def on_draw():
            self.window.clear()
            
        pyglet.app.run()