from typing import Tuple

from data_classes.entities.Line.AbstractLine import AbstractLine


class Result:
    def __init__(self, line: AbstractLine, line_weight, execution_duration, solver_name):
        self.line = line
        self.line_weight = line_weight
        self.execution_duration = execution_duration
        self.solver_name = solver_name

    def get_line_and_label(self) -> Tuple[AbstractLine, str]:
        return self.line, self.solver_name

    def __str__(self):
        return f"""
Solver: {self.solver_name}
Line: {self.line}
Line weight: {self.line_weight}
Execution duration: {self.execution_duration} seconds
"""