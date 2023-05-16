# 
#   Student Taras Zherebetskyy
#   
from random import randint
from math import gcd, sqrt


def isPrime(p, k=128):
    '''
        if p is a prime number and 
        a is not a multiple of p [therefore gcd(p,a) = 1]
        then a^(p-1) = 1 (mod p)
    '''
    # testing for the most simple cases like: odd numbers
    if p <= 3:
        return True
    
    # if even
    if p % 2 == 0:
        return False
    
    # testing for k times
    a = set([randint(2, p - 1) for _ in range(k)]) # we do not need to test the same number twice. With set we eliminate the duplicates

    tests = set(map(lambda a: pow(base=a, exp=p-1, mod=p), a))

    if len(tests) > 1: 
        return False
    return True

    


