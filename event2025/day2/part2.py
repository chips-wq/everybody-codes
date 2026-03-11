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

LIMIT = 1_000_000

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

def is_engraved(P: Complex):
    R = Complex(0, 0)
    for _ in range(100):
        R = R * R
        R = R / Complex(100000, 100000)
        R = R + P
        if R.x > LIMIT or R.x < -LIMIT or R.y > LIMIT or R.y < -LIMIT: return False
    return True

def compute_engraved(P: Complex):
    R = Complex(0, 0)
    for _ in range(100):
        R = R * R
        R = R / Complex(100000, 100000)
        R = R + P
        if R.x > LIMIT or R.x < -LIMIT or R.y > LIMIT or R.y < -LIMIT: assert False
    return R

def test_is_engraved():
    compute_engraved(Complex(35630,-64880)) == Complex(-2520,-5355)
    compute_engraved(Complex(35630,-64870)) == Complex(5021,6454)
    compute_engraved(Complex(35640,-64860)) == Complex(-3291,-684)
    compute_engraved(Complex(36230,-64270)) == Complex(-7266,3234)
    compute_engraved(Complex(36250,-64270)) == Complex(162903,-679762)

if __name__ == '__main__':
    addition_tc()
    mul_tc()
    division_tc()
    test_is_engraved()

    infile = "part1.in" if len(sys.argv) < 2 else sys.argv[1]
    with open(infile, "r") as f:
        content = f.read().strip()
        tup = content.split("[")[1].split("]")[0].split(",")
        x, y = int(tup[0]), int(tup[1])
        A = Complex(x, y)
        
        ans = 0
        for xx in range(101):
            for yy in range(101):
                x1, y1 = A.x + xx * 10, A.y + yy * 10
                cc = Complex(x1, y1)
                if is_engraved(cc):
                    ans += 1
                    print("x", end="")
                else:
                    print(".", end="")
            print()
        print(f"{ans=}")

