import time
from typing import List, Tuple

from data_classes.Result.Result import Result
from data_classes.entities.Circle import Circle
from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Line.VerticalLine import VerticalLine
from solvers.Solver import Solver
from data_classes.entities.GlobalData import GlobalData
from solvers.timer import timer
from util.TwoCirclesLinesBuilder import TwoCirclesLinesBuilder


class Bruteforce(Solver):
    def __init__(self, global_data: GlobalData):
        self.name = "Bruteforce"
        self._global_data = global_data
        self.execution_time = 0

    @property
    def global_data(self) -> GlobalData:
        return self._global_data

    @global_data.setter
    def global_data(self, value):
        self._global_data = value

    def solve(self) -> Result:
        result = self.__solve()
        result.execution_duration = self.execution_time
        return result

    @timer
    def __solve(self) -> Result:
        X, Y, R, circles = self.global_data.get()
        if len(circles) == 1:
            circle = circles[0]
            return Result(VerticalLine(circle.x), circle.weight, 0, "Bruteforce")

        circles.sort(key=lambda c: c.weight, reverse=True)
        max_sum = 0
        best_line = None
        n = len(circles)
        for i in range(n - 1):
            current_line, current_sum = self.__find_sum_for_sector(circles[i], circles[i + 1], R, circles[i + 2:])
            if current_sum > max_sum:
                max_sum = current_sum
                best_line = current_line

        return Result(best_line, max_sum, 0, "Bruteforce")

    def __find_sum_for_sector(self, circle1: Circle, circle2: Circle, r: float, other_circles: List[Circle]) -> Tuple[
        AbstractLine, float]:
        sum1 = circle1.weight + circle2.weight
        sum2 = circle1.weight + circle2.weight
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

    def set_execution_time(self, execution_time: float):
        self.execution_time = execution_time
