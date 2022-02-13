"""
This is program written for finding all the powers, which will be no more than given number
"""

N = int(input('Choose your number: '))
n = 0
while N >= (n+1)**2:
    n += 1
    sqr = n**2
    print(sqr)

