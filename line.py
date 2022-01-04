from pyglet import text
class Line:
    def __init__(self, line_number, line_text, font_name, font_size, x, y):
        self.line_number = line_number
        self.line_content =  text.Label(line_text, font_name=font_name, font_size=font_size, 
                                  x=x, y=y,
                                  anchor_x='left', anchor_y='baseline')
        self.line_content.color = (0,0,0,255)
        return self

    def update_line_text(self, new_char):
        self.line_content.text = new_char