from random import uniform
from typing import List

import numpy as np
from matplotlib import pyplot as plt

from data_classes.entities.Circle import Circle
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.FileGenerator import FileGenerator
from data_classes.generator.RandomGenerator import RandomGenerator
from data_classes.generator.RandomGeneratorWithoutInput import RandomGeneratorWithoutInput
from solvers.FloatingLine import FloatingLine


class FloatingLineTest:
    def __init__(self):
        min_val, max_val = map(float, input("Enter min and max value of delta separated by whitespace: ").split())
        k = float(input("Enter step k for delta: "))
        self.deltas = list(np.arange(min_val, max_val + k, k))

    def __generate_circles(self, X: float, Y: float, num_circles: int) -> List[Circle]:
        circles: List[Circle] = []
        for _ in range(num_circles):
            x = X
            y = Y
            weight = round(uniform(1, 100), 2)
            circles.append(Circle(x, y, weight))
        return circles

    def test(self):
        execution_time_values = []
        target_func_values = []
        i = 0
        n = len(self.deltas)
        tasks_n = int(input("Enter number of tasks generated per delta: "))
        dimension = int(input("Enter dimension of task: "))
        X, Y = tuple(map(float, input("Enter X,Y separated by whitespace: ").split()))
        R = int(input("Enter R of every circle: "))
        for delta in self.deltas:
            tasks = [GlobalData(X, Y, R, self.__generate_circles(X, Y, dimension)) for _ in range(tasks_n)]
            avg_exec_time = 0
            avg_target_func_values = 0
            for task in tasks:
                solver = FloatingLine(task, delta=delta)
                result = solver.solve()
                avg_exec_time += result.execution_duration / tasks_n
                avg_target_func_values += result.line_weight / tasks_n
            print(f'{i}/{n}')
            execution_time_values.append(avg_exec_time)
            target_func_values.append(avg_target_func_values)
            i += 1
        return execution_time_values, target_func_values

    def plot(self, execution_time_values: List[float], target_func_values: List[float]):
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel('Delta')
        ax1.set_ylabel('Execution Time (s)', color=color)
        ax1.plot(self.deltas, execution_time_values, color=color, label='Execution Time')
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Target Function Value', color=color)
        ax2.plot(self.deltas, target_func_values, color=color, label='Target Function Value')
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.title('Execution Time and Target Function Value vs Delta')
        plt.show()

    def __get_data_from_file(self) -> GlobalData:
        file_generator = FileGenerator()
        return file_generator.get_data()
