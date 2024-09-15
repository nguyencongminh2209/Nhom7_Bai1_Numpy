import os
import PyQt6.QtWidgets
import matplotlib.colors as mcolors
import sympy
from .Equation import Equation

class EquationTab(PyQt6.QtWidgets.QWidget):
    colors = tuple(mcolors.TABLEAU_COLORS.keys())

    def __init__(self):
        super().__init__()

        # Create layout
        self.plot = None
        self.layout = PyQt6.QtWidgets.QVBoxLayout()

        # Add label
        self.label = PyQt6.QtWidgets.QLabel("Equations")

        # Add label to layout
        self.layout.addWidget(self.label)

        # Add button
        self.button = PyQt6.QtWidgets.QPushButton("Add Equation")

        # Add equation when button is clicked
        self.button.clicked.connect(self.add_equation)

        self.refresh_button = PyQt6.QtWidgets.QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)

        # Add buttons to layout
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.refresh_button)

        # Set layout
        self.setLayout(self.layout)

    def add_equation(self):
        # Create equation
        equation = Equation()

        # Add equation to the second to last position of the layout
        self.layout.insertWidget(self.layout.count() - 2, equation)

    def refresh(self):
        # Loop over all Equation widgets
        plot = None
        for widget in self.findChildren(Equation):
            equation = widget
            if equation.equation_right is None:
                continue
            lhs, rhs = equation.equation_left, equation.equation_right
            intersection_points = sympy.solve(lhs - rhs, sympy.var("y"))

            for f in sympy.solve(lhs - rhs, sympy.var("y")):
                label = f'y = {f}'
                if plot is None:
                    plot = sympy.plotting.plot(f, show=False, line_color=self.colors[len(plot.series)], ylabel="y", legend=True, label=label)
                else:
                    plot.extend(sympy.plotting.plot(f, show=False, line_color=self.colors[len(plot.series)], ylabel="y", legend=True, label=label))
        
        if plot is not None:
            cache_dir = "cache"
            if not os.path.exists(cache_dir):
                os.mkdir(cache_dir)
            plot.save(os.path.join(cache_dir, "graph.png"))
            self.plot = plot
            self.parent().parent().refresh()
