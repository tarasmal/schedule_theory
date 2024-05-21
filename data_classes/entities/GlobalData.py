from random import uniform
from typing import List
from data_classes.entities.Circle import Circle


class GlobalData:

    def __init__(self, X: float, Y: float, R: float, circles: List[Circle]):
        self.X = X
        self.Y = Y
        self.R = R
        self.circles = circles

    def get(self):
        return self.X, self.Y, self.R, self.circles

    def set_param(self, param_name: str, value: float):
        if param_name == 'X':
            self.X = value
        elif param_name == 'Y':
            self.Y = value
        elif param_name == 'R':
            self.R = value
        elif param_name == 'n':
            self.circles = [Circle(uniform(0, self.X), uniform(0, self.Y),round(uniform(1, 100), 2)) for _ in range(int(value))]
        else:
            raise ValueError(f"Unknown parameter name: {param_name}")
