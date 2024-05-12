from solvers.Solver import Solver
from data_classes.entities.Line import Line
from data_classes.entities.GlobalData import GlobalData


class Bruteforce(Solver):
    def __init__(self, global_data: GlobalData):
        self.global_data = global_data

    @property
    def global_data(self) -> GlobalData:
        return self.global_data

    @global_data.setter
    def global_data(self, value):
        self._global_data = value

    def solve(self) -> Line:
        pass
