from abc import ABC, abstractmethod
from data_classes.entities.Line import Line
from data_classes.entities.GlobalData import GlobalData


class Solver(ABC):
    @property
    @abstractmethod
    def global_data(self) -> GlobalData:
        pass

    @abstractmethod
    def solve(self) -> Line:
        pass
