__author__ = 'ray'

# get number of inputs
num_entries = int(raw_input())

# get each input in an array
inputs = []
for i in range(num_entries):
    num = int(raw_input())
    inputs.append(num)

# iterate through each input
for num in inputs:
    # calculate arithematic sum for 3, 5
    total = []
    for digit in [3,5]:
        a1 = digit
        num_terms = num // digit
        if num % digit == 0:
            num_terms -= 1
        an = digit * num_terms

        subtotal = (num_terms * (a1 + an)) / 2
        total.append(subtotal)

    # remove overlaps
    a1 = 15
    num_terms = num // 15
    an = 15 * num_terms
    print sum(total) - (num_terms * (a1 + an) / 2)