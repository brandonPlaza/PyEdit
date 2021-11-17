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
        label = pyglet.text.Label(self.Message, font_name='Times New Roman', font_size=12, 
                                  x=self.EditorWindow.width//2, y=self.EditorWindow.height//2,
                                  anchor_x='center', anchor_y='center')

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