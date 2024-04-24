# WAP to display multiplication Table (for loop)

def multiTable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiTable(num)