from fib import memoize
import random

# comment out the @memoize decorator to see the difference it makes.
@memoize
def lcs(a,b):
    if (len(a) == 0) or (len(b) == 0):
        return []

    if a[-1] == b[-1]:
        return lcs(a[:-1],b[:-1]) + [a[-1]]

    lcs_a = lcs(a,b[:-1])
    lcs_b = lcs(a[:-1],b)

    return max(lcs_a,lcs_b,key=len)

# lcs of two randomly generated strings of 0's and 1's, each of length 100.
print ''.join(lcs(''.join([random.choice('10') for x in range(100)]),''.join([random.choice('10') for x in range(100)])))
