from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.GeneratorForParamsTest import GeneratorForParamsTest
from solvers.Bruteforce import Bruteforce
from solvers.Greedy import Greedy
from util.visualizer.TestsVisualizer.PlotDataForParametersTests import PlotDataForParametersTests


class TaskParamsTest:
    def __init__(self, solverReference):
        self.solver = solverReference

    def test_x(self):
        constant_params = {
            "Y": 1000,
            "R": 3,
            "n": 1000
        }
        min_val, max_val = tuple(map(int, input("Enter range of x separated by whitespace: ").split()))
        data = GeneratorForParamsTest(constant_params,  test_param='X', test_param_value=0).get_data()
        to_plot = self.test("X", min_val, max_val, data)
        to_plot.plot()

    def test_y(self):
        constant_params = {
            "X": 1000,
            "R": 3,
            "n": 1000
        }
        min_val, max_val = tuple(map(int, input("Enter range of x separated by whitespace: ").split()))
        data = GeneratorForParamsTest(constant_params, test_param='Y', test_param_value=0).get_data()
        to_plot = self.test("X", min_val, max_val, data)
        to_plot.plot()

    def test_r(self):
        constant_params = {
            "X": 1000,
            "Y": 1000,
            "n": 1000
        }
        min_val, max_val = tuple(map(int, input("Enter range of x separated by whitespace: ").split()))
        data = GeneratorForParamsTest(constant_params, test_param='R', test_param_value=0).get_data()
        to_plot = self.test("X", min_val, max_val, data)
        to_plot.plot()

    def test_n(self):
        constant_params = {
            "Y": 1000,
            "R": 10,
            "X": 1000
        }
        min_val, max_val = tuple(map(int, input("Enter range of n separated by whitespace: ").split()))
        data = GeneratorForParamsTest(constant_params, test_param='n', test_param_value=0).get_data()
        to_plot = self.test("n", min_val, max_val, data)
        to_plot.plot()

    def test(self, parameter_name, parameter_min_value, parameter_max_value, data: GlobalData) -> PlotDataForParametersTests:
        target_function_value = []
        execution_duration = []
        parameter_values = [val for val in range(parameter_min_value, parameter_max_value + 1)]
        solver = None
        for val in parameter_values:
            data.set_param(parameter_name, val)
            print(f"Testing {parameter_name}={val}")
            solver = self.solver(data)
            result = solver.solve()
            target_function_value.append(result.line_weight)
            execution_duration.append(result.execution_duration)
        return PlotDataForParametersTests(solver.name, parameter_name, parameter_values, accuracy_values=target_function_value,
                                          execution_time_values=execution_duration)


test = TaskParamsTest(Greedy)
test.test_n()
