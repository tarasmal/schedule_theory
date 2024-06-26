from typing import Tuple, List


from data_classes.Result.Result import Result
from data_classes.entities.GlobalData import GlobalData
from data_classes.entities.Line.AbstractLine import AbstractLine
from data_classes.entities.Line.Line import Line
from data_classes.entities.Line.VerticalLine import VerticalLine
from data_classes.entities.Rectangle import Rectangle
from solvers.Solver import Solver
from solvers.timer import timer


class Greedy(Solver):

    def __init__(self, global_data: GlobalData):
        self.name = "Greedy"
        self._global_data = global_data
        self.R = global_data.R
        self.A = (0, 0)
        self.B = (0, 0)
        self.current_circles = []
        self.current_rectangles = []
        self.rectangles_A = []
        self.rectangles_B = []
        self.execution_time = 0
        self.best_line = None
        self.best_sum = 0

    @property
    def global_data(self) -> GlobalData:
        return self._global_data

    @global_data.setter
    def global_data(self, value):
        self._global_data = value

    def get_global_data(self) -> GlobalData:
        pass

    def __build_line(self) -> AbstractLine:
        x1, y1 = self.A
        x2, y2 = self.B
        if x1 == x2:
            return VerticalLine(x1)
        k = (y2 - y1) / (x2 - x1)
        b = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)
        return Line(k, b)

    def solve(self) -> Result:
        result = self.__solve()
        result.execution_duration = self.execution_time
        return result

    @timer
    def __solve(self) -> Result:
        X, Y, R, circles = self.global_data.get()
        init_coordinates = 0, 0, X, Y
        init_rectangle = Rectangle(*init_coordinates)
        self.current_rectangles = init_rectangle.split_rectangle()
        self.current_circles = circles
        rect1, rect2 = self.__get_two_largest_rectangles_by_sum(init_rectangle.split_rectangle())
        self.__recursive_solver(circles, rect1, rect2)
        return Result(self.best_line, self.best_sum, 0, "Greedy")

    def __recursive_solver(self, circles, rect1: Rectangle, rect2: Rectangle):
        self.rectangles_A = rect1.split_rectangle()
        self.rectangles_B = rect2.split_rectangle()
        new_circles = []
        for circle in circles:
            cx = circle.x
            cy = circle.y
            for i in range(len(self.rectangles_A)):
                child_rect_A = self.rectangles_A[i]
                child_rect_B = self.rectangles_B[i]
                if self.__check_circle_in_rectangle(cx, cy, self.R, *child_rect_A.get_attributes()):
                    child_rect_A.sum += circle.weight
                    new_circles.append(circle)

                if self.__check_circle_in_rectangle(cx, cy, self.R, *child_rect_B.get_attributes()):
                    child_rect_B.sum += circle.weight
                    new_circles.append(circle)

        rect1 = self.__get_largest_rectangle(self.rectangles_A)
        rect2 = self.__get_largest_rectangle(self.rectangles_B)
        self.A = rect1.get_center_coordinates()
        self.B = rect2.get_center_coordinates()

        current_line = self.__build_line()
        current_sum = self.get_weight_of_line(current_line)
        if current_sum > self.best_sum:
            self.best_line = current_line
            self.best_sum = current_sum
        if rect1.get_diagonal_length() > 2 * self.R:

            self.__recursive_solver(new_circles, rect1, rect2)

    def __get_largest_rectangle(self, rectangles: List[Rectangle]):
        return max(rectangles, key=lambda x: x.sum)

    def __get_two_largest_rectangles_by_sum(self, rectangles: List[Rectangle]) -> Tuple[Rectangle, Rectangle]:
        sorted_rectangles = sorted(rectangles, key=lambda x: x.sum, reverse=True)
        return sorted_rectangles[0], sorted_rectangles[1]

    def __check_circle_in_rectangle(self, cx, cy, r, x1, y1, x2, y2) -> bool:
        fully_inside = (x1 + r <= cx <= x2 - r) and (y1 + r <= cy <= y2 - r)
        partially_inside = (x1 - r <= cx <= x2 + r) and (y1 - r <= cy <= y2 + r)
        return fully_inside or partially_inside

    def get_weight_of_line(self, line: AbstractLine):
        result = 0
        for circle in self.global_data.circles:
            if line.check_intersection_with_circle(circle, self.R):
                result += circle.weight
        return result