from data_classes.entities.Line.PlottedLine import PlottedLine
from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData
from data_classes.generator.RandomGenerator import RandomGenerator
from solvers.Bruteforce import Bruteforce
from solvers.FloatingLine import FloatingLine
from util.visualizer.Visualizer import Visualizer

generator: DataGenerator = InputDataGenerator()
global_data: GlobalData = generator.get_data()
solver1 = FloatingLine(global_data)
solver2 = Bruteforce(global_data)
line1, max_sum1 = solver1.solve()
line2, max_sum2 = solver2.solve()
print(line1, max_sum1, "Floating line")
print(line2, max_sum2, "Bruteforce")

lines = [PlottedLine(line1, "FloatingLine", "red"), PlottedLine(line2, "Bruteforce", "blue")]
visualizer = Visualizer(global_data.circles, lines, global_data.X, global_data.Y, global_data.R)
visualizer.draw()

