from typing import Tuple, List

from data_classes.entities.Circle import Circle
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.DataGenerator import DataGenerator
from random import uniform


class RandomGenerator(DataGenerator):
    def get_data(self) -> GlobalData:
        X, Y = self.__generateXY()
        R = self.__generateR()
        circles = self.__generate_circles(X, Y)
        return GlobalData(X, Y, R, circles)

    def __generateXY(self) -> Tuple[float, float]:
        x_range = float(input("Enter range of X value: "))
        y_range = float(input("Enter range of Y value: "))
        return uniform(0, x_range), uniform(0, y_range)

    def __generateR(self) -> float:
        a, b = tuple(map(int, input("Enter range of R value separated by whitespace: ").split()))
        return uniform(a, b)

    def __generate_circles(self, X: float, Y: float) -> List[Circle]:
        def generate_circle() -> Circle:
            x = uniform(0, X)
            y = uniform(0, Y)
            weight = round(uniform(weight_range[0], weight_range[1]), 2)
            return Circle(x, y, weight)

        n = int(input("Enter number of circles: "))
        weight_range = tuple(map(float, input("Enter range of weight value separated by whitespace: ").split()))
        circles: List[Circle] = []
        for _ in range(n):
            circles.append(generate_circle())

        return circles
