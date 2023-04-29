# 
#   Student Taras Zherebetskyy
#   
from random import randint
from math import gcd, sqrt


def isPrime(primeNum, k=128):
    '''
    Returns true or false
        if false the number is for sure not prime
        if true it may be prime
    '''
    # testing for the most simple cases like: odd numbers
    if primeNum <= 3:
        return True
    
    # if even
    if primeNum % 2 == 0:
        return False
    
    limit = int(sqrt(primeNum-1))

    if primeNum < 128:
        k = limit

    for _ in range(k):
        '''
            a can be any number but for performance is crucial to select the sqrt(p),
            since NO gcd of primeNumber (if any) is greater than sqrt(p)
        '''
        a = randint(2, limit)
        
        if gcd(primeNum % a, a) == 1: # gcd(primeNum, a) == gcd(primeNum % a, a)
            modulo = pow(base=a, exp=primeNum-1, mod=primeNum)
            if modulo == 1: continue
            else:
                return False
        else: 
            return False
    return True


