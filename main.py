from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData
from solvers.Bruteforce import Bruteforce

generator: DataGenerator = InputDataGenerator()
global_data: GlobalData = generator.get_data()
solver = Bruteforce(global_data)
best_line = solver.solve()
print(best_line)



