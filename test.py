from primality import isPrime

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
        if isPrime(p):
            print(f'{p} => may be a prime\n')
        else:
            print(f'{p} => Not prime\n')