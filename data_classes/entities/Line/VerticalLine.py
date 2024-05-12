from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Circle import Circle


class VerticalLine(AbstractLine):
    def __init__(self, x: float):
        self.x = x

    def get(self):
        return self.x

    def check_intersection_with_circle(self, circle: Circle, r: float) -> bool:
        distance = abs(self.x - circle.x)
        return True if distance <= r else False

    def __str__(self):
        return f'x = {self.x}'
