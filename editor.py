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
        self.Font = self.LoadFont()
        

    def LoadFont(self):
        font.add_directory('fonts/')
        return font.load('Consolas',12)

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)
        label = pyglet.text.Label(self.Message, font_name=self.Font, font_size=12, 
                                  x=1, y=self.editorWindow.height-13,
                                  anchor_x='left', anchor_y='baseline')
        label.color = (0,0,0,255)

        @self.editorWindow.event
        def on_draw():
            self.editorWindow.clear()
            label.draw()
        
        @self.editorWindow.event
        def on_key_press(symbol, modifiers):
            self.buffer.TypedIntoBuffer(symbol, modifiers)
            label.text = self.buffer.GetBuffer()
            
        pyglet.app.run()