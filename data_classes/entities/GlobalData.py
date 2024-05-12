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
