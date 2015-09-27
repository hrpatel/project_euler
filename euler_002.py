__author__ = 'ray'

# get number of inputs
num_entries = int(raw_input())

# get each input in an array
inputs = []
for i in range(num_entries):
    num = int(raw_input())
    inputs.append(num)

# generate even fibonacci numbers
def even_fib(n):
    ax, ay = 0, 1
    while ax < n:
        if ax % 2 == 0:
            yield ax
        ax, ay = ay, ax + ay


# iterate through each
for num in inputs:
    print sum([x for x in even_fib(num)])