with(DEtools):
# Example differential equation modeling time loops
de := diff(y(t), t) = -y(t) + sin(t):
sol := dsolve(de, y(t)):
plot(rhs(sol), t = 0..10);