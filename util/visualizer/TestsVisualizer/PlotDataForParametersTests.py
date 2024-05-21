import matplotlib.pyplot as plt
from typing import List

class PlotDataForParametersTests:
    def __init__(self, solver_name, parameter_name: str, parameter_values: List[float], accuracy_values: List[float], execution_time_values: List[float]):
        self.parameter_name = parameter_name
        self.parameter_values = parameter_values
        self.accuracy_values = accuracy_values
        self.execution_time_values = execution_time_values
        self.solver_name = solver_name

    def plot(self):
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(self.parameter_values, self.accuracy_values, marker='o', linestyle='-', color='b')
        plt.xlabel(self.parameter_name)
        plt.ylabel('Target function value')
        plt.title(f'Target function value vs {self.parameter_name} ({self.solver_name})')
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(self.parameter_values, self.execution_time_values, marker='o', linestyle='-', color='r')
        plt.xlabel(self.parameter_name)
        plt.ylabel('Execution Time (seconds)')
        plt.title(f'Execution time vs {self.parameter_name} ({self.solver_name})')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

