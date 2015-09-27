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
    # calculate arithmetic sum for 3, 5, 15 (to remove duplicate terms)
    total = []
    for digit in [3,5,15]:
        a1 = digit
        num_terms = num // digit
        # highest term has to be <= num
        if num % digit == 0:
            num_terms -= 1
        an = digit * num_terms

        subtotal = (num_terms * (a1 + an)) / 2
        total.append(subtotal)

    # remove overlaps
    print total[0] + total[1] - total[2]