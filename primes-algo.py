from bisect import bisect
from math import prod

def meb_sieve(limit):
    
    def expand(factors):
        f = [*factors]
        f.append(factors[-1])
        return f
    
    def upgrade(factors, primes):
        next_index = bisect(primes, factors[-1])
        f = [*factors]
        f[-1] = primes[next_index]
        return f
    
    primes = []
    composites = {}
    
    for i in range(2, limit + 1):
        if i in composites:
            expanded_factors = expand(composites[i])
            composites[prod(expanded_factors)] = expanded_factors
   
            upgraded_factors = upgrade(composites[i], primes)
            composites[prod(expanded_factors)] = upgraded_factors
        else:
            primes.append(i)
            primes.sort()
            composites[i ** 2] = [i, i]
    
    return primes
