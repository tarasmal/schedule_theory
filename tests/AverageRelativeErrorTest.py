from typing import List

from data_classes.Result.Result import Result
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.RandomGeneratorWithoutInput import RandomGeneratorWithoutInput
from solvers.Bruteforce import Bruteforce
from solvers.FloatingLine import FloatingLine
from solvers.Greedy import Greedy


class AverageRelativeErrorTest:
    def __init__(self):
        self.errors = {
            "Bruteforce": 0,
            "Floating line": 0,
            "Greedy": 0
        }
        n_min, n_max = tuple(map(int, (input("Enter n_min, n_max separated by whitespace: ").split())))
        self.n_min = n_min
        self.n_max = n_max
        self.average_errors = {
            "Bruteforce": [],
            "Floating line": [],
            "Greedy": []
        }
        self.iterations = int(input("Enter number of generated tasks per n: "))
        self.n_range = [n for n in range(self.n_min, self.n_max + 1)]

    def test(self):
        i = 0
        for n in self.n_range:
            print(f'{100 * i / (self.n_max + 1 - self.n_min)}%')
            for iteration in range(1, self.iterations + 1):
                data = self.__get_data(n)
                solver1 = FloatingLine(data)
                solver2 = Bruteforce(data)
                solver3 = Greedy(data)
                results = [solver1.solve(), solver2.solve(), solver3.solve()]
                self.__get_average_error_on_iteration(results, iteration)
            for key in self.errors:
                self.average_errors[key].append(self.errors[key])
            self.reset_errors()
            i += 1

    def __get_data(self, n) -> GlobalData:
        generator = RandomGeneratorWithoutInput(n)
        return generator.get_data()

    def __get_average_error_on_iteration(self, results: List[Result], iteration):
        max_result = max(results, key=lambda x: x.line_weight).line_weight
        for res in results:
            line_weight = res.line_weight
            error = 1 - line_weight / max_result
            avg_error = (self.errors[res.solver_name] * (iteration - 1) + error) / iteration
            self.errors[res.solver_name] = avg_error

    def reset_errors(self):
        self.errors["Bruteforce"] = 0
        self.errors["Floating line"] = 0
        self.errors["Greedy"] = 0

# average_test = AverageRelativeErrorTest()
# print(average_test.test())
