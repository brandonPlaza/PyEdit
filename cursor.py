class Cursor():
    def __init__(self):
        self.current_line = 0
        self.current_char = 0
    
    def change_cursor_line(self, direction_value, total_lines):
        if(direction_value>0) and (self.current_line + direction_value < total_lines): 
            self.current_line = total_lines
            return
        if(direction_value<0) and (self.current_line - direction_value < 0): 
            self.current_line = 1
            return
        
        if(direction_value>0): 
            self.current_line+=direction_value
        if(direction_value<0): 
            self.current_line-=direction_value
        
        self.current_char = 0
    
    def move_cursor(self, direction_value, total_line_chars):
        if(direction_value>0) and (self.current_char + direction_value < total_line_chars-1): 
            self.current_char = total_line_chars-1
            return
        if(direction_value<0) and (self.current_char - direction_value < 0): 
            self.current_char = 0
            return
        
        if(direction_value>0): self.current_char+=direction_value
        if(direction_value<0): self.current_char-=direction_value
        
    def get_cursor_location(self):
        return (self.current_line, self.current_char)
    
    def increment_cursor_char(self):
        self.current_char+=1
        
    def decrement_cursor_char(self):
        self.current_char-=1
        
    def new_cursor_line(self, new_line_num):
        self.current_line = new_line_num
        self.current_char = 0