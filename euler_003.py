from math import sqrt

__author__ = 'ray'

# get number of inputs
num_entries = int(raw_input())

# get each input in an array
inputs = []
for i in range(num_entries):
    num = int(raw_input())
    inputs.append(num)

# find all prime numbers
def get_prime(n):

    max_int = int(sqrt(n))

    primes = []
    for i in xrange(2, max_int):
        if n % i == 0:
            primes.append(i)

    if not primes:
        primes.append(n)

    return primes

# iterate through each
for num in inputs:
    print max([x for x in get_prime(num)])
