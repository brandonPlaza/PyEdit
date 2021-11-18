import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font

from buffer import Buffer

from line_manager import LineManager

class Editor:
    def __init__(self):
        self.buffer = Buffer("")
        self.lineManager = LineManager()
        self.Message = self.buffer.GetBuffer()
        self.editorWindow = pyglet.window.Window(500,500,"PyEdit")
        self.cursor = {"LineNumber" : self.lineManager.GetCurrentLineNumber(), "CharacterNumber" : 0}

    def run(self):
        pyglet.gl.glClearColor(1,1,1,1)
        @self.editorWindow.event
        def on_draw():
            self.editorWindow.clear()
            for new_line in self.lineManager.listOfLines:
                new_line.lineContent.draw()
        
        @self.editorWindow.event
        def on_key_press(symbol, modifiers):
            if self.buffer.SpecialKeyPressed(symbol):
                self.lineManager.GetLineFromNumber(self.cursor["LineNumber"]).UpdateLineText(self.buffer.GetBuffer())

        @self.editorWindow.event
        def on_text(text):
            self.buffer.TypeIntoBuffer(text)
            self.lineManager.GetLineFromNumber(self.cursor["LineNumber"]).UpdateLineText(self.buffer.GetBuffer())

            
        pyglet.app.run()