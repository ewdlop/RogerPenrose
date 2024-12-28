with(plots):
stairs := plot3d([cos(t), sin(t), t], t = 0..2*Pi, coords = cylindrical, style = patchnogrid, color = red):
display(stairs);