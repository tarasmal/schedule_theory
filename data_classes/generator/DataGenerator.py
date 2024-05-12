from abc import ABC, abstractmethod
from ..entities.GlobalData import *


class DataGenerator(ABC):
    @abstractmethod
    def get_data(self) -> GlobalData:
        pass
