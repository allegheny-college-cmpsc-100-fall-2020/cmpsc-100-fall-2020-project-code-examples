class PC:
    
    def __init__(self, name, hair_color, hair_length, eye, height):
        self.name = name
        self.hair_color = hair_color
        self.hair_length = hair_length
        self.eye = eye
        self.height = height
    
    def __str__(self):
        return f"Your hair {self.hair_length} is color {self.hair_color}; your eyes {self.eye}; your height {self.height}"