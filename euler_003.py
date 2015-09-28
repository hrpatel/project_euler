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
    # initialize iterator, array, upper test limit
    itr = 2
    primes = []
    max_int = int(sqrt(n))

    # loop through each number in ascending order
    while itr <= max_int:
        # we're done
        if n == 1:
            break
        # we found a factor, start over
        if n % itr == 0:
            primes.append(itr)
            n /= itr
            itr = 2
        else:
            itr += 1

    # attach left over prime (1 is valid)
    primes.append(n)

    return primes

# iterate through each
for num in inputs:
    # find max and print
    print max([x for x in get_prime(num)])
