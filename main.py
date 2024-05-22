from data_classes.generator.DataGenerator import DataGenerator
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.FileGenerator import FileGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.generator.RandomGenerator import RandomGenerator
from solvers.Bruteforce import Bruteforce
from solvers.FloatingLine import FloatingLine
from solvers.Greedy import Greedy
from solvers.Solver import Solver
from tests.AverageRelativeErrorTest import AverageRelativeErrorTest
from tests.TaskParamsTest import TaskParamsTest
from util.visualizer.TestsVisualizer.PlotDataForAverageErrorTest import PlotDataForAverageErrorTest
from util.visualizer.Visualizer import Visualizer

class Main:
    def __init__(self):
        self.data: GlobalData = None
        self.tests = TestsOptionsChooser()

    def menu(self):
        options = {1: self.solve_by_one, 2: self.__solve_by_all, 3: TestsOptionsChooser.task_parameter_test, 4: TestsOptionsChooser.average_error_test}
        option = -1
        while option != 0:
            option = int(input("0 - Exit\n1 - solve by Bruteforce/FloatingLine/Greedy\n2 - solve with all algorithms\n3 - task parameter test\n4 - average_error_test\n"))
            if option in range(1, len(options.keys()) + 1):
                options[option]()

    def __solve_by_all(self):
        self.__choose_data_generator()
        solvers = [Bruteforce(self.data), FloatingLine(self.data, with_setting_of_delta=True), Greedy(self.data)]
        results = [solver.solve() for solver in solvers]
        for res in results:
            print(res)
        with_plot = int(input("Draw plot of results? (0 - No, 1 - Yes):"))
        Visualizer(self.data.circles, results, self.data.X, self.data.Y, self.data.R) if with_plot == 1 else None


    def __choose_data_generator(self):
        generators = {1: RandomGenerator, 2: FileGenerator, 3: InputDataGenerator}
        option = int(input("Choose solver (1 - Random generator, 2 - File generator 3 - Input generator): "))
        self.__option_restriction(option, 1, 3)
        self.data = generators[option]().get_data()

    def solve_by_one(self):
        solvers = {1: self.greedy_solve, 2: self.floating_line_solve, 3: self.bruteforce_solve}
        option = int(input("Choose solver (1 - Greedy, 2 - Floating line, 3 - Bruteforce): "))
        self.__option_restriction(option, 1, 3)
        self.__choose_data_generator()
        solvers[option]()

    def greedy_solve(self):
        self.__solve_by_one(Greedy)

    def floating_line_solve(self):
        self.__solve_by_one(FloatingLine)

    def bruteforce_solve(self):
        self.__solve_by_one(Bruteforce)

    def __solve_by_one(self, solver: Solver):
        if isinstance(solver, FloatingLine):
            s = solver(self.data, with_setting_of_delta=True)
        else:
            s = solver(self.data)
        result = s.solve()
        print(result)
        with_plot = int(input("Draw plot of results? (0 - No, 1 - True):"))
        Visualizer(self.data.circles, [result], self.data.X, self.data.Y, self.data.R) if with_plot == 1 else None

    def __option_restriction(self, val, min_val, max_val):
        if not min_val <= val <= max_val:
            raise ValueError(f"Choose value in range from {min_val} to {max_val}")

class TestsOptionsChooser:
    @staticmethod
    def task_parameter_test():
        print("Task parameters test")
        option = None
        while option != 0:
            option = int(input("0 - exit\n1 - test: "))
            if option == 1:
                TaskParamsTest().test()

    @staticmethod
    def average_error_test():
        print("Average error test")
        option = None
        while option != 0:
            option = int(input("0 - exit\n1 - test: "))
            if option != 0:
                test = AverageRelativeErrorTest()
                test.test()
                plotter = PlotDataForAverageErrorTest(test.average_errors, test.n_range)
                plotter.plot()


main = Main()
main.menu()

