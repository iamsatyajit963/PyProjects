# Write a python program to print first n Fibonacci numbers

def fibo(n):
    if (n<=1):
        return n
    else:
        return (fibo(n-1)+ fibo(n-2))

nterms = int(input("Enter nterms for Fibonacci serires: "))

if(nterms <= 0):
    print("Enter positive number")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(fibo(i))