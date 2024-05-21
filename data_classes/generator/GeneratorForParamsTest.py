from typing import List
from random import uniform

from data_classes.entities.Circle import Circle
from data_classes.entities.GlobalData import GlobalData


class GeneratorForParamsTest:
    def __init__(self, constant_params: dict, test_param: str, test_param_value):
        self.constant_params = constant_params
        self.test_param = test_param
        self.test_param_value = test_param_value
        self.X = self.constant_params.get('X', 0)
        self.Y = self.constant_params.get('Y', 0)
        self.R = self.constant_params.get('R', 1)
        self.n = self.constant_params.get('n', 0)
        self.circles = []

    def get_data(self) -> GlobalData:
        if self.test_param == 'X':
            self.X = self.test_param_value
        elif self.test_param == 'Y':
            self.Y = self.test_param_value
        elif self.test_param == 'R':
            self.R = self.test_param_value
        elif self.test_param == 'n':
            self.n = self.test_param_value

        self.circles = self.__generate_circles(self.X, self.Y, self.n)
        return GlobalData(self.X, self.Y, self.R, self.circles)

    def __generate_circles(self, X: float, Y: float, num_circles: int) -> List[Circle]:
        circles: List[Circle] = []
        for _ in range(num_circles):
            x = X
            y = Y
            weight = round(uniform(1, 100), 2)
            circles.append(Circle(x, y, weight))
        return circles

    def get(self):
        return self.X, self.Y, self.R, self.n, self.circles