from data_classes.generator.DataGenerator import DataGenerator
from data_classes.entities.GlobalData import GlobalData
from data_classes.entities.Circle import Circle


class InputDataGenerator(DataGenerator):
    def get_data(self) -> GlobalData:
        X, Y, R = list(map(float, input("Enter X, Y, R by whitespace: ").split()))
        circles = list(map(lambda circle_data: self.__get_circle_data(circle_data),
                           input(
                               "Enter x,y,weight for every circle separated by ',', every circle data must be separated by whitespace: ")
                           .split()))

        global_data = GlobalData(X, Y, R, circles)
        return global_data

    def __get_circle_data(self, circle_data: str):
        return Circle(*list(map(float, circle_data.split(","))))