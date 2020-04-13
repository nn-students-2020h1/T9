import math

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def lenght_ab(self):
        l_ab = math.sqrt((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2)
        return l_ab

    def lenght_bc(self):
        l_bc = math.sqrt((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2)
        return l_bc

    def lenght_ac(self):
        l_ac = math.sqrt((self.cx - self.ax) ** 2 + (self.cy - self.ay) ** 2)
        return l_ac

    def perimeter(self):
        return (self.lenght_ab() + self.lenght_ac() + self.lenght_bc())

    def square(self):
        if type(self.ax) not in [int, float]:
            raise TypeError("Wrong Type")
        elif type(self.bx) not in [int, float]:
            raise TypeError("Wrong Type")
        p = (self.lenght_ab() + self.lenght_ac() + self.lenght_bc()) / 2
        s = math.sqrt(p * (p - self.lenght_ab()) * (p - self.lenght_ac()) * (p - self.lenght_bc()))
        return s