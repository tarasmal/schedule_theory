import numpy as np


class CircleLineSystemEquationsSolver:

    @staticmethod
    def solve_equation(circle_coordinates, line_coordinates):
        a, b, r = circle_coordinates
        k, x = line_coordinates
        A = 1 + k ** 2
        B = 2 * k * (x - b) - 2 * a
        C = a ** 2 + (x - b) ** 2 - r ** 2
        discriminant = B ** 2 - 4 * A * C
        result = []
        if discriminant > 0:
            x1 = (-B + np.sqrt(discriminant)) / (2 * A)
            x2 = (-B - np.sqrt(discriminant)) / (2 * A)
            y1 = k * x1 + x
            y2 = k * x2 + x
            result = [(x1, y1), (x2, y2)]
        elif discriminant == 0:
            x = -B / (2 * A)
            y = k * x + x
            result = [(x, y)]
        return result

    @staticmethod
    def check_intersection(circle_coordinates, line_coordinates):
        return True if CircleLineSystemEquationsSolver.solve_equation(circle_coordinates, line_coordinates) else False
