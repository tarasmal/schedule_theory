from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData
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

visualizer = Visualizer(global_data.circles, [line1, line2], global_data.X, global_data.Y, global_data.R)
visualizer.draw()

