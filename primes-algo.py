from bisect import bisect
from math import prod
from datetime import datetime

def meb_sieve(limit):
    
    def expand(factors):
        f_copy = [*factors]
        f_copy.append(factors[-1])
        return f_copy
    
    prime_steps = {}
    def upgrade(factors, primes):
        f_copy = [*factors]
        f_copy[-1] = prime_steps[factors[-1]]
        return f_copy
    
    latest_p = 2
    primes = []
    composites = {}
    
    for i in range(2, limit + 1):
        print(i)
        if i in composites:
            expanded_factors = expand(composites[i])
            print("expansion", prod(expanded_factors))
            composites[prod(expanded_factors)] = expanded_factors
   
            upgraded_factors = upgrade(composites[i], primes
            print("upgrade", prod(upgraded_factors))
            composites[prod(upgraded_factors)] = upgraded_factors
        else:
            primes.append(i)
            if i > 2:
                prime_steps[latest_p] = i
                latest_p = i
                print(prime_steps)
            composites[i ** 2] = [i, i]
    
    return primes.sort()

t1 = datetime.now()
p = meb_sieve(10)
print(datetime.now() - t1, p[-1])
