from line import Line
from cursor import Cursor

class LineManager:
    def __init__(self):
        self.list_of_lines = []
        self.number_of_lines = 0
        self.cursor = Cursor()
        self.create_new_line()

    def create_new_line(self):
        self.number_of_lines+=1
        new_line = Line(self.number_of_lines, "", 'Courier', 12, 1, 735 - (15 * self.number_of_lines))
        self.list_of_lines.append(new_line)
        
    def write_to_line(self, char):
        pass