from typing import List

import numpy as np

from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Circle import Circle


class Line(AbstractLine):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def get(self):
        return self.k, self.b

    def __str__(self):
        return f'y = {self.k}x + {self.b}'

    def __solve_line_circle_equations_system(self, circle: Circle, r: float) -> List:
        x, y = circle.get()
        A = 1 + self.k ** 2
        B = 2 * self.k * (x - self.b) - 2 * x
        C = self.b ** 2 + (x - self.b) ** 2 - r ** 2
        discriminant = B ** 2 - 4 * A * C
        result = []
        if discriminant > 0:
            x1 = (-B + np.sqrt(discriminant)) / (2 * A)
            x2 = (-B - np.sqrt(discriminant)) / (2 * A)
            y1 = self.k * x1 + x
            y2 = self.k * x2 + x
            result = [(x1, y1), (x2, y2)]
        elif discriminant == 0:
            x = -B / (2 * A)
            y = self.k * x + x
            result = [(x, y)]
        return result

    def check_intersection_with_circle(self, circle: Circle, r: float) -> bool:
        return True if self.__solve_line_circle_equations_system(circle, r) else False
