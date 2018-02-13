class Diff:
    def __init__(self, f, h=1E-4):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/(h)


# You don't actually need a class. Nested functions can do the job.
# deriv() uses f and h given to Diff()
# Diff() returns a function.

def Diff(f,h=1e-4):
    h = float(h)
    def deriv(x):
        return (f(x+h)-f(x))/h
    return deriv