# WAP to print all prime numbers in a given interval

def isPrime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))
isPrime(start, end)