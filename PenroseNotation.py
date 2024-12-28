# Penrose graphical notation is complex and usually done by hand, but here's a simple tensor diagram example
with(plots):
tensor_diagram := plot([cos(t), sin(t)], t = 0..2*Pi, color = blue, title = "$\\text{Simple Tensor Diagram}$", labels = ["$t$", "$\\cos(t)$", "$\\sin(t)$"], gridlines = true, style = [point, line], symbol = diamond, symbolsize = 10):
display(tensor_diagram);
