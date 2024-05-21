from typing import List

from data_classes.entities.Circle import Circle
from data_classes.generator.RandomGenerator import RandomGenerator


class FileWriter:
    def __init__(self, max_x: float, max_y: float, R: float, circles: List[Circle]):
        self.max_x = max_x
        self.max_y = max_y
        self.R = R
        self.circles = circles

    def save_to_file(self, filename: str):
        with open(f"../data/{filename}", 'w') as file:
            file.write(f'{self.max_x}\n')
            file.write(f'{self.max_y}\n')
            file.write(f'{self.R}\n')
            for circle in self.circles:
                file.write(f"{circle.x},{circle.x},{circle.weight}\n")


random_generator = RandomGenerator()
data = random_generator.get_data()
file_writer = FileWriter(*data.get())
file_writer.save_to_file("floating_line_test")
