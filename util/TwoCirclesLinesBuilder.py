import math
from typing import List, Tuple

from data_classes.entities.Circle import Circle
from data_classes.entities.Line.Line import Line
from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Line.VerticalLine import VerticalLine


class TwoCirclesLinesBuilder:
    def __init__(self, circle1: Circle, circle2: Circle, r: float):
        self.circle1 = circle1
        self.circle2 = circle2
        self.r = r

    def find_tangent_lines(self) -> Tuple[AbstractLine, AbstractLine]:
        connective_line: AbstractLine = self.__find_connective_line()
        if isinstance(connective_line, VerticalLine):
            return self.__find_vertical_tangent_lines(connective_line)
        elif isinstance(connective_line, Line):
            return self.__find_tangent_lines(connective_line)

    def __find_connective_line(self) -> AbstractLine:
        x1, y1 = self.circle1.get()
        x2, y2 = self.circle2.get()
        if x1 == x2:
            return VerticalLine(x1)
        k = (y2 - y1) / (x2 - x1)
        b = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)
        return Line(k, b)

    def __find_vertical_tangent_lines(self, connective_line: VerticalLine) -> Tuple[VerticalLine, VerticalLine]:
        line1 = VerticalLine(connective_line.x + self.r)
        line2 = VerticalLine(connective_line.x - self.r)
        return line1, line2

    def __find_tangent_lines(self, connective_line: Line) -> Tuple[Line, Line]:
        shift = self.r * math.sqrt(connective_line.k**2 + 1)
        line1 = Line(connective_line.k, connective_line.b + shift)
        line2 = Line(connective_line.k, connective_line.b - shift)
        return line1, line2
