from abc import ABC, abstractmethod
from typing import Tuple

from data_classes.Result.Result import Result
from data_classes.entities.GlobalData import GlobalData
from data_classes.entities.Line.AbstractLine import AbstractLine


class Solver(ABC):
    @property
    @abstractmethod
    def global_data(self) -> GlobalData:
        pass

    @abstractmethod
    def solve(self) -> Result:
        pass
