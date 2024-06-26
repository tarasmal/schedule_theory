class Circle:
    def __init__(self, x: float, y: float, weight: float):
        self.x = x
        self.y = y
        self.weight = weight

    def get(self):
        return self.x, self.y

    def __str__(self):
        return f'x={self.x}, y={self.y}, weight={self.weight}'
