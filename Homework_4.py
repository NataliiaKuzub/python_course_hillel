"""
This is program written for finding the max power of two, which will be less than given number
"""

N = int(input('Choose your number: '))
n = 1
pow = 0

while N > n:
    n *= 2
    pow +=1
else:
    print(int(n/2), 'is the max power of 2, which is less than your number. It is 2 in the power of', pow-1)