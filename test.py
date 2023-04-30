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
        201181192685185252019112523, # not prime
        # The number bellow is a prime
        150480188081237471404602331543794130711001857842571187235980008491419259102293002032453227733908743782233833131600886731093508825156766343809332959958321690961369166739945034620991796836742667926262887101099273255817101468205392395761233445341276682087698486876674554267763749050037673904538985360519
    ]

    for p in numbers:
        if isPrime(p):
            print(f'{p} => may be a prime\n')
        else:
            print(f'{p} => Not prime\n')