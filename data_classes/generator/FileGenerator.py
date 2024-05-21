from pathlib import Path
from typing import List

from data_classes.entities.Circle import Circle
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.DataGenerator import DataGenerator


class FileGenerator(DataGenerator):
    def get_data(self) -> GlobalData:
        filename = input("Enter filename: ")
        lines = self.__get_file_lines(filename)
        X = float(lines[0].strip())
        Y = float(lines[1].strip())
        R = float(lines[2].strip())
        circles = []

        for line in lines[3:]:
            c_x, c_y, c_w = map(float, line.strip().split(','))
            circles.append(Circle(c_x, c_y, c_w))
        return GlobalData(X, Y, R, circles)

    def __get_file_lines(self, filename="data4.txt") -> List[str]:
        current_dir = Path(__file__).parent
        file_path = current_dir / '../../data' / filename
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
