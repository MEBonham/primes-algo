from bisect import bisect
from math import prod

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
    
    latest_p = 0
    primes = []
    composites = {}
    
    for i in range(2, limit + 1):
        if i in composites:
            expanded_factors = expand(composites[i])
            composites[prod(expanded_factors)] = expanded_factors
   
            upgraded_factors = upgrade(composites[i], primes)
            composites[prod(upgraded_factors)] = upgraded_factors
        else:
            primes.append(i)
            if i > 2:
                prime_steps[latest_p] = i
                latest_p = i
            composites[i ** 2] = [i, i]
    
    return primes.sort()
