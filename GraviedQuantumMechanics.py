with(plots):
# Example Schrödinger equation with gravitational potential
psi := t -> exp(-t^2 + I*t):
plot(abs(psi(t)), t = -10..10, title = "$\\text{Quantum System under Gravitational Effects}$", labels = ["$t$", "$|\\psi(t)|$"], gridlines = true, style = [point, line], symbol = diamond, symbolsize = 10);
