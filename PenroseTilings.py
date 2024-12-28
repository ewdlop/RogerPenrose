with(plots):
golden_ratio := (1 + sqrt(5)) / 2:

# Function to create a rhombus
rhombus := proc(a, b, c, d)
    plot([a, b, c, d, a], style = polygon)
end proc:

# Coordinates for the rhombuses
A := [0, 0]:
B := [1, 0]:
C := [1/2, sqrt(3)/2]:
D := [-1/2, sqrt(3)/2]:

# Generate the tiling
display(
    seq(rhombus(A, B, C, D), i = 1..10),
    scaling = constrained, axes = none,
    title = "$\\text{Penrose Tiling}$",
    labels = ["$x$", "$y$"],
    gridlines = true
);
