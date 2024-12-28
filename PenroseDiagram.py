with(plots):
penrose_diagram := plot([tanh(x), tanh(y)], x = -10..10, y = -10..10, axes = boxed, title = "$\\text{Penrose Diagram}$", labels = ["$x$", "$y$"], gridlines = true):
display(penrose_diagram);
