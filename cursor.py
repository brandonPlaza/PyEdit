class Cursor():
    def __init__(self):
        self.current_line = 0
        self.current_char = 0
    
    def change_cursor_line(self, direction_value, total_lines):
        if(direction_value>0) and (self.current_line + direction_value < total_lines): 
            self.current_line = total_lines
            return
        if(direction_value<0) and (self.current_line - direction_value < 0): 
            self.current_line = 0
            return
        
        if(direction_value>0): self.current_line+=direction_value
        if(direction_value<0): self.current_line-=direction_value
    
    def move_cursor(self, direction_value, total_line_chars):
        if(direction_value>0) and (self.current_char + direction_value < total_line_chars): 
            self.current_char = total_line_chars-1
            return
        if(direction_value<0) and (self.current_char - direction_value < 0): 
            self.current_char = 0
            return
        
        if(direction_value>0): self.current_char+=direction_value
        if(direction_value<0): self.current_char-=direction_value