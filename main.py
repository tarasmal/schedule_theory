from data_classes.generator.DataGenerator import DataGenerator
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.FileGenerator import FileGenerator
from data_classes.generator.RandomGenerator import RandomGenerator
from solvers.Bruteforce import Bruteforce
from solvers.FloatingLine import FloatingLine
from solvers.Greedy import Greedy
from util.visualizer.Visualizer import Visualizer

generator: DataGenerator = RandomGenerator()
global_data: GlobalData = generator.get_data()
solver1 = FloatingLine(global_data)
solver2 = Bruteforce(global_data)
solver3 = Greedy(global_data)
result1 = solver1.solve()
result2 = solver2.solve()
result3 = solver3.solve()
result = [result1, result2, result3]
print(result1)
print(result2)
print(result3)
visualizer = Visualizer(global_data.circles, result, global_data.X, global_data.Y, global_data.R)

