from typing import List, Tuple
from math import sqrt

from data_classes.entities.Circle import Circle


class Rectangle:
    def __init__(self, x1, y1, x2, y2, sum=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.sum = 0
        self.circles = []

    def split_rectangle(self):
        mid_x = (self.x1 + self.x2) / 2
        mid_y = (self.y1 + self.y2) / 2
        coordinates = [
            (self.x1, self.y1, mid_x, mid_y),
            (self.x1, mid_y, mid_x, self.y2),
            (mid_x, self.y1, self.x2, mid_y),
            (mid_x, mid_y, self.x2, self.y2)
        ]
        rectangles = [Rectangle(*coord) for coord in coordinates]
        return rectangles

    def get_attributes(self):
        return self.x1, self.y1, self.x2, self.y2

    def get_diagonal_length(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return sqrt(width ** 2 + height ** 2)
    def get_center_coordinates(self) -> Tuple[float, float]:
        x = (self.x2 + self.x1) / 2
        y = (self.y2 + self.y1) / 2
        return x, y

    def get_sum(self, circles: List[Circle], r: float):
        for circle in circles:
            if self.__check_if_circle_in_rectangle(circle.x, circle.y, r):
                self.sum += 1
                self.circles.append(circle)
        return self.sum

    def __check_if_circle_in_rectangle(self, cx, cy, r) -> bool:
        fully_inside = (self.x1 + r <= cx <= self.x2 - r) and (self.y1 + r <= cy <= self.y2 - r)
        partially_inside = (self.x1 - r <= cx <= self.x2 + r) and (self.y1 - r <= cy <= self.y2 + r)
        return fully_inside or partially_inside

    def __str__(self):
        return f'({self.x1};{self.y1}), ({self.x2};{self.y2}) - {self.sum}'

