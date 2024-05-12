from typing import List, Tuple

from data_classes.entities.Circle import Circle
from data_classes.entities.Line.AbstractLine import AbstractLine
from solvers.Solver import Solver
from data_classes.entities.Line import Line
from data_classes.entities.GlobalData import GlobalData
from util.TwoCirclesLinesBuilder import TwoCirclesLinesBuilder


class Bruteforce(Solver):
    def __init__(self, global_data: GlobalData):
        self._global_data = global_data

    @property
    def global_data(self) -> GlobalData:
        return self._global_data

    @global_data.setter
    def global_data(self, value):
        self._global_data = value

    def solve(self) -> AbstractLine:
        X, Y, R, circles = self.global_data.get()
        circles.sort(key=lambda c: c.weight, reverse=True)
        max_sum = 0
        best_line: AbstractLine = None
        n = len(circles)
        for i in range(n - 1):
            current_line, current_sum = self.__find_sum_for_sector(circles[i], circles[i + 1], R, circles[i + 2:])
            if current_sum > max_sum:
                max_sum = current_sum
                best_line = current_line
        return best_line

    def __find_sum_for_sector(self, circle1: Circle, circle2: Circle, r: float, other_circles: List[Circle]) -> Tuple[AbstractLine, float]:
        sum1, sum2 = circle1.weight,  circle2.weight
        line_builder = TwoCirclesLinesBuilder(circle1, circle2, r)
        line1, line2 = line_builder.find_tangent_lines()
        for circle in other_circles:
            if line1.check_intersection_with_circle(circle, r):
                sum1 += circle.weight
            elif line2.check_intersection_with_circle(circle, r):
                sum2 += circle.weight
        if sum1 >= sum2:
            return line1, sum1
        else:
            return line2, sum2
