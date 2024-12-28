with(plots):
room := plot3d([x, y, sin(x+y)], x = -2*Pi..2*Pi, y = -2*Pi..2*Pi, style = patchnogrid, color = rainbow, title = "$\\text{Penrose Room}$", labels = ["$x$", "$y$", "$\\sin(x+y)$"], gridlines = true):
display(room);
