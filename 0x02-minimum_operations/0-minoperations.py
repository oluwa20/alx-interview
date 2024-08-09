#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor <= n:
        # If n is divisible by factor, it's a prime factor
        while n % factor == 0:
            # Reduce n by factor and add the operation
            operations += factor
            n //= factor
        factor += 1
    
    return operations



