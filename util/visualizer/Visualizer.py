from typing import List

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from data_classes.Result.Result import Result
from data_classes.entities.Line.Line import Line
from data_classes.entities.Line.PlottedLine import PlottedLine
from data_classes.entities.Line.VerticalLine import VerticalLine

matplotlib.use('MACOSX')


class Visualizer:
    def __init__(self, circles, result: List[Result], xlim, ylim, R):
        self.circles = circles
        self.xlim = (0, xlim)
        self.ylim = (0, ylim)
        self.R = R
        self.lines = self.__to_plotted_lines(result)
        self.fig, self.ax = plt.subplots(figsize=(6, 8))
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.draw()

    def __to_plotted_lines(self, results: List[Result]) -> List[PlottedLine]:
        colors = ["red", "green", "blue"]
        plotted_lines = []
        for index in range(len(results)):
            line, label = results[index].get_line_and_label()
            plotted_line = PlottedLine(line, label, colors[index])
            plotted_lines.append(plotted_line)
        return plotted_lines



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
        self.ax.text(circle.x, circle.y, circle.weight, fontsize=6,
                     verticalalignment='center', horizontalalignment='center', color='black')

    def add_line(self, line_to_plot: PlottedLine):
        line = line_to_plot.line
        label = line_to_plot.label
        color = line_to_plot.color
        if isinstance(line, Line):
            self.__add_line(line, label, color)
        elif isinstance(line, VerticalLine):
            self.__add_vertical_line(line, label, color)

    def __add_line(self, line: Line, label, color):
        x_vals = np.linspace(0, self.xlim, 400)
        y_vals = line.k * x_vals + line.b
        self.ax.plot(x_vals, y_vals, color=color, linestyle='--', label=label)

    def __add_vertical_line(self, line: VerticalLine, label, color):
        self.ax.axvline(x=line.x, color=color, linestyle='--', label=label)
