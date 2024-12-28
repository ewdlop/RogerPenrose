with(plots):
# Example Schrödinger equation with gravitational potential
psi := t -> exp(-t^2 + I*t):
plot(abs(psi(t)), t = -10..10, title = "Quantum System under Gravitational Effects");