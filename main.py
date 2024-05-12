from data_classes.generator.DataGenerator import DataGenerator
from data_classes.generator.InputDataGenerator import InputDataGenerator
from data_classes.entities.GlobalData import GlobalData
from util.TwoCirclesLinesBuilder import TwoCirclesLinesBuilder

generator: DataGenerator = InputDataGenerator()
global_data: GlobalData = generator.get_data()
X, Y, R, circles = global_data.get()
circle1, circle2 = circles
lines_builder = TwoCirclesLinesBuilder(circle1, circle2, R)
lines = lines_builder.find_tangent_lines()
for line in lines:
    print(line)

