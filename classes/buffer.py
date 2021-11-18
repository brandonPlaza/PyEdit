class Buffer:
    def __init__(self, buffer):
        self.buffer = buffer
    
    def TypeIntoBuffer(self, newChar):
        self.buffer += newChar
    
    def GetBuffer(self):
        return self.buffer

    def ClearBuffer(self):
        self.buffer = ""

    def Backspace(self):
        self.buffer = self.buffer[:-1]

    def Space(self):
        self.buffer += " "