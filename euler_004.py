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
        if test[0] == test[-1]:
            return palindrome(test[1:-1])
        else:
            return False


def main():

    # generate all 6 digit palindromes that are a product of 3 digit integers
    palindromes = set()
    for x in xrange(100,1000):
        for y in xrange(100,1000):
            product = x * y
            if product > 100000 and palindrome(str(product)):
                palindromes.add(product)

    # make a sorted list of palindromes
    l = list(palindromes)
    l.sort()

    # iterate through each input
    for num in inputs:
        # input constraints
        if num < 101102 or num > 999999:
            continue

        # find the closest palindrome to the input
        for val in xrange(len(l)):
            if l[val] > num:
                print l[val-1]
                break


main()