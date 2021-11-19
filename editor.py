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
        self.editorWindow = pyglet.window.Window(850,750,"PyEdit")
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
            if symbol == key.ENTER:
                self.lineManager.CreateNewLine()
                self.cursor["LineNumber"] = self.lineManager.GetCurrentLineNumber()
                self.buffer.AddNewBufferLine()
            elif self.buffer.SpecialKeyPressed(symbol, self.cursor["LineNumber"]):
                self.lineManager.GetLineFromNumber(self.cursor["LineNumber"]).UpdateLineText(self.buffer.GetBuffer(self.cursor["LineNumber"]))

        @self.editorWindow.event
        def on_text(text):
            print(text)
            self.buffer.TypeIntoBuffer(text, self.cursor["LineNumber"])
            self.lineManager.GetLineFromNumber(self.cursor["LineNumber"]).UpdateLineText(self.buffer.GetBuffer(self.cursor["LineNumber"]))

            
        pyglet.app.run()