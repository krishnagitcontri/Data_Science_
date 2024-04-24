# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No.
# 3. Write an OOP program to perform addition, base and power, concatenation, max, min of two
# numbers stored in two different objects created from same class.

class NomNomNom:
    def __init__(self, num):
        self.num = num

    def add(self, other):
        return self.num + other.num

    def raised_to(self, other):
        return self.num ** other.num

    def concat(self, other):
        return int(str(self.num) + str(other.num))

    def max(self, other):
        return max(self.num, other.num)

    def min(self, other):
        return min(self.num, other.num)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
n1 = NomNomNom(a)
n2 = NomNomNom(b)
print("Addition:", n1.add(n2))  # 7
print(f"{a} raised to {b} is", n1.raised_to(n2))  # 32
print("Concat answer:", n1.concat(n2))  # 25
print("Max:", n1.max(n2))  # 5
print("Min:", n1.min(n2))  # 2