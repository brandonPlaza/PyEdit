from line import Line

class LineManager:
    def __init__(self):
        self.listOfLines = []
        self.numberOfLines = 0
        self.CreateNewLine()

    def CreateNewLine(self):
        newLine = Line(self.numberOfLines)
        newLine.CreateLine("", 'Courier', 12, 1, 480)
        self.listOfLines.append(newLine)
        self.numberOfLines+=1

    def GetCurrentLineNumber(self):
        return self.numberOfLines

    def GetLineFromNumber(self, lineNum):
        return self.listOfLines[lineNum-1]


    

    