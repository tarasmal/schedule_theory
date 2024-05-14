from typing import Tuple

from data_classes.entities.GlobalData import GlobalData
from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Line.Line import Line
from data_classes.entities.Line.VerticalLine import VerticalLine
from solvers.Solver import Solver
from math import *


class FloatingLine(Solver):
    def __init__(self, global_data: GlobalData):
        self._global_data = global_data
        self.angle = 0
        self.delta = 0.001

    @property
    def global_data(self) -> GlobalData:
        return self._global_data

    @global_data.setter
    def global_data(self, value):
        self._global_data = value

    def solve(self) -> Tuple[AbstractLine, float]:
        X, Y, R, circles = self.global_data.get()
        max_sum = 0
        best_line = None
        line = self.__get_starting_line(Y)
        while self.angle <= 180:
            current_sum = 0
            for circle in circles:
                if line.check_intersection_with_circle(circle, R):
                    current_sum += circle.weight
            if current_sum > max_sum:
                max_sum = current_sum
                best_line = line
            self.angle += self.delta
            line = self.__get_rotated_line(X, Y, self.angle)

        return best_line, max_sum

    def __get_rotated_line(self, X, Y, new_angle) -> AbstractLine:
        if 90 - self.delta <= new_angle <= 90 + self.delta:
            return VerticalLine(X / 2)
        k = tan(radians(new_angle))
        b = Y / 2 - k * X / 2
        return Line(k, b)

    def __get_starting_line(self, Y):
        return Line(0, Y / 2)
