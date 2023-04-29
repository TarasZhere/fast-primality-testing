# 
#   Student Taras Zherebetskyy
#   
from random import randint
from math import gcd, sqrt


def primality(primeNum, k=128):
    
    # testing for the most simple cases like: odd numbers
    if primeNum <= 3:
        return True
    # if even
    elif primeNum % 2 == 0:
        return False

    for _ in range(k):
        '''
            Selecting an a is crucial for performance!
            a can be any number but for performance is crucial to select the sqrt(p),
            since NO gcd of primeNumber (if any) is greater than sqrt(p)
        '''
        a = randint(2, int(sqrt(primeNum-1)))

        
        if gcd(primeNum % a, a) == 1: # gcd(primeNum, a) == gcd(primeNum % a, a)
            modulo = pow(base=a, exp=primeNum-1, mod=primeNum)
            if modulo == 1: continue
            else:
                return False
        else: 
            return False
    return True


if __name__=="__main__":
    numbers = [
        31, # prime number
        17, # prime number
        394893589358942, # Not a prime larg number
        169665573205075467667167, # I discovered that it is divisibile by 3
        557940830126698960967415391, # Not prime
        10106665597294733930808268834911, # Not prime - divisibile by 3
        2305567963945518424753102147331756071, # Not prime

        # Found this number to test which is one of the largest prime numbers 
        170141183460469231731687303715884105727, # This is a prime
    ]
    for p in numbers:
        if primality(p):
            print(f'{p} => may be a prime\n')
        else:
            print(f'{p} => Not prime\n')

