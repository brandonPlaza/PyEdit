from line import Line
from cursor import Cursor

class LineManager:
    def __init__(self):

        self.list_of_lines = []

        self.number_of_lines = 0

        self.cursor = Cursor()

        self.enter_flag = False

        self.create_new_line()

    def create_new_line(self):

        self.number_of_lines+=1

        new_line = Line(self.number_of_lines)

        new_line.inject_new_line("", 'Courier', 12, 1, 735 - (15 * self.number_of_lines))

        self.list_of_lines.append(new_line)

        self.cursor.new_cursor_line(self.number_of_lines)
        
    def write_to_line(self, typed_char):
        cursor_location = self.cursor.get_cursor_data()

        self.list_of_lines[cursor_location.current_line-1].update_line_text(typed_char)

        self.cursor.increment_cursor_char()

    def delete_character(self):
        cursor_location = self.cursor.get_cursor_data()

        self.list_of_lines[cursor_location.current_line-1].character_deleted(cursor_location.current_char-1)
        if cursor_location.current_char>0:
            self.cursor.decrement_cursor_char()
        


        
    def set_enter_flag(self, bool_val):
        self.enter_flag = bool_val
        