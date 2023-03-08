from bisect import bisect
from math import prod
from datetime import datetime

def meb_sieve(limit):
    
    def expand(factors):
        f_copy = [*factors]
        f_copy.append(factors[-1])
        return f_copy
    
    prime_steps = {}
    def upgrade(factors):
        f_copy = [*factors]
        f_copy[-1] = prime_steps[factors[-1]]
        return f_copy
    
    latest_p = 2
    composites = {}
    
    for i in range(2, limit + 1):
        if i in composites:
            expanded_factors = expand(composites[i])
            composites[prod(expanded_factors)] = expanded_factors
   
            upgraded_factors = upgrade(composites[i])
            composites[prod(upgraded_factors)] = upgraded_factors
        else:
            if i > 2:
                prime_steps[latest_p] = i
                latest_p = i
            composites[i ** 2] = [i, i]
    
    primes = [2]
    while len(primes) <= len(prime_steps):
        primes.append(prime_steps[primes[-1]])
    
    return primes

t1 = datetime.now()
p = meb_sieve(10000000)
print(datetime.now() - t1, p[-1])       # less than 83 seconds on my smartphone
