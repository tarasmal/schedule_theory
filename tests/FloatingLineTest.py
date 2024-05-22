from typing import List

import numpy as np
from matplotlib import pyplot as plt

from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.FileGenerator import FileGenerator
from solvers.FloatingLine import FloatingLine


class FloatingLineTest:
    def __init__(self):
        min_val, max_val = map(float, input("Enter min and max value of delta separated by whitespace: ").split())
        k = float(input("Enter step k for delta: "))
        self.deltas = list(np.arange(min_val, max_val + k, k))
        self.data = self.__get_data_from_file()

    def test(self):
        execution_time_values = []
        target_func_values = []
        i = 0
        n = len(self.deltas)
        for delta in self.deltas:
            print(f'{i}/{n}')
            solver = FloatingLine(self.data, delta=delta)
            result = solver.solve()
            execution_time_values.append(result.execution_duration)
            target_func_values.append(result.line_weight)
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


a = FloatingLineTest()
execution_time_values, target_func_values = a.test()
a.plot(execution_time_values, target_func_values)