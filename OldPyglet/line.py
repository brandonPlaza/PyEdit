from pyglet import text
class Line:

    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
        self.lineContent = None

    def CreateLine(self, lineText, fontName, fontSize, x, y):
        self.lineContent =  text.Label(lineText, font_name=fontName, font_size=fontSize, 
                                  x=x, y=y,
                                  anchor_x='left', anchor_y='baseline')
        self.lineContent.color = (0,0,0,255)
        return self.lineContent

    def UpdateLineText(self, newText):
        self.lineContent.text = newText
        
    # def UpdateLineFont(self):
    #     pass
    # def UpdateLineFontSize(self):
    #     pass