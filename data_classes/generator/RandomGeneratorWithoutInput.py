from random import uniform, randint
from typing import Tuple, List

from data_classes.entities.Circle import Circle
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.DataGenerator import DataGenerator


class RandomGeneratorWithoutInput(DataGenerator):
    def __init__(self, n):
        self.x_range = self.__generate_range(0, 1000)
        self.y_range = self.__generate_range(0, 1000)
        self.r_range = self.__generate_range(1, 10)
        self.weight_range = self.__generate_range(1, 1000)
        self.num_circles = n

    def __generate_range(self, min_val: float, max_val: float) -> Tuple[float, float]:
        start = uniform(min_val, max_val / 2)
        end = uniform(max_val / 2, max_val)
        return start, end

    def get_data(self) -> GlobalData:
        X, Y = self.__generateXY()
        R = self.__generateR()
        circles = self.__generate_circles(X, Y)
        return GlobalData(X, Y, R, circles)

    def __generateXY(self) -> Tuple[float, float]:
        return uniform(*self.x_range), uniform(*self.y_range)

    def __generateR(self) -> float:
        return uniform(*self.r_range)

    def __generate_circles(self, X: float, Y: float) -> List[Circle]:
        circles: List[Circle] = []
        for _ in range(self.num_circles):
            x = uniform(0, X)
            y = uniform(0, Y)
            weight = round(uniform(*self.weight_range), 2)
            circles.append(Circle(x, y, weight))
        return circles
