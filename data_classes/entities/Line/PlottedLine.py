from data_classes.entities.Line.AbstractLine import AbstractLine


class PlottedLine:
    def __init__(self, line: AbstractLine, label: str, color):
        self.line = line
        self.label = label
        self.color = color
