import pyglet
from pyglet.window import key
from line_manager import LineManager

class EditorCore():
    def __init__(self):
        self.line_manager = LineManager()
    
    def process_non_char(self, key_pressed):
        if(key_pressed == key.ENTER):
            self.line_manager.set_enter_flag(True)
            self.line_manager.create_new_line()
        if(key_pressed == key.BACKSPACE):
            self.line_manager.delete_character()
    
    def process_char(self, character):
        if(self.line_manager.enter_flag):
            self.line_manager.set_enter_flag(False)
            return
        self.line_manager.write_to_line(character)
        
    def get_list_of_lines(self):
        return self.line_manager.list_of_lines