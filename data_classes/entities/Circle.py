class Circle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def __str__(self):
        return f'{self.x}, {self.y}'
