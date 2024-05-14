from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData
from solvers.Bruteforce import Bruteforce
from solvers.FloatingLine import FloatingLine

generator: DataGenerator = InputDataGenerator()
global_data: GlobalData = generator.get_data()
solver1 = FloatingLine(global_data)
solver2 = Bruteforce(global_data)
best_line1 = solver1.solve()
best_line2 = solver2.solve()

print(best_line1[0], '\n', best_line1[1], "Nika")
print(best_line2[0], '\n', best_line2[1], "Taras")



