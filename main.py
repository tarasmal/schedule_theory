from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData

generator: DataGenerator = InputDataGenerator()
global_data: GlobalData = generator.get_data()
X, Y, R, circles = global_data.get()
print(X, Y, R)
for circle in circles:
    print(circle)