import pyglet
from pyglet.window import key

class Buffer:
    def __init__(self, buffer):
        #self.buffer = buffer
        self.listOfBuffersForEachLine = [buffer]

    def TypeIntoBuffer(self, character, bufferLine):
        self.listOfBuffersForEachLine[bufferLine-1] += character

    def SpecialKeyPressed(self, character, bufferLine):
        if (character == key.BACKSPACE):
            self.Backspace(bufferLine-1)
            return True
    
    def GetBuffer(self,bufferLine):
        return self.listOfBuffersForEachLine[bufferLine-1]
    
    def AddNewBufferLine(self):
        self.listOfBuffersForEachLine.append("")

    def Backspace(self,bufferLine):
        self.listOfBuffersForEachLine[bufferLine] = self.listOfBuffersForEachLine[bufferLine][:-1]
    
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
        
    