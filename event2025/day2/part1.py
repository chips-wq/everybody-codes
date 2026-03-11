import sys

class Complex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
    
    def __eq__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __truediv__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(int(self.x/other.x), int(self.y/other.y))
    
    def __repr__(self):
        return f"Complex({self.x}, {self.y})"


"""
A few examples of addition:
assert(Complex(1,1) + Complex(2,2) == Complex(3,3))
assert(Complex(2,5) + Complex(3,7) == Complex(5,12))
assert(Complex(-2,5) + Complex(10,-1) == Complex(8,4))
assert(Complex(-1,-2) + Complex(-3,-4) == Complex(-4,-6))
"""

"""
multiplication

assert(Complex(1,1) * Complex(2,2) == Complex(0,4))
assert(Complex(2,5) * Complex(3,7) == Complex(-29,29))
assert(Complex(-2,5) * Complex(10,-1) == Complex(-15,52))
assert(Complex(-1,-2) * Complex(-3,-4) == Complex(-5,10))
"""

"""
division

assert(Complex(10,12) / Complex(2,2) == Complex(5,6))
assert(Complex(11,12) / Complex(3,5) == Complex(3,2))
assert(Complex(-10,-12) / Complex(2,2) == Complex(-5,-6))
assert(Complex(-11,-12) / Complex(3,5) == Complex(-3,-2))
"""

def addition_tc():
    assert(Complex(1,1) + Complex(2,2) == Complex(3,3))
    assert(Complex(2,5) + Complex(3,7) == Complex(5,12))
    assert(Complex(-2,5) + Complex(10,-1) == Complex(8,4))
    assert(Complex(-1,-2) + Complex(-3,-4) == Complex(-4,-6))


def mul_tc():
    assert(Complex(1,1) * Complex(2,2) == Complex(0,4))
    assert(Complex(2,5) * Complex(3,7) == Complex(-29,29))
    assert(Complex(-2,5) * Complex(10,-1) == Complex(-15,52))
    assert(Complex(-1,-2) * Complex(-3,-4) == Complex(-5,10))

def division_tc():
    assert(Complex(10,12) / Complex(2,2) == Complex(5,6))
    assert(Complex(11,12) / Complex(3,5) == Complex(3,2))
    assert(Complex(-10,-12) / Complex(2,2) == Complex(-5,-6))
    assert(Complex(-11,-12) / Complex(3,5) == Complex(-3,-2))

if __name__ == '__main__':
    addition_tc()
    mul_tc()
    division_tc()

    infile = "part1.in" if len(sys.argv) < 2 else sys.argv[1]
    with open(infile, "r") as f:
        content = f.read().strip()
        tup = content.split("[")[1].split("]")[0].split(",")
        x, y = int(tup[0]), int(tup[1])
        A = Complex(x, y)
        
        TEN = Complex(10, 10)

        R = Complex(0, 0)

        for _ in range(3):
            R = R * R
            R = R / TEN
            R = R + A

        print(R)

