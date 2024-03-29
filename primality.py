#
#   Student Taras Zherebetskyy
#
from random import randint
from thread import ThreadReturn

def modpow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        exp = exp >> 1  # bit shift. equiv: p // 2
        base = (base**2) % mod

    return result


def isPrime(p, k=128):
    """
    if p is a prime number and
    a is not a multiple of p [therefore gcd(p,a) = 1]
    then a^(p-1) = 1 (mod p)
    """
    p_1 = p-1
    # testing for the most simple cases like: odd numbers
    if p <= 3:
        return True

    # if even
    if p % 2 == 0:
        return False

    # testing for k times
    a = set(
        [randint(2, p - 1) for _ in range(k)]
    )  # we do not need to test the same number twice. With set we eliminate the duplicates

    threads = list(map(lambda i: ThreadReturn(target=modpow, args=[i, p_1, p]), a))

    for thread in threads:
        thread.start()
    
    tests = set(map(lambda i: i.join(), threads))

    if len(tests) > 1:
        return False
    return True
