# write a Python program to solve quadratic equation using OOP.
# the standard form of a quadratic equation is:
# where a, b and c are real numbers and The solutuons of this quadratic equation is given by:
# ax + bx + c = 0
# 2
# a != 0
#(-b ± (b - 4ac)/ 2a

import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("a must not be zero")
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant < 0:
            raise ValueError("No real solutions")
        sqrt_discriminant = math.sqrt(discriminant)
        solution1 = (-self.b + sqrt_discriminant) / (2*self.a)
        solution2 = (-self.b - sqrt_discriminant) / (2*self.a)
        return solution1, solution2

eq = QuadraticEquation(1, -3, 2)
solution1, solution2 = eq.solve()
print(f"The solutions are {solution1} and {solution2}")