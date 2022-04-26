from pyglet import text
class Line():
    def __init__(self, line_number):
        self.line_number = line_number
        self.line_content = None
        self.buffer = ""
    
    def inject_new_line(self, line_text, font_name, font_size, x, y):
        self.buffer = line_text
        self.line_content =  text.Label(self.buffer, font_name=font_name, font_size=font_size, 
                                  x=x, y=y,
                                  anchor_x='left', anchor_y='baseline')
        self.line_content.color = (0,0,0,255)
        return self.line_content
    
    def update_line_text(self, new_char):
        self.buffer += new_char
        self.line_content.text = self.buffer

    def character_deleted(self,character_to_delete):
        new_buffer = ""
        for character in range(len(self.buffer)):
            if(character != character_to_delete):
                new_buffer+=self.buffer[character]
        self.buffer = new_buffer
        self.line_content.text = self.buffer
    
    def get_line_text(self):
        return self.buffer