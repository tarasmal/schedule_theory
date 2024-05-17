import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

class Visualizer:
    def __init__(self, circles, lines, xlim, ylim, R):
        self.circles = circles
        self.lines = lines
        self.xlim = (0, xlim)
        self.ylim = (0, ylim)
        self.R = R
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.draw()


    def draw(self):
        for circle in self.circles:
            self.add_circle(circle)
        for line in self.lines:
            self.add_line(line)
        self.ax.legend()
        plt.show()

    def add_circle(self, circle):
        circ = plt.Circle((circle.x, circle.y), self.R, color="red", fill=False, linewidth=2)
        self.ax.add_patch(circ)
        self.ax.text(circle.x, circle.y, circle.weight, fontsize=int(self.R * 2),
                     verticalalignment='center', horizontalalignment='center', color='black')

    def add_line(self, line):
        x_vals = np.linspace(0, self.xlim, 400)
        y_vals = line.k * x_vals + line.b
        self.ax.plot(x_vals, y_vals, color="green", linestyle='--', label="test_label")

