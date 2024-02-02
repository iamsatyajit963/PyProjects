# Getting all the Divisors
def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            print(i)
    print(n)
    
get_divisors(220)