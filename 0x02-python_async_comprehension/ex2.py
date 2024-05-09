#!/usr/bin/env python3


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(n):
    prime = []
    for i in range(2, n+1):
        if is_prime(i):
            prime.append(i)
    return prime

def prime_fact(n):
    prime_factor = []
    prime = generate_prime(n)
    
    for i in prime:
        while n % i == 0:
            prime_factor.append(i)
            n //= i
    return prime_factor

def minOperations(n):
    if n <= 1:
        return 0
    number_operations = prime_fact(n)
    sum = 0
    
    for operation in number_operations:
        sum += operation
    
    return sum

print(minOperations(4))