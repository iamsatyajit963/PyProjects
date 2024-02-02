"""
Take a postive number as input from the user. Display all the twin prime numbers equal to or less than the input number.
Twin numbers are prime numbers which have a difference of two.

if no twin prime numbers are found, then display 0. If inpur is non-positive or zero then display -1

Input Format: The input String will contain a single Integer
Ouput format: A string in which integers of a twin prime pair should be separated by colon and each pair should be separated by comma

example 20 -> 3:5,5:7,11:13,17:19
3 -> 0
-8 -> -1
"""

inputstring=input()
n=int(inputstring)
prime = [True for i in range(n+2)]

p = 2

while (p * p <= n+1):
    if(prime[p] == True):
        for i in range(p*2, n+2, p):
            prime[i]= False
    p+=1

for p in range (2,n-1):
    if(prime[p] and prime[p+2]):
        print("{0}:{1}".format(p,p+2),",",end="")