def meb_sieve(limit):  
    def product(factors): 
        p = 1 
        for x in factors: 
            p *= x 
        return p 
    def expand(factors): 
        return [*factors, factors[-1]] 
    def upgrade(factors, primes): 
        j = primes.index(factors[-1]) 
        return [*factors[:-1], primes[j + 1]] 
    primes = [] 
    composites = set() 
    factors_dict = {} 
    for i in range(2, limit + 1): 
        if not i in composites: 
            bisect.insort(primes, i) 
            composites.add(i ** 2) 
            factors_dict[i ** 2] = [i, i] 
        else: 
            expanded_factors = expand(factors_dict[i]) 
            c = product(expanded_factors) 
            composites.add(c) 
            factors_dict[c] = expanded_factors 
            upgraded_factors = upgrade(factors_dict[i], primes) 
            c = product(upgraded_factors) 
            composites.add(c) 
            factors_dict[c] = upgraded_factors 
    return primes
