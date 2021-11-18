import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font

from buffer import Buffer

class Editor:
    def __init__(self):
        self.TextBuffer = Buffer("")
        self.Message = self.TextBuffer.GetBuffer()
        self.EditorWindow = pyglet.window.Window(500,500,"PyEdit")
        self.Font = self.LoadFont()
        

    def LoadFont(self):
        font.add_directory('fonts/')
        return font.load('Consolas',12)

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)
        label = pyglet.text.Label(self.Message, font_name=self.Font, font_size=12, 
                                  x=1, y=self.EditorWindow.height-12,
                                  anchor_x='left', anchor_y='baseline')
        label.color = (0,0,0,255)

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
                if(modifiers == 0):
                    self.TextBuffer.TypeIntoBuffer(key._key_names[symbol].lower())
                    label.text = self.TextBuffer.GetBuffer()
                else:
                    self.TextBuffer.TypeIntoBuffer(key._key_names[symbol])
                    label.text = self.TextBuffer.GetBuffer()
        pyglet.app.run()