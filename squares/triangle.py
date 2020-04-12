class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def square(self):
        if type(self.a) and type(self.h) not in [int, float]:
            raise TypeError("Wrong Type")
        elif self.a < 0 or self.h < 0:
            raise ValueError("Negative Values")
        return self.a*self.h/2