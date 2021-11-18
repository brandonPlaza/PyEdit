import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font

from buffer import Buffer

class Editor:
    def __init__(self):
        self.buffer = Buffer("")
        self.Message = self.buffer.GetBuffer()
        self.editorWindow = pyglet.window.Window(500,500,"PyEdit")

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)
        label = pyglet.text.Label(self.Message, font_name='Courier', font_size=12, 
                                  x=1, y=self.editorWindow.height-15,
                                  anchor_x='left', anchor_y='baseline')
        label.color = (0,0,0,255)

        @self.editorWindow.event
        def on_draw():
            self.editorWindow.clear()
            label.draw()
        
        @self.editorWindow.event
        def on_key_press(symbol, modifiers):
            self.buffer.SpecialKeyPressed(symbol)
            label.text = self.buffer.GetBuffer()

        @self.editorWindow.event
        def on_text(text):
            self.buffer.TypeIntoBuffer(text)
            label.text = self.buffer.GetBuffer()
            
        pyglet.app.run()