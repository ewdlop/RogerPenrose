# Example analysis of a Nobel Prize-winning experiment
with(plots):
experiment := plot3d([x^2 + y^2, x, y], x = -1..1, y = -1..1, title = "$\\text{Nobel Prize Winning Experiment}$", labels = ["$x$", "$y$", "$z$"], gridlines = true, style = [point, line], symbol = diamond, symbolsize = 10):
display(experiment);
