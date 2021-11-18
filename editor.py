import pyglet
from pyglet.window import key
from pyglet.window import mouse

from buffer import Buffer

class Editor:
    def __init__(self):
        self.TextBuffer = Buffer("")
        self.Message = self.TextBuffer.GetBuffer()
        self.EditorWindow = pyglet.window.Window()
    
    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)
        label = pyglet.text.Label(self.Message, font_name='Times New Roman', font_size=12, 
                                  x=self.EditorWindow.width//2-315, y=self.EditorWindow.height-12,
                                  anchor_x='left', anchor_y='baseline')
        label.color = (1,1,1,1)

        @self.EditorWindow.event
        def on_draw():
            self.EditorWindow.clear()
            label.draw()
        
        @self.EditorWindow.event
        def on_key_press(symbol, modifiers):
            if (symbol == key.BACKSPACE):
                self.TextBuffer.Backspace()
                label.text = self.TextBuffer.GetBuffer()

            elif (key._key_names.__contains__(symbol)):
                print(key._key_names[symbol])
                self.TextBuffer.TypeIntoBuffer(key._key_names[symbol])
                label.text = self.TextBuffer.GetBuffer()

        pyglet.app.run()