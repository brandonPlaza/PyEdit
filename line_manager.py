from line import Line

class LineManager:
    def __init__(self):
        self.listOfLines = []
        self.numberOfLines = 0
        self.CreateNewLine()

    def CreateNewLine(self):
        self.numberOfLines+=1
        newLine = Line(self.numberOfLines)
        newLine.CreateLine("", 'Courier', 12, 1, 735 - (15 * self.numberOfLines))
        self.listOfLines.append(newLine)
        

    def GetCurrentLineNumber(self):
        return self.numberOfLines

    def GetLineFromNumber(self, lineNum):
        return self.listOfLines[lineNum-1]


    

    