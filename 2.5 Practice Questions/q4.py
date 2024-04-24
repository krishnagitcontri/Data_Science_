#WAP to print fibonacci series

def fibonacci(n):
    result = []
    n1, n2 = 0, 1
    count = 0

    while count < n:
        result.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

    return result

num = int(input("Enter a number: "))
print(fibonacci(num))