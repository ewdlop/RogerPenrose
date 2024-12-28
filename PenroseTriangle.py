with(plots):
triangle := plot3d([cos(t), sin(t), t/2], t = 0..2*Pi, coords = cylindrical, style = patchnogrid, color = blue):
display(triangle);