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
    itr = 2
    primes = []
    while itr <= max_int:
        if n == 1:
            break
        if n % itr == 0:
            primes.append(itr)
            n /= itr
            itr = 2
        else:
            itr += 1

    primes.append(n)

    return primes

# iterate through each
for num in inputs:
    print max([x for x in get_prime(num)])
