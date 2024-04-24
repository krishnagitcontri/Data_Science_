# WAP to check Armstrong number

def armstrongNumber(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

num = int(input("Enter a number: "))
if armstrongNumber(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
