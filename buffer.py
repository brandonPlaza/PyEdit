import pyglet
from pyglet.window import key

class Buffer:
    def __init__(self, buffer):
        self.buffer = buffer

    def TypeIntoBuffer(self, character):
        self.buffer += character

    def SpecialKeyPressed(self, character):
        if (character == key.BACKSPACE):
            self.Backspace()
            return True
    
    def GetBuffer(self):
        return self.buffer

    def ClearBuffer(self):
        self.buffer = ""

    def Backspace(self):
        self.buffer = self.buffer[:-1]
    
    # def TypedIntoBuffer(self, keyPressed, modifier):
    #     rawCharacter = key._key_names[keyPressed]
    #     if keyPressed in (key.LSHIFT, key.RSHIFT, key.CAPSLOCK):
    #         return
    #     elif (keyPressed == key.BACKSPACE):
    #         self.Backspace()
    #         return
    #     elif (keyPressed == key.SPACE):
    #         self.Space()
    #         return
    #     self.buffer += self.parser.ParseKey(keyPressed,rawCharacter, self.ForbiddenKeys, modifier)
        
    