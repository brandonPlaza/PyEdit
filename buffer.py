import pyglet
from pyglet.window import key

from character_parser import Parser

class Buffer:
    def __init__(self, buffer):
        self.lines = []
        self.buffer = buffer
        self.ForbiddenKeys = {key.LCTRL, key.RCTRL, key.LOPTION, key.ROPTION, key.UP, key.DOWN, key.LEFT, key.RIGHT,
                              key.TAB, key.LCOMMAND, key.RCOMMAND}
        self.parser = Parser()
    
    def GenerateSingleLine(self, offset):
        # return pyglet.text.Label("", font_name='Consolas', font_size=12, 
        #                           x=1, y=488-offset,
        #                           anchor_x='left', anchor_y='baseline')
        pass

    def TypedIntoBuffer(self, keyPressed, modifier):
        rawCharacter = key._key_names[keyPressed]
        if keyPressed in (key.LSHIFT, key.RSHIFT, key.CAPSLOCK):
            return
        elif (keyPressed == key.BACKSPACE):
            self.Backspace()
            return
        elif (keyPressed == key.SPACE):
            self.Space()
            return
        self.buffer += self.parser.ParseKey(keyPressed,rawCharacter, self.ForbiddenKeys, modifier)
        
    def GetBuffer(self):
        return self.buffer

    def ClearBuffer(self):
        self.buffer = ""

    def Backspace(self):
        self.buffer = self.buffer[:-1]

    def Space(self):
        self.buffer += " "