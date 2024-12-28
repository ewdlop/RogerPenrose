with(plots):
# Example cosmological equation for big bounce
a := t -> cosh(t):
plot(a(t), t = -5..5, color = red, title = "Big Bounce Dynamics", labels = ["$t$", "$a(t)$"], gridlines = true, style = [point, line], symbol = diamond, symbolsize = 10);
