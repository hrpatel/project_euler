from math import sqrt

__author__ = 'ray'

# get number of inputs
num_entries = int(raw_input())

# get each input in an array
inputs = []
for i in range(num_entries):
    num = int(raw_input())
    inputs.append(num)


def palindrome(test):
    """
    determine if a given number is a palindrome
    :param test: test string
    :return: True if 'test' is a palindrome
    """
    if len(test) == 1:
        return True
    elif len(test) == 2:
        return test[0] == test[1]
    else:
        return palindrome(test[1:-1])

print(palindrome("12345"))

exit()

# iterate through each
for num in inputs:
    # generate a product from 3 digit integers and check if the results are prime
    for x in xrange(100,1000):
        for y in xrange(100,1000):
            product = x * y
            if product < num and palindrome(str(product)):
                print(product)
