with(plots):
# Example calculation for energy extraction
energy := (1 - sqrt(1 - 2/3)):
plot(energy, 0..1, color = green, title = "$\\text{Energy Extraction in Penrose Process}$", labels = ["$x$", "$\\text{Energy}$"], gridlines = true, style = [point, line], symbol = diamond, symbolsize = 10);
