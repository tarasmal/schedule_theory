import matplotlib.pyplot as plt

from tests.AverageRelativeErrorTest import AverageRelativeErrorTest


class PlotDataForAverageErrorTest:
    def __init__(self, average_errors: dict, n_range):
        self.average_errors = average_errors
        self.n_range = n_range

    def plot(self):
        plt.figure(figsize=(10, 6))
        for solver_name, errors in self.average_errors.items():
            plt.plot(self.n_range, errors, label=solver_name)

        plt.xlabel('n')
        plt.ylabel('Average Error')
        plt.title('Average Error vs. n')
        plt.legend()
        plt.grid(True)
        plt.show()

