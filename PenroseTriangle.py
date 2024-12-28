with(plots):
triangle := plot3d([cos(t), sin(t), t/2], t = 0..2*Pi, coords = cylindrical, style = patchnogrid, color = blue, title = "$\\text{Penrose Triangle}$", labels = ["$t$", "$\\cos(t)$", "$\\sin(t)$"], gridlines = true):
display(triangle);
