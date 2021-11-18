import pyglet
from pyglet.window import key

class Buffer:
    def __init__(self, buffer):
        self.buffer = buffer
        self.ForbiddenKeys = {key.LCTRL, key.RCTRL, key.LOPTION, key.ROPTION, key.UP, key.DOWN, key.LEFT, key.RIGHT,
                              key.TAB, key.LCOMMAND, key.RCOMMAND}
    
    def TypeIntoBuffer(self, newChar):
        for number in range(0,10):
            if(newChar.__contains__(str(number))):
                self.buffer += str(number)
                return
        self.buffer += newChar
        
    
    def GetBuffer(self):
        return self.buffer

    def ClearBuffer(self):
        self.buffer = ""

    def Backspace(self):
        self.buffer = self.buffer[:-1]

    def Space(self):
        self.buffer += " "